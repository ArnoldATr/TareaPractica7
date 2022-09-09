'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 08 de septiembre del 2022
Autor: Arnold Avalos Torres
Tarea: Autenticar Usuario con bcrypt
'''

import bcrypt

def leer_usuarios():
    archivo = open("usuarios.txt", "r")

    cadena = archivo.read()
    listUs = cadena.split("\n")

    archivo.close()
    list = set()
    for usu in listUs:
        reg = usu.split(" ")
        tupla = (reg[0], reg[1], reg[2])
        list.add(tupla)
    return list

def estudiantes():
    archivo = open("Estudiantes.prn", "r")

    cadena = archivo.read()
    listaEst = cadena.split("\n")

    archivo.close()
    list = set()
    for est in listaEst:
        tupla = (est[:8], est[8:])
        list.add(tupla)
    return list

def autenticar_usuario(usuario, password):
    usuapasw = leer_usuarios() # Metodo encargado de leer y extraer la info del archivo usuarios.txt
    estudiante = estudiantes() # Metodo encargado de leer y verificar la info del archivo Estudiantes.prn
    aut = {}
    for reg in usuapasw:
        if reg[0] == usuario:
            for est in estudiante:
                if est[0] == usuario:
                    bandera = bcrypt.checkpw(password.encode('utf-8'), reg[2].encode('utf-8'))
                    aut["Bandera"] = bandera
                    aut["Usuario"] = est[1]
                    if bandera:
                        aut["Mensaje"] = "Bienvenido al Sistema de Autenticación de usuarios"
                    else:
                        aut["Mensaje"] = "Contraseña incorrecta"
                    return aut
    aut["Bandera"] = False
    aut["Usuario"] = ""
    aut["Mensaje"] = "No existe el Usuario"
    return aut

print(autenticar_usuario("18420428","Fn?@21M$2U"))