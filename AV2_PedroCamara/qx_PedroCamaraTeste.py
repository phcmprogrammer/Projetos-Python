import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
    )

crs = mydb.cursor()

execsqlcmd = lambda cmd,crs: crs.execute(cmd)

execcreatetable = lambda table, attrs,crs: execsqlcmd("CREATE TABLE " + table + " (" + attrs + ");\n", crs)
execcreatedatabase = lambda dbname,crs: execsqlcmd("CREATE DATABASE " + dbname + ";\n", crs)
execdropdatabase = lambda dbname,crs: execsqlcmd("DROP DATABASE " + dbname + ";\n", crs)
execdroptable = lambda dbname,crs: execsqlcmd("DROP TABLE " + dbname + ";\n", crs)
execusedatabase = lambda dbname,crs: execsqlcmd("USE " + dbname + ";\n", crs)
execselectfromwhere = lambda attrs, table, whrecond,crs: execsqlcmd("SELECT " + attrs +" FROM " + table + " WHERE "
execcreatetable = lambda table, attrs,crs: execsqlcmd("CREATE TABLE " + table + " (" + attrs + ");\n", crs)


