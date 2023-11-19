import os

def Create_file():
    Nombre_Archivo = input("Ingrese El Nombre Del Archivo Que Deseas Crear: ")
    with open(Nombre_Archivo, 'w') as Archivo:
        print("El Archivo Fue Creado De Manera Exitoza.")

def Read_file():
    Nombre_Archivo = input("Introduzca El Nombre Del Archivo Que Desea Leer: ")
    with open(Nombre_Archivo, 'r') as Archivo:
        Contenido = Archivo.read()
        print("El Contenido Del Archivo Es:")
        print(Contenido)

def Add_data():
    Nombre_Archivo = input("Introduce El Nombre Del Archivo Que Desea Modificar: ")
    Elemento = input("Introduce El Elemento Que Desea Agregar: ")
    with open(Nombre_Archivo, 'a') as Archivo:
        Archivo.write(Elemento + "\n")
        print("El Elemento Fue Agregado Exitosamente.")

def Modify_data():
    Nombre_Archivo = input("Introduce El Nombre Del Archivo Que Deseas Modificar: ")
    with open(Nombre_Archivo, 'r') as Archivo:
        Lineas = Archivo.readlines()

    print("El Contenido Del Archivo Es : ")
    for i, Linea in enumerate(Lineas):
        print(f"{i}: {Linea}", end='')

    Numero_Linea = int(input("Introduce El Número De Línea Que Desea Modificar: "))
    Nueva_Linea = input("Introduce La Nueva Línea: ")
    Lineas[Numero_Linea] = Nueva_Linea + "\n"

    with open(Nombre_Archivo, 'w') as Archivo:
        Archivo.writelines(Lineas)
        print("Las Líneas Fueron Modificadas Exitosamente.")

def Delete_data():
    Nombre_Archivo = input("Introduce El Nombre Del Archivo Que Deseas Eliminar: ")
    os.remove(Nombre_Archivo)
    print("El Archivo Fue eliminado exitosamente.")

while True:
    Menu = ('''  
            Menu 
        1. Crear Un archivo.
        2. Leer Un Archivo 
        3. Agregar Elementos A Un Archivo 
        4. Modificar Un Archivo 
        5. Eliminar El Archivo 
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
