import sqlite3
#import jsonload

def sql_create_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS usuarios (dni text, nombre text, altura real)")
    cursorObj.execute("INSERT INTO usuarios VALUES ('X', 'isaac', '1.85') ")
    con.commit()

def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE usuarios SET nombre = "Sergio" where dni = "X"')
    con.commit()

def sql_print(con):
   cursorObj = con.cursor()
   cursorObj.execute('SELECT * FROM usuarios')
   #SELECT dni, nombre FROM usuarios WHERE altura > 1.0
   rows = cursorObj.fetchall()
   for row in rows:
    print(row)

def sql_delete_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('drop table if exists usuarios')
    con.commit()

con = sqlite3.connect('example.db')
sql_create_table(con)
sql_print(con)
sql_update(con)
sql_print(con)
#sql_fetch(con)
#sql_delete(con)
#sql_fetch(con)
sql_delete_table(con)
con.close()