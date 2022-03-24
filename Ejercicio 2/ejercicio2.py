import sqlite3
import json
import pandas as pd
import numpy as np

with open('users.json') as file:
    # Transform json input to python objects
    data = json.load(file)


def sql_create_table(con):
    cursorObj = con.cursor()

    # TABLA PARA USUARIOS
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS usuariosTable (nombre, telefono, contrasena, provincia, permisos, emailTotal, emailPhishing, emailCliclados)")
    for usuarios in range(len(data['usuarios'])):
        for name in data['usuarios'][usuarios].keys():
            telefono = str(data['usuarios'][usuarios][name]['telefono'])
            contra = str(data['usuarios'][usuarios][name]['contrasena'])
            provincia = str(data['usuarios'][usuarios][name]['provincia'])
            permisos = str(data['usuarios'][usuarios][name]['permisos'])
            emailTotal = str(data['usuarios'][usuarios][name]['emails']['total'])
            emailPhishing = str(data['usuarios'][usuarios][name]['emails']['phishing'])
            emailCliclados = str(data['usuarios'][usuarios][name]['emails']['cliclados'])

            cursorObj.execute(
                'INSERT INTO usuariosTable (nombre, telefono, contrasena, provincia, permisos, emailTotal, emailPhishing, emailCliclados) VALUES (?,?,?,?,?,?,?,?)',
                (name, telefono, contra, provincia, permisos, emailTotal, emailPhishing, emailCliclados))
            con.commit()

    # TABLA PARA FECHAS
    cursorObj.execute("CREATE TABLE IF NOT EXISTS fechasTable (nombre, fechas)")
    for usuarios in range(len(data['usuarios'])):
        for name in data['usuarios'][usuarios].keys():
            for fecha in data['usuarios'][usuarios][name]['fechas']:
                cursorObj.execute('''INSERT INTO fechasTable (nombre, fechas) VALUES (?,?)''', (name, str(fecha),))
                con.commit()

    # TABLA PARA IPS
    cursorObj.execute("CREATE TABLE IF NOT EXISTS ipsTable (nombre, ips)")
    for usuarios in range(len(data['usuarios'])):
        for name in data['usuarios'][usuarios].keys():
            for ip in data['usuarios'][usuarios][name]['ips']:
                cursorObj.execute('''INSERT INTO ipsTable (nombre, ips) VALUES (?,?)''', (name, str(ip),))
                con.commit()


def sql_print(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM usuariosTable')
    rowsUser = cursorObj.fetchall()
    for rowUser in rowsUser:
        print(rowUser)

    cursorObj.execute('SELECT * FROM fechasTable')
    rowsFecha = cursorObj.fetchall()
    for rowFecha in rowsFecha:
        print(rowFecha)

    cursorObj.execute('SELECT * FROM ipsTable')
    rowsIp = cursorObj.fetchall()
    for rowIp in rowsIp:
        print(rowIp)


def sql_delete_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP TABLE IF EXISTS usuariosTable')
    con.commit()
    cursorObj.execute('DROP TABLE IF EXISTS fechasTable')
    con.commit()
    cursorObj.execute('DROP TABLE IF EXISTS ipsTable')
    con.commit()


def dataframe():
    df = pd.read_sql_query("SELECT * FROM usuariosTable GROUP BY nombre", con)
    df["fechas"] = pd.read_sql_query("SELECT COUNT(fechas) FROM fechasTable GROUP BY nombre", con)
    df["ips"] = pd.read_sql_query("SELECT COUNT(ips) FROM ipsTable GROUP BY nombre", con)
    return df


con = sqlite3.connect('ejercicio2.db')
sql_create_table(con)
# sql_print(con)
df = dataframe()
print(df)
# sql_delete_table(con)
con.close()
# eval()
