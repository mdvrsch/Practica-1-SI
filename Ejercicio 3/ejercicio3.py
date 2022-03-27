import sqlite3
import pandas as pd


def dataframe_users():
    df = pd.read_sql_query(
        "SELECT permisos, email_total, email_phishing, email_cliclados FROM usuariosTable GROUP BY nombre",
        con)
    return df


con = sqlite3.connect('../database.db')
df = dataframe_users()

# EJERCICIO 3

# 1º agrupación: < 200 correos || >= 200 correos
df["email_phishing"] = df["email_phishing"].astype(int)
df_emails_menos = df[df["email_phishing"] < 200]
df_emails_mas = df[df["email_phishing"] >= 200]

# 2º agrupación : permisos = 0 (usuarios) || permisos = 1 (administradores)
df_emails_menos = df_emails_menos.groupby("permisos")
df_emails_mas = df_emails_mas.groupby("permisos")

print("Emails < 200:\n", df_emails_menos.sum())
print("Emails >= 200:\n", df_emails_mas.sum())

# EMAIL PHISHING
df["email_phishing"] = df["email_phishing"].astype(int)

# Número de observaciones = Número de emails totales de phishing que hemos recibido
observaciones_totales = df["email_phishing"].sum()
observaciones_menos = df_emails_menos.sum()
observaciones_mas = df_emails_mas.sum()
print("El número total de observaciones de emails de phishing: ", observaciones_totales)
print("El número total de observaciones de emails < 200 de phishing:\n", observaciones_menos)
print("El número total de observaciones de emails >= 200 de phishing:\n", observaciones_mas)

# Número de valores ausentes
missing = 0
for index, row in df.iterrows():
    if row["email_phishing"] == 0:
        missing += 1
print("Número de valores ausentes: ", missing)

# Mediana
mediana_menos = df_emails_menos.median()
mediana_mas = df_emails_mas.median()
print("La mediana de emails < 200 de phishing es:\n", mediana_menos)
print("La mediana de emails >= 200 de phishing es:\n", mediana_mas)

# Media
media_menos = df_emails_menos.mean()
media_mas = df_emails_mas.mean()
print("La media de emails < 200 de phishing es:\n", media_menos)
print("La media de emails >= 200 de phishing es:\n", media_mas)

# Varianza
varianza_menos = df_emails_menos.var()
varianza_mas = df_emails_mas.var()
print("La varianza de emails < 200 de phishing es:\n", varianza_menos)
print("La varianza de emails >= 200 de phishing es:\n", varianza_mas)

# Valores máximo y mínimo
min_phishing_menos = df_emails_menos.min()
min_phishing_mas = df_emails_mas.min()
print("El valor minimo de emails < 200 de phishing es:\n", min_phishing_menos)
print("El valor minimo de emails >= 200 de phishing es:\n", min_phishing_mas)

max_phishing_menos = df_emails_menos.max()
max_phishing_mas = df_emails_mas.max()
print("El valor maximo de emails < 200 de phishing es:\n", max_phishing_menos)
print("El valor maximo de emails >= 200 de phishing es:\n", max_phishing_mas)

con.close()
