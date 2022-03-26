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


con = sqlite3.connect('../database.db')

df_users = dataframe_users()
df_legal = dataframe_legal()
df_contra = dataframe_contra()

# EJERCICIO 4

# Mostrar los 10 usuarios más críticos representadas en un gráfico de barras
# Usuario crítico -> contraseña débil + mayor probabilidad de pulsar un correo de spam
    # 1º unimos por nombre df_user + df_contra
df_contra["vulnerable"] = df_contra["vulnerable"].astype(int)
df_critico = df_contra.merge(df_users, on="nombre")
    # 2º seleccionamos solo los que tienen la contraseña vulnerable
df_contra_debil = df_critico[df_critico["vulnerable"] == 1]
    # 3º calculamos la probabilidad de entre los que son vulnerables
df_probabilidad = (df_contra_debil["email_cliclados"].astype(float) / df_contra_debil["email_phishing"].astype(float)) * 100
    # 4º ordenamos los valores de mayor a menor
df_probabilidad = df_probabilidad.sort_values(ascending=False)
    # 5º seleccionamos los 10 mayores
df_probabilidad = df_probabilidad.head(n=10)

df_probabilidad.plot(kind="bar", stacked=False, figsize=(10, 8))
plt.show()

# Mostrar las 5 páginas web que tienen más políticas (cookies, protección de datos o aviso legal) desactualizadas



# Mostrar las media de conexiones de usuario con contraseña vulnerable, frente a los que no son vulnerables
df_vulnerable = (df_contra["vulnerable"][df_contra["vulnerable"] == 1]).count()
media_vulnerable = (df_vulnerable / (df_contra["vulnerable"].count()))*100
print("La media de conexiones de usuario con contrasena vulnerable: ", media_vulnerable)
df_no_vulnerable = (df_contra["vulnerable"][df_contra["vulnerable"] == 0]).count()
media_no_vulnerable = (df_no_vulnerable / (df_contra["vulnerable"].count()))*100
print("La media de conexiones de usuario con contrasena no vulnerable: ", media_no_vulnerable)

# Mostrar según el año de creacción las webs que cumplen todas las políticas de privacidad, frente a las que no cumplen la política de privacidad
df_legal = df_legal.sort_values("creacion")
df_legal["cookies"] = df_legal["cookies"].astype(int)
df_legal["aviso"] = df_legal["aviso"].astype(int)
df_legal["proteccion"] = df_legal["proteccion"].astype(int)
df_legal = df_legal[df_legal["cookies"] == 1]
df_legal = df_legal[df_legal["aviso"] == 1]
df_politicas = df_legal[df_legal["proteccion"] == 1]
print(df_politicas)

df_no_politicas = df_legal.diff(periods=20)
print(df_no_politicas)


# Mostrar el número de contraseñas comprometidas y contraseñas no comprometidas
df_comprometida = (df_contra["vulnerable"][df_contra["vulnerable"] == 1]).count()
print("Numero de contraseñas comprometidas: ", df_comprometida)
df_no_comprometida = (df_contra["vulnerable"][df_contra["vulnerable"] == 0]).count()
print("Numero de contraseñas no comprometidas: ", df_no_comprometida)

con.close()
