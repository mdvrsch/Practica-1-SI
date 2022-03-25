import sqlite3
import pandas as pd


def dataframe():
    df = pd.read_sql_query("SELECT * FROM usuariosTable GROUP BY nombre", con)
    df["fechas"] = pd.read_sql_query("SELECT COUNT(fechas) FROM fechasTable GROUP BY nombre", con)
    df["ips"] = pd.read_sql_query("SELECT COUNT(ips) FROM ipsTable GROUP BY nombre", con)
    return df


con = sqlite3.connect('../database.db')

df = dataframe()
# print(df)

# EJERCICIO 3

# 1º agrupación: < 200 correos || >= 200 correos
df["email_total"] = df["email_total"].astype(int)
small = df[df["email_total"] < 200]
big = df[df["email_total"] >= 200]

# 2º agrupación : permisos = 0 (usuarios) || permisos = 1 (administradores)
small = small.groupby(df.permisos)
userSmall = small.get_group("0")
adminSmall = small.get_group("1")

big = big.groupby(df.permisos)
userBig = big.get_group("0")
adminBig = big.get_group("1")

print("Permisos = 0 && email < 200\n")
print(userSmall)

print("Permisos = 0 && email >= 200\n")
print(userBig)

print("Permisos = 1 && email < 200\n")
print(adminSmall)

print("Permisos = 1 && email >= 200\n")
print(adminBig)

# EMAIL PHISHING
# Número de observaciones


# Número de valores ausentes
missing = 0
for index, row in df.iterrows():
    if row["email_phishing"] == 0:
        missing += 1

print("Número de valores ausentes: ", missing)

# Mediana
mediana = df["email_phishing"].median()
print("La mediana de emails de phishing es: ", mediana)

# Media
media = df["email_phishing"].mean()
print("La media de emails de phishing es: ", media)

# Varianza
df["email_phishing"] = df["email_phishing"].astype(int)
varianza = df["email_phishing"].var()
print("La varianza de emails de phishing es: ", varianza)

# Valores máximo y mínimo
minPhishing = df["email_phishing"].min()
print("El valor minimo de emails de phishing es: ", minPhishing)

maxPhishing = df["email_phishing"].max()
print("El valor maximo de emails de phshing es: ", maxPhishing)

con.close()
