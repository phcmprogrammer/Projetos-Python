import mysql.connector

# Conexão com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ph@290193"
)

crs = mydb.cursor()

execsqlcmd = lambda cmd, crs: crs.execute(cmd)
execcreatetable = lambda table, attrs, crs: execsqlcmd(f"CREATE TABLE {table} ({attrs});", crs)
execcreatedatabase = lambda dbname, crs: execsqlcmd(f"CREATE DATABASE {dbname};", crs)
execdropdatabase = lambda dbname, crs: execsqlcmd(f"DROP DATABASE {dbname};", crs)
execdroptable = lambda table, crs: execsqlcmd(f"DROP TABLE {table};", crs)
execusedatabase = lambda dbname, crs: execsqlcmd(f"USE {dbname};", crs)
execselectfromwhere = lambda attrs, table, wherecond, crs: execsqlcmd(f"SELECT {attrs} FROM {table} WHERE {wherecond};", crs)
execinsertinto = lambda table, attrs, values, crs: execsqlcmd(f"INSERT INTO {table} ({attrs}) VALUES ({values});", crs)
execdeletefromwhere = lambda table, wherecond, crs: execsqlcmd(f"DELETE FROM {table} WHERE {wherecond};", crs)

#Scaffold
exec_inner_join = lambda select_attrs, from_table, joins, where_cond, crs: [crs.execute(f"SELECT {select_attrs} FROM {from_table} " + " ".join(f"INNER JOIN {j[0]} ON {j[1]}" for j in joins) + f" WHERE {where_cond};"), crs.fetchall()]
exec_select = lambda attrs, tables, where_cond, crs: [crs.execute(f"SELECT {attrs} FROM {tables} WHERE {where_cond};"), crs.fetchall()]

# Exemplo de uso das funções lambda
execcreatedatabase("testdatabase", crs)
execusedatabase("testdatabase", crs)

execcreatetable("USERS", "id VARCHAR(255), name VARCHAR(255), country VARCHAR(255), id_console VARCHAR(255)", crs)
execcreatetable("VIDEOGAMES", "id_console VARCHAR(255), name VARCHAR(255), id_company VARCHAR(255), release_date VARCHAR(255)", crs)
execcreatetable("GAMES", "id_game VARCHAR(255), title VARCHAR(255), genre VARCHAR(255), release_date VARCHAR(255), id_console VARCHAR(255)", crs)
execcreatetable("COMPANY", "id_company VARCHAR(255), name VARCHAR(255), country VARCHAR(255)", crs)

execinsertinto("USERS", "id, name, country, id_console", "'1', 'Pedro', 'Brasil', '1'", crs)
execinsertinto("VIDEOGAMES", "id_console, name, id_company, release_date", "'1', 'Super Nintendo', '1', '21/11/1990'", crs)
execinsertinto("GAMES", "id_game, title, genre, release_date, id_console", "'1', 'Mario Kart', 'Racing game', '27/08/1992', '1'", crs)
execinsertinto("COMPANY", "id_company, name, country", "'1', 'Nintendo', 'Japão'", crs)

results = exec_inner_join("*", "GAMES", [("VIDEOGAMES", "GAMES.id_console = VIDEOGAMES.id_console"), ("COMPANY", "VIDEOGAMES.id_company = COMPANY.id_company")], "GAMES.release_date > '1990-01-01'", crs)[1]
print_result = lambda res: [print(x) for x in res]
print_result(results)

execdroptable("USERS", crs)
execdroptable("VIDEOGAMES", crs)
execdroptable("GAMES", crs)
execdroptable("COMPANY", crs)
execdropdatabase("testdatabase", crs)

mydb.close()
