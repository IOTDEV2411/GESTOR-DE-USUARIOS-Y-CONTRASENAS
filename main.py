# Importamos el modulo "os" para tener acceso a algunas funciones del sistema operativo
import os
# Importamos el modulo "getpass" del archivo "getpass" para que la contraseña ingresada pueda ser leida pero no visible
from getpass import getpass
# Importamos el modulo "tabulate" del archivo "tabulate" para una mejor visualizacion de las tablas creadas
# Debido a que este modulo no se encuentra instalado por defecto en python, procedemos a abrir el terminal
# y ejecutamos la instruccion "pip install tabulate" para instalar el modulo requerido
from tabulate import tabulate
# Del modulo "conexion", importamos todas las funciones creadas
from conexion import *
# Del modulo "usuario", importamos todas las funciones creadas
from usuario import *
# Del modulo "contrasena", importamos todas las funciones creadas
from contrasena import *

conexion = conectar()
crear_tablas(conexion)

def inicio():
    # Primero, procedemos a limpiar la consola con el comando "cls"
    os.system('cls')
    # Seguidamente, comprobamos si se ha creado algun usuario en la Base de Datos
    comprobar = comprobar_usuario()
    # Si no se ha creado ningun usuario, procedemos a ingresar nuestros datos
    if len(comprobar) == 0:
        print('Bienvenido, registre su informacion: ')
        Nombre = input('Ingrese su Nombre: ')
        Apellido = input('Ingrese su Apellido: ')
        # Para que no se visualice la contraseña ingresada en la terminal, usamos la funcion "getpass"
        Contrasena_Maestra = getpass('Ingrese su Contrasena Maestra: ')
        # Usamos la funcion "registrar" para pasar los datos ingresados por consola a la Base de Datos
        respuesta = registrar(Nombre,Apellido,Contrasena_Maestra)
        # Evaluamos la respuesta que nos devuelve la funcion "registrar"
        # Si se ha ejecutado correctamente la funcion "Registrar", mostrar un mensaje de bienvenida y ejecutar la funcion "menu"
        if respuesta == 'Registro Correcto':
            print(f'Bienvenido {Nombre}')
            menu()
        # Caso contrario, mostrar el codigo de error que se genero
        else:
            print(respuesta)
    # Si ya existe un usuario en la base de datos, se debe pedir la contraseña para acceder
    else:
        Contrasena_Maestra = getpass('Ingrese su Contrasena Maestra: ')
        # Usamos la funcion "comprobar_contrasena" para verificar si la contrasena ingresada coincide con la almacenada
        respuesta = comprobar_contrasena(1,Contrasena_Maestra)
        # Si la contraseña ingresada no coincide con la almacenada, mostrar 'Contraseña Incorrecta'
        if len(respuesta) == 0:
            print('Contraseña Incorrecta')
        # Caso contrario, mostrar mensaje de bienvenida y ejecutar la funcion "menu"
        else:
            print('Bienvenido')
            menu()

def menu():
    while True:
        print('Seleccione una de las siguientes opciones:')
        print('\t1 - Añadir Contraseña: ')
        print('\t2 - Ver todas las contraseñas: ')
        print('\t3 - Visualizar una contraseña: ')
        print('\t4 - Modificar contraseña: ')
        print('\t5 - Eliminar contraseña: ')
        print('\t6 - Salir')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            nueva_contrasena()
        elif opcion == '2':
            mostrar_contrasenas()
        elif opcion == '3':
            buscar_contrasena()
        elif opcion == '4':
            modificar_contrasena()
        elif opcion == '5':
            eliminar_contrasena()
        elif opcion == '6':
            break
        else:
            print('No ingreso una opcion Valida...')

def nueva_contrasena():
    Nombre = input('Ingrese Nombre: ')
    URL = input('Ingrese URL: ')
    Nombre_usuario = input('Ingrese el Nombre del Usuario: ')
    Contrasena = getpass('Ingrese la Contrasena: ')
    Descripcion = input('Ingrese una descripcion: ')
    respuesta = agregar(Nombre,URL,Nombre_usuario,Contrasena,Descripcion)
    print(respuesta)

def mostrar_contrasenas():
    datos = mostrar()
    header = ['ID','NOMBRE','URL','USUARIO','CONTRASEÑA','DESCRIPCION']
    tabla = tabulate(datos,header,tablefmt='fancy_grid')
    print('\t\t\t\tTodas las Contraseñas')
    print(tabla)

def buscar_contrasena():
    contrasena_maestra = getpass('Ingrese su Contrasena Maestra: ')
    respuesta = comprobar_contrasena(1,contrasena_maestra)
    if len(respuesta)==0:
        print('Contrasena Incorrecta')
    else:
        id = input('Ingrese el id de la contraseña a buscar: ')
        datos = buscar(id)
        header = ['ID','NOMBRE','URL','USUARIO','CONTRASEÑA','DESCRIPCION']
        tabla = tabulate(datos,header,tablefmt='fancy_grid')
        print('\t\tLa contraseña del usuario con id = ' + str(id))
        print(tabla)

def modificar_contrasena():
    contrasena_maestra = getpass('Ingrese su Contrasena Maestra: ')
    respuesta = comprobar_contrasena(1,contrasena_maestra)
    if len(respuesta)==0:
        print('Contrasena Incorrecta')
    else:
        id = input('Ingrese el id de la contraseña a modificar: ')
        Nombre = input('Ingrese el Nuevo Nombre: ')
        URL = input('Ingrese la Nueva URL: ')
        Nombre_usuario = input('Ingrese el Nuevo Nombre del Usuario: ')
        Contrasena = getpass('Ingrese la Nueva Contrasena: ')
        Descripcion = input('Ingrese una descripcion: ')
        respuesta = modificar(id, Nombre, URL, Nombre_usuario, Contrasena, Descripcion)
        print(respuesta)

def eliminar_contrasena():
    contrasena_maestra = getpass('Ingrese su Contrasena Maestra: ')
    respuesta = comprobar_contrasena(1,contrasena_maestra)
    if len(respuesta)==0:
        print('Contrasena Incorrecta')
    else:
        id = input('Ingrese el id de la contraseña a eliminar: ')
        respuesta = eliminar(id)
        print(respuesta)

# Para inicializar todo el programa, ejecutamos la funcion "inicio"    
inicio()