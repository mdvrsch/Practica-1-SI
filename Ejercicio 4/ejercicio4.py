import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def dataframe_users():
    df_users = pd.read_sql_query("SELECT * FROM usuariosTable GROUP BY nombre", con)
    df_users["fechas"] = pd.read_sql_query("SELECT COUNT(fechas) FROM fechasTable GROUP BY nombre", con)
    df_users["ips"] = pd.read_sql_query("SELECT COUNT(ips) FROM ipsTable GROUP BY nombre", con)
    return df_users

def dataframe_legal():
    df_legal = pd.read_sql_query("SELECT * FROM legalTable GROUP BY nombre", con)
    return df_legal


con = sqlite3.connect('../database.db')

df_users = dataframe_users()
df_legal = dataframe_legal()
# print(df_users)
# print(df_legal)

# EJERCICIO 4

# Mostrar los 10 usuarios más críticos representadas en un gráfico de barras
df_mayor = df_users.sort_values(by='email_cliclados', ascending=False)
print(df_mayor)

df_mayor.plot(kind="bar", stacked=False, figsize=(10, 8))
plt.show()

con.close()
