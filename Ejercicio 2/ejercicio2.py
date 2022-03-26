import sqlite3
import pandas as pd


def dataframe():
    df = pd.read_sql_query("SELECT * FROM usuariosTable GROUP BY nombre", con)
    df["fechas"] = pd.read_sql_query("SELECT COUNT(fechas) FROM fechasTable GROUP BY nombre", con)
    df["ips"] = pd.read_sql_query("SELECT COUNT(ips) FROM ipsTable GROUP BY nombre", con)
    return df


def dataframeIps():
    dfIp = pd.read_sql_query("SELECT (ips) FROM ipsTable GROUP BY nombre", con)
    return dfIp


con = sqlite3.connect('./database.db')

df = dataframe()
# print(df)

dfIp = dataframeIps()
print(dfIp)

# EJERCICIO 2

# Número de muestras (valores distintos de missing)

missing = 0
for index, row in df.iterrows():
    if row["telefono"] == "None":
        missing += 1
    if row["provincia"] == "None":
        missing += 1

for index, row in dfIp.iterrows():
    if row["ips"] == "N":
        missing += 1

not_missing = (len(df) * len(df.columns)) - missing
print("Número de muestras: ", not_missing)

# Media y desviación estándar del total de fechas que se ha iniciado sesión
# Todos los usuarios tienen al menos una fecha

mediaFechas = df["fechas"].mean()
print("La media del total de fechas que han iniciado sesion: ", mediaFechas)
desviacionFechas = df["fechas"].std()
print("La desviación estandar del total de fechas que han iniciado sesion: ", desviacionFechas)

# Media y desviación estándar del total de IPs que se han detectado
# Hay un usuario que no tiene niguna dirección Ip - restar este usuario
''' Comparar estos resultados porque coge hasta las 4 IPs None '''

mediaIPs = df["ips"].mean()
print("La media del total de IPs: ", mediaIPs)
desviacionIPs = df["ips"].std()
print("La desviacion estandar del total de IPs: ", desviacionIPs)

# Media y desviación estándar del número de emails recibidos : columna emailsTotal
# Entendemos que los emails de Phishing y los emails Cliclados se encuentran contenidos en los emails totales
df["email_total"] = df["email_total"].astype(int)
mediaEmail = df["email_total"].mean()
print("La media del numero de email recibidos: ", mediaEmail)
desviacionEmail = df["email_total"].std()
print("La desviacion estandar del numero de email recibidos: ", desviacionEmail)

# Valor mínimo y máximo del total de fechas que se ha iniciado sesión
minFechas = df["fechas"].min()
print("El valor minimo de fechas que se ha iniciado sesion: ", minFechas)
maxFechas = df["fechas"].max()
print("El valor maximo de fechas que se ha iniciado sesion: ", maxFechas)

# Valor mínimo y máximo del número de emails recibidos
minEmails = df["email_total"].min()
print("El valor minimo de emails recibidos: ", minEmails)
maxEmails = df["email_total"].max()
print("El valor maximo de emails recibidos: ", maxEmails)

con.close()
