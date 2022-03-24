import sqlite3
import json

with open('users.json') as file:
    # Transform json input to python objects
    data = json.load(file)

def sql_create_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS usuariosTable (nombre, telefono, contrasena, provincia, permisos, emailTotal, emailPhishing, emailCliclados, fechas, ips)")

    for usuarios in range(len(data['usuarios'])):
        #print(str(data['usuarios'][usuarios]))
        for name in data['usuarios'][usuarios].keys():
            telefono = str(data['usuarios'][usuarios][name]['telefono'])
            contra = str(data['usuarios'][usuarios][name]['contrasena'])
            provincia = str(data['usuarios'][usuarios][name]['provincia'])
            permisos = str(data['usuarios'][usuarios][name]['permisos'])
            emailTotal = str(data['usuarios'][usuarios][name]['emails']['total'])
            emailPhishing = str(data['usuarios'][usuarios][name]['emails']['phishing'])
            emailCliclados = str(data['usuarios'][usuarios][name]['emails']['cliclados'])

            # fechas = []
            # for fecha in data['usuarios'][usuarios][name]['fechas']:
                # fechas.append(fecha)
            # stringFechas = " - ".join(fechas)

            # arrayFechas = stringFechas.split("-")
            # print(stringFechas)

            # ips = []
            # for ip in data['usuarios'][usuarios][name]['ips']:
                # ips.append(ip)
            # stringIps = " - ".join(ips)

            # arrayIps = stringIps.split("-")
            # print(arrayIps)

            #cursorObj.execute(
                #"INSERT INTO usuariosTable VALUES ('name', 'telefono', 'contra', 'provincia', 'permisos', 'emailTotal', 'emailPhishing', 'emailCliclados') ")
            cursorObj.execute('INSERT INTO usuariosTable (nombre, telefono, contrasena, provincia, permisos, emailTotal, emailPhishing, emailCliclados, fechas, ips) VALUES (?,?,?,?,?,?,?,?)',(name,telefono, contra, provincia, permisos, emailTotal, emailPhishing, emailCliclados, stringFechas, stringIps))
            con.commit()


def sql_print(con):
   cursorObj = con.cursor()
   cursorObj.execute('SELECT * FROM usuariosTable')
   rows = cursorObj.fetchall()
   for row in rows:
    print(row)

def sql_delete_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP TABLE IF EXISTS usuariosTable')
    con.commit()

con = sqlite3.connect('BBDDprueba2.db')
sql_create_table(con)
sql_print(con)
sql_delete_table(con)
con.close()
#eval()