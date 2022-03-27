import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def dataframe_users():
    df_users = pd.read_sql_query("SELECT nombre, email_phishing, email_cliclados FROM usuariosTable GROUP BY nombre",con)
    return df_users

def dataframe_legal():
    df_legal = pd.read_sql_query("SELECT * FROM legalTable GROUP BY nombre", con)
    return df_legal

def dataframe_contra():
    df_contra = pd.read_sql_query("SELECT * FROM contrasenaTable GROUP BY nombre", con)
    return df_contra

def dataframe_desactualizadas():
    df_desactualizadas = pd.read_sql_query("SELECT nombre, cookies, aviso, proteccion FROM legalTable GROUP BY nombre", con)
    return df_desactualizadas


con = sqlite3.connect('../database.db')

df_users = dataframe_users()
df_legal = dataframe_legal()
df_contra = dataframe_contra()
df_desactualizadas = dataframe_desactualizadas()

# EJERCICIO 4

# Mostrar los 10 usuarios más críticos representadas en un gráfico de barras
# Usuario crítico -> contraseña débil + mayor probabilidad de pulsar un correo de spam
    # 1º unimos por nombre df_user + df_contra
df_contra["vulnerable"] = df_contra["vulnerable"].astype(int)
df_critico = df_contra.merge(df_users, on="nombre")
    # 2º seleccionamos solo los que tienen la contraseña vulnerable
df_contra_debil = df_critico[df_critico["vulnerable"] == 1]
    # 3º calculamos la probabilidad de entre los que son vulnerables
df_contra_debil["probabilidad"] = (df_contra_debil["email_cliclados"].astype(float) / df_contra_debil["email_phishing"].astype(float)) * 100
    # 4º ordenamos los valores de mayor a menor
df_contra_debil= df_contra_debil.sort_values("probabilidad", ascending=False)
    # 5º seleccionamos los 10 mayores
df_contra_debil= df_contra_debil.head(n=10)
df_contra_debil = df_contra_debil.drop(["vulnerable"], axis=1)

df_contra_debil.plot(x="nombre", kind="bar", stacked=False, figsize=(10, 8))
plt.show()

# Mostrar las 5 páginas web que tienen más políticas (cookies, protección de datos o aviso legal) desactualizadas
# Desactualizadas = más políticas a 0
df_desactualizadas["cookies"] = df_desactualizadas["cookies"].astype(int)
df_desactualizadas["aviso"] = df_desactualizadas["aviso"].astype(int)
df_desactualizadas["proteccion"] = df_desactualizadas["proteccion"].astype(int)
df_desactualizadas["desactualizadas"] = 3-(df_desactualizadas[["cookies", "aviso", "proteccion"]].sum(axis=1))
df_desactualizadas = df_desactualizadas.sort_values("desactualizadas", ascending=False)
df_desactualizadas = df_desactualizadas.head(n=5)
df_desactualizadas = df_desactualizadas.drop(["desactualizadas"], axis=1)

df_desactualizadas.plot(x="nombre", kind="bar", stacked=False, figsize=(10, 8))
plt.show()


# Mostrar las media de conexiones de usuario con contraseña vulnerable, frente a los que no son vulnerables
df_vulnerable = (df_contra["vulnerable"][df_contra["vulnerable"] == 1]).count()
media_vulnerable = (df_vulnerable / (df_contra["vulnerable"].count())) * 100
df_no_vulnerable = (df_contra["vulnerable"][df_contra["vulnerable"] == 0]).count()
media_no_vulnerable = (df_no_vulnerable / (df_contra["vulnerable"].count())) * 100

leyenda = ["Conexiones vulnerables", "Conexiones no vulnerables"]
valores = [media_vulnerable, media_no_vulnerable]
plt.pie(valores, labels=leyenda, autopct="%0.1f %%")
plt.show()

# Mostrar según el año de creacción las webs que cumplen todas las políticas de privacidad, frente a las que no cumplen la política de privacidad
'''FALTA POR TERMINAR'''
df_legal["cookies"] = df_legal["cookies"].astype(int)
df_legal["aviso"] = df_legal["aviso"].astype(int)
df_legal["proteccion"] = df_legal["proteccion"].astype(int)
df_creacion = df_legal.sort_values("creacion")
df_creacion = df_creacion[df_creacion["cookies"] == 1]
df_creacion = df_creacion[df_creacion["aviso"] == 1]
df_politicas_cumplen = df_creacion[df_creacion["proteccion"] == 1]
df_politicas_cumplen.plot(x="creacion", kind="bar", stacked=False, figsize=(10, 8))
plt.show()

# df_politicas_no_cumplen = len(df_legal)




# Mostrar el número de contraseñas comprometidas y contraseñas no comprometidas
df_comprometida = (df_contra["vulnerable"][df_contra["vulnerable"] == 1]).count()
df_no_comprometida = (df_contra["vulnerable"][df_contra["vulnerable"] == 0]).count()

plt.bar(["Contraseñas comprometidas", "Contraseñas no comprometidas"], [df_comprometida, df_no_comprometida])
plt.show()

con.close()

