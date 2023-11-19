import os

def Create_file():
    Nombre_Fichero = input("Ingrese El Nombre Del Fichero Que Deseas Crear: ")
    with open(Nombre_Fichero, 'w') as Fichero:
        print("El Fichero Fue Creado De Manera Exitoza.")

def Read_file():
    Nombre_Fichero = input("Introduzca El Nombre Del Fichero Que Desea Leer: ")
    with open(Nombre_Fichero, 'r') as Fichero:
        Contenido = Fichero.read()
        print("El Contenido Del Fichero Es:")
        print(Contenido)

def Add_data():
    Nombre_Fichero = input("Introduce El Nombre Del Fichero Que Desea Modificar: ")
    Elemento = input("Introduce El Elemento Que Desea Agregar: ")
    with open(Nombre_Fichero, 'a') as Fichero:
        Archivo.write(Elemento + "\n")
        print("El Elemento Fue Agregado Exitosamente.")

def Modify_data():
    Nombre_Fichero = input("Introduce El Nombre Del Fichero Que Deseas Modificar: ")
    with open(Nombre_Fichero, 'r') as Fichero:
        Lineas = Fichero.readlines()

    print("El Contenido Del Fichero Es : ")
    for i, Linea in enumerate(Lineas):
        print(f"{i}: {Linea}", end='')

    Numero_Linea = int(input("Introduce El Número De Línea Que Desea Modificar: "))
    Nueva_Linea = input("Introduce La Nueva Línea: ")
    Lineas[Numero_Linea] = Nueva_Linea + "\n"

    with open(Nombre_Fichero, 'w') as Fichero:
        Fichero.writelines(Lineas)
        print("Las Líneas Fueron Modificadas Exitosamente.")

def Delete_data():
    Nombre_Fichero = input("Introduce El Nombre Del Fichero Que Deseas Eliminar: ")
    os.remove(Nombre_Fichero)
    print("El Fichero Fue eliminado exitosamente.")

while True:
    Menu = ('''  
            Menu 
        1. Crear Un Fichero.
        2. Leer Un Fichero 
        3. Agregar Elementos A Un Fichero 
        4. Modificar Un Fichero 
        5. Eliminar El Fichero 
        6. Salir 
        Selecciona Una Opcion Entre : ''')
    
    opcion = input(Menu)

    match opcion: 
        case '1':
            Create_file ()
        case '2':
            Read_file()
        case '3':
            Add_data()
        case '4':
            Modify_data()
        case '5':
            Delete_data()
        case '6':
            print("Saliendo...")
            break
        case _:
            print("Opción Inválida, Por Favor Inténtalo De Nuevo.")
