import sqlite3
from sqlite3 import Error

# En esta funcion, creamos la conexion con nuestra base de datos sqlite3
# Siempre, considerando el manejo de excepciones que pueden aparecer

def conectar():
    try:
        conexion = sqlite3.connect('Database.db')
        return conexion
    except Error as err:
        print('No se pudo realizar la conexion a la base de datos')

# En esta funcion, crearemos las 02 tablas para nuestro proyecto:
#
# La primera tabla con el nombre "usuario"
# La segunda tabla con el nombre "contrasena"
#
# Para ambas tablas, indicamos su llave primaria
# asi como las columnas correspondientes.

def crear_tablas(conexion):
    cursor = conexion.cursor()
    sentencia_sql_01 = ''' CREATE TABLE IF NOT EXISTS usuario (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Nombre TEXT NOT NULL,
                            Apellido TEXT NOT NULL,
                            Contrasena_Maestra TEXT NOT NULL
                            )'''
    sentencia_sql_02 = ''' CREATE TABLE IF NOT EXISTS contrasena (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Nombre TEXT NOT NULL,
                            URL TEXT NOT NULL,
                            Nombre_Usuario TEXT NOT NULL,
                            Contrasena TEXT NOT NULL,
                            Descripcion TEXT
                            )'''
    cursor.execute(sentencia_sql_01)
    cursor.execute(sentencia_sql_02)
    conexion.commit()