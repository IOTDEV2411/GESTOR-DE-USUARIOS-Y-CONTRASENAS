# Procedemos ahora a Implementar todas las funciones para nuestra tabla "Contrasena"
# Para crear las conexiones con nuestra base de datos sqlite, usaremos el concepto de "cursor"

# Del archivo "conexion", importamos todas las funciones creadas
from conexion import *

# Procedemos a la implementacion de la funcion que nos permite crear un nuevo
# registro en nuestra base de datos en sqlite
# Siempre, considerando el manejo de excepciones que pueden aparecer

def agregar(nombre,url,nombre_usuario,contrasena,descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO contrasena (Nombre,URL,Nombre_Usuario,Contrasena,Descripcion)
                            VALUES (?,?,?,?,?)'''
        datos = (nombre,url,nombre_usuario,contrasena,descripcion)
        cursor.execute(sentencia_sql,datos)
        conexion.commit()
        conexion.close()
        return 'Registro Correcto'
    except Error as err:
        print('Ha ocurrido un error '+str(err))

# Procedemos a implementar la funcion que nos permite visualizar 
# todo el contenido de nuestra tabla "contrasena" en nuestra base
# de datos sqlite.
# Siempre, considerando el manejo de excepciones que pueden aparecer

def mostrar():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM Contrasena'''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except Error as err:
        print('Ha ocurrido un error '+str(err))

# Procedemos a implementar la funcion que nos permite buscar y mostrar un elemento
# de nuestra tabla "Contrasena" segun el atributo id indicado
# Siempre, considerando el manejo de excepciones que pueden aparecer

def buscar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM Contrasena WHERE id=?'''
        cursor.execute(sentencia_sql,(id,))
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except Error as err:
        print('Ha ocurrido un error '+str(err))

# Procedemos a implementar la funcion que nos permite actualizar el contenido de nuestra
# tabla "contrasena" en nuestra base de datos sqlite.
# Siempre, considerando el manejo de excepciones que pueden aparecer

def modificar(id, Nombre, URL, Nombre_Usuario, Contrasena, Descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''UPDATE contrasena SET Nombre =?, URL =?, 
                            Nombre_Usuario=?, Contrasena=?, Descripcion=? WHERE id=?'''
        datos = (Nombre, URL, Nombre_Usuario, Contrasena, Descripcion,id)
        cursor.execute(sentencia_sql,datos)
        conexion.commit()
        conexion.close()
        return 'Se modifico la contrasena'
    except Error as err:
        print('Ha ocurrido un error '+str(err))

# Procedemos a implementar la funcion que nos permite eliminar un registro de
# la tabla "contrasena" en funcion del atributo "id" ingresado
# Siempre, considerando el manejo de excepciones que pueden aparecer

def eliminar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''DELETE FROM contrasena WHERE id=?'''
        cursor.execute(sentencia_sql,(id,))
        conexion.commit()
        conexion.close()
        return 'Se elimino la contrasena'
    except Error as err:
        print('Ha ocurrido un error '+str(err))
