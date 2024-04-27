import mysql.connector

# Conexão com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ph@290193"
)

crs = mydb.cursor()

execsqlcmd = lambda cmd, crs: crs.execute(cmd)

execcreatetable = lambda table, attrs, crs : execsqlcmd ("CREATE TABLE " + table + " (" + attrs + ");\n", crs)
execcreatedatabase = lambda dbname, crs : execsqlcmd ("CREATE DATABASE " + dbname + ";\n", crs)
execdropdatabase = lambda dbname, crs : execsqlcmd ("DROP DATABASE " + dbname + ";\n", crs)
execdroptable = lambda table, crs : execsqlcmd ("DROP TABLE " + table + ";\n", crs)
execusedatabase = lambda dbname, crs : execsqlcmd ("USE " + dbname + ";\n", crs)
execselectfromwhere = lambda attrs, table, wherecond, crs : execsqlcmd ("SELECT " + attrs + " FROM " + table + " WHERE " + wherecond + ";\n", crs)
execinsertinto = lambda table, attrs, values, crs : execsqlcmd ("INSERT INTO " + table + " (" + attrs + ")" + " VALUES (" + values + ")" + ";\n", crs)
execdeletefromwhere = lambda table, wherecond, crs : execsqlcmd("DELETE FROM " + table + " WHERE " + wherecond + ";\n", crs)

# Criação do database
#execdropdatabase ("testdatabase", crs)
execcreatedatabase ("testdatabase", crs)
execusedatabase ("testdatabase", crs)

# Criação das tabelas
execcreatetable ("USERS" , "id VARCHAR (255) , name VARCHAR (255) , country VARCHAR (255) , id_console VARCHAR (255)", crs)
execcreatetable ("VIDEOGAMES" , "id_console VARCHAR (255) , name VARCHAR (255) , id_company VARCHAR (255), release_date VARCHAR (255) ", crs)
execcreatetable ("GAMES" , "id_game VARCHAR (255) , title VARCHAR (255) , genre VARCHAR (255) , release_date VARCHAR (255) , id_console VARCHAR (255)", crs)
execcreatetable ("COMPANY" , "id_company VARCHAR (255) , name VARCHAR (255) , country VARCHAR (255)", crs)

#Inserir atributos nas tabelas
execinsertinto("USERS", "id , name , country , id_console", "'1' , 'Pedro' , 'Brasil' , '1'", crs)
execinsertinto("USERS", "id , name , country , id_console", "'2' , 'Lais' , 'Brasil' , '2'", crs)
execinsertinto("VIDEOGAMES", "id_console , name , id_company , release_date", "'1' , 'Super Nintendo' , '1' , '21/11/1990'", crs)
execinsertinto("GAMES", "id_game , title , genre , release_date , id_console", "'1' , 'Mario Kart' , 'Racing game' , '27/08/1992' , '1'", crs)
execinsertinto("COMPANY", "id_company , name , country", "'1' , 'Nintendo' , 'Japão'", crs)

#Remoção de elementos da tabela
execdeletefromwhere("USERS", "id='2'", crs)

#Consultar registros de tabelas
execselectfromwhere ("*", "USERS", "true", crs)
#execselectfromwhere ("*", "VIDEOGAMES", "true", crs)
#execselectfromwhere ("*", "GAMES", "true", crs)
#execselectfromwhere ("*", "COMPANY", "true", crs)
#execselectfromwhere ("*", "USERS , VIDEOGAMES , GAMES , COMPANY", "true", crs)

res = crs.fetchall ()
print_result = lambda res : [print (x) for x in res]

print_result (res)

execdroptable ("USERS", crs)
execdroptable ("VIDEOGAMES", crs)
execdroptable ("GAMES", crs)
execdroptable ("COMPANY", crs)
execdropdatabase ("testdatabase", crs)

mydb.close()