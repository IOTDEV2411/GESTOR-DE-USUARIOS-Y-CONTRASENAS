# Procedemos ahora a Implementar todas las funciones para nuestra tabla "usuario"
# Para crear las conexiones con nuestra base de datos sqlite, usaremos el concepto de "cursor"

# Para encriptar la contraseña maestra de la aplicacion, importamos el modulo "hashlib"
import hashlib
# Del archivo "conexion", importamos todas las funciones creadas
from conexion import *

# En esta funcion, se mostraran todos los usuarios 
# registrados en nuestra tabla "usuario"
# Siempre, con el manejo de excepciones respectivos

def comprobar_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    sentencia_sql = '''SELECT * FROM usuario '''
    cursor.execute(sentencia_sql)
    usuario_encontrado = cursor.fetchall()
    conexion.close()
    return usuario_encontrado

# En esta funcion, ingresaremos un nuevo registro para nuestra tabla "usuario"
# Tener en cuenta que, para el caso de nuestra contrasena, esta estara encriptada
# mediante un codigo HASH SHA256, esto para mayor seguridad.
# Siempre, con el manejo de excepciones respectivos

def registrar(Nombre,Apellido,Contrasena_Maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO usuario (Nombre,Apellido,Contrasena_Maestra)
                            values (?,?,?)'''
        cm_cifrada = hashlib.sha256(Contrasena_Maestra.encode('utf-8')).hexdigest()
        datos = (Nombre,Apellido,cm_cifrada)
        cursor.execute(sentencia_sql,datos)
        conexion.commit()
        conexion.close()
        return 'Registro Correcto'
    except Error as err:
        return 'Ha ocurrido un error' + str(err)

# En esta funcion, comprobamos si la contrasena registrada corresponde
# a la contrasena ingresada en funcion del id ingresado
# Tener en cuenta que, para ingresar 02 valores en el metodo ".execute()"
# debemos de ingresarlos usando la estructura de datos "tupla"
# Siempre, con el manejo de excepciones respectivos

def comprobar_contrasena(id,Contrasena_Maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM usuario WHERE id=? AND Contrasena_Maestra=?'''
        cm_cifrada = hashlib.sha256(Contrasena_Maestra.encode('utf-8')).hexdigest()
        cursor.execute(sentencia_sql,(id,cm_cifrada))
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except Error as err:
        return 'Ha ocurrido un error' + str(err)

