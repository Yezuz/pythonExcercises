import sqlite3

conexion = sqlite3.connect('novelas.db')

def crearTabla():
    
    consulta = conexion.cursor()
    tabla = "CREATE TABLE tabla (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"\
    "nombre VARCHAR (30) NOT NULL,"\
    "autor VARCHAR(40) NOT NULL,"\
    "year INTEGER(9) NOT NULL);"

    print(tabla)

    if(consulta.execute(tabla)): print("La tabla fue creada")
    else: print("La tabla NO fue creada")

    consulta.close()
    conexion.commit()
    conexion.close()

def insertarRegistros():
    print("Ingresa los datos de la novela")
    nombre1 = input("Titulo: ")
    autor1 = input("Autor: ")
    year1 = input("Anio: ")

    consulta = conexion.cursor()

    strConsulta = "INSERT INTO tabla(nombre, autor, year) VALUES ('" + nombre1 + "','" + autor1 + "','" + year1 + "')"
    print(strConsulta)
    consulta.execute(strConsulta)
    consulta.close()
    conexion.commit()
    conexion.close()

def consultarRegistros():
    print("Estas en la funcion consulta")
    consulta = conexion.cursor()
    Strconsulta = "SELECT * FROM tabla"
    consulta.execute(strConsulta)
    registros = consulta.fetchall()
    lista = []

    for registro in registros:
        s = [] 
        s['nombre'] = registro[1]
        s['autor'] = registro[2]
        s['year'] = str(registro[3])
        lista.append(s)

    consulta.close()
    conexion.close()
    return lista    
        
        
