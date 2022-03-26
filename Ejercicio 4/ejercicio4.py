import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def dataframe_users():
    df_users = pd.read_sql_query("SELECT nombre, email_phishing, email_cliclados FROM usuariosTable GROUP BY nombre",
                                 con)
    return df_users


def dataframe_legal():
    df_legal = pd.read_sql_query("SELECT * FROM legalTable GROUP BY nombre", con)
    return df_legal


def dataframe_contra():
    df_contra = pd.read_sql_query("SELECT * FROM contrasenaTable GROUP BY nombre", con)
    return df_contra


con = sqlite3.connect('../database.db')

df_users = dataframe_users()
df_legal = dataframe_legal()
df_contra = dataframe_contra()
# print(df_users)
# print(df_legal)
# print(df_contra)

# EJERCICIO 4

# Mostrar los 10 usuarios más críticos representadas en un gráfico de barras
df_criticos = df_contra.groupby("vulnerable").count()
df_criticos = df_criticos.get_group("1")
print(df_criticos)
#df_criticos.plot(ind="bar", stacked=False, figsize=(10, 8))
#plt.show()

df_probabilidad = (df_users["email_cliclados"].astype(int) / df_users["email_phishing"].astype(int)) * 100

# df_probabilidad.plot(kind="bar", stacked=False, figsize=(10, 8))
# plt.show()

con.close()
