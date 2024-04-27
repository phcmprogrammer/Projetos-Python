from flask import Flask, request, jsonify
import mysql.connector
import bcrypt

app = Flask(__name__)

# Conexão com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ph@290193"
)
crs = mydb.cursor()

# Lambda Commands
execsqlcmd = lambda cmd, cursor: cursor.execute(cmd)
execusedatabase = lambda dbname, cursor: execsqlcmd(f"USE {dbname};", cursor)
execselectfromwhere = lambda attrs, table, wherecond, cursor: execsqlcmd(f"SELECT {attrs} FROM {table} WHERE {wherecond};", cursor)
execinsertinto = lambda table, attrs, values, cursor: execsqlcmd(f"INSERT INTO {table} ({attrs}) VALUES ({values});", cursor)
execcreatetable = lambda table, attrs, cursor: execsqlcmd(f"CREATE TABLE IF NOT EXISTS {table} ({attrs});", cursor)
execcreatedatabase = lambda dbname, cursor: execsqlcmd(f"CREATE DATABASE IF NOT EXISTS {dbname};", cursor)

# Criar banco de dados e usar
execcreatedatabase("testdatabase", crs)
execusedatabase("testdatabase", crs)

# Criação de tabela com senha criptografada
create_user_table = lambda cursor: execcreatetable("USERS", "id VARCHAR(255), name VARCHAR(255), country VARCHAR(255), id_console VARCHAR(255), password VARCHAR(255)", cursor)
create_user_table(crs)

hash_password = lambda password: bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

insert_user = lambda id, name, country, id_console, password, cursor: execinsertinto("USERS", "id, name, country, id_console, password", f"'{id}', '{name}', '{country}', '{id_console}', '{hash_password(password)}'", cursor) or mydb.commit()

@app.route('/')
def home():
    return "Welcome to the Flask Server! Professor Samuel Barrocas"

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    insert_user(data['id'], data['name'], data['country'], data['id_console'], data['password'], crs)
    return jsonify({'status': 'success'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    execselectfromwhere("password", "USERS", f"id = '{data['id']}'", crs)
    user_record = crs.fetchone()
    if user_record and bcrypt.checkpw(data['password'].encode('utf-8'), user_record[0].encode('utf-8')):
        return jsonify({'status': 'login successful'}), 200
    else:
        return jsonify({'status': 'login failed'}), 401

if __name__ == '__main__':
    app.run(debug=True)
