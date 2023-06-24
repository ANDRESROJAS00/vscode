"""
Opcion 1:
Grabar: Corresponde a guardar ciertos datos de un vehiculo, entre ellos: 
Tipo, patente, marca y precio, multas: monto y fecha, fecha de registro del vehiculo y nombre del dueno.

Ademas, debe verificar que la patente sea correcta, la marca considere entre 2 y 15 caracteres y el precio sea mayor a 5.000.000

Opcion2:
Buscar: Corresponde buscar un auto por su patente y mostrar toda su informacion almacenada.

Opcion3:
Imprimir certificado: Esta opcion permite imprimir los certificados de Emision de contaminantes, de anotaciones vigentes y de multas. Estos deben ser previamente ingresados con valores
aleatorios entre $1.500 y $3.500. Al imprimir el certificado, debe mostrar el nombre del certifcado, la patente del auto y los datos del dueno actual.

Opcion 4
Salir: Corresponde a salir del programa emitiendo un mensaje de salida. Considere, ademas, su nombre y apellido y la version del programa.

"""

import random

import re


lista_vehiculos = []


def grabar_auto():

    patron_patente = r'^[A-Z]{4}-\d{2}$'
    monto_minimo = 1500
    monto_maximo = 3500
    
    tipo = input('Ingrese el tipo de vehiculo: ')
    patente = input('Ingrese la patente en formato AAAA-11: ')
    while not re.match(patron_patente, patente):
        print('La patente ingresada no es válida. Debe tener el formato AAA-111.')
        patente = input('Ingrese la patente del vehículo (AAA-111): ')
    marca = input('Ingrese la marca: ')
    while len(marca) < 2 or len(marca) > 15:
        print('debe ser mayor a 2 letras y menor a 15')
        marca = input('Ingrese la marca: ')
        return
    precio = int(input('Precio del vehiculo: '))
    while precio <= 5000000:
        print('El precio debe ser mayor a $5.000.000')
        precio = int(input('Precio del vehiculo: '))
    fecha_registro_vehiculo = input('Fecha de registro del vehiculo: ')
    nombre_dueno = input('Ingrese el nombre del dueno: ')

    multa = []
    cant_multas = int(input('Ingres la cantidad de multas: '))
    for _ in range(cant_multas):
        monto_multa = random.randint(monto_minimo, monto_maximo)
        fecha_multa = input('Ingrese la fecha de la multa: ')
        multas = {
            'monto multa' : monto_multa,
            'fecha multa' : fecha_multa
        }
        multa.append(multas)

    diccionario_vehiculo = {
        'tipo' : tipo,
        'patente' : patente,
        'marca' : marca,
        'precio' : precio,
        'fecha de registro' : fecha_registro_vehiculo,
        'nombre de dueno' : nombre_dueno,
        'multas' : multa
    }
    lista_vehiculos.append(diccionario_vehiculo)



def buscar_info():
    patente = input('Ingresar patente:')

    for vehiculo in lista_vehiculos:
        if vehiculo['patente'] == patente:
            print('\n---Datos del vehiculo---')
            print('Tipo:',vehiculo['tipo'])
            print('Patente:', vehiculo['patente'])
            print('Marca:',vehiculo['marca'])
            print('Precio:',vehiculo['precio'])
            print('Fecha de registro:', vehiculo['fecha de registro'])
            print('Nombre del dueño:','',vehiculo['nombre de dueno'],'\n')
            print('---Multas---')
            for multa in vehiculo['multas']:
                print('Monto de la multa:',multa['monto multa'])
                print('Fecha de la multa:', multa['fecha multa'])
                return

    else:
        print('error')


def imprimir_certificado(tipo_certificado):

    monto_minimo = 1500
    monto_maximo = 3500

    print('Certificado:', tipo_certificado)

    for certificado in lista_vehiculos:
        monto_certificado = random.randint(monto_minimo, monto_maximo)

        print('Nombre del dueno:', certificado['nombre de dueno'])
        print('Patente del vehiculo:', certificado['patente'])
        print('Monto de deuda:', monto_certificado) 


def menu():

        while True:

            print('---Menu de la automotora---')
            print('1. Guardar informacion')
            print('2. Buscar informacion')
            print('3. Imprimir Certificado')
            print('4. Salir')


            opcion = int(input('Ingrese la opcion: '))

            if opcion == 1:
                grabar_auto()
            elif opcion == 2:
                buscar_info()
            elif opcion == 3:
                print('---Tipo de certificado---')
                print('1. Emision de contaminantes')
                print('2. Anotaciones vigentes')
                print('3. Multa')
                print('4. Salir')

                tipo_certificado = int(input('Ingrese la opcion de la multa: '))

                if tipo_certificado == 1:
                    imprimir_certificado('Emision de contaminantes')
                elif tipo_certificado == 2:
                    imprimir_certificado('Anotaciones vigentes')
                elif tipo_certificado == 3:
                    imprimir_certificado('Multa')
                else:
                    print('Valor no valido asegurese que sea ua opcion del menu.')

            elif opcion == 4:
                print('Saliendo del programa...')
                break
                
            else:
                print('Opcion invalida.')

menu()