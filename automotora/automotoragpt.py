import random
import re

archivador_de_datos = []

def grabar_datos():
    patron_patente = r'^[A-Z]{3}-\d{3}$'
    monto_minimo_multa = 1500
    monto_maximo_multa = 3500

    nombre_dueno = input('Ingrese el nombre del dueño: ')
    tipo_vehiculo = input('Ingrese el tipo de vehículo: ')
    patente = input('Ingrese la patente del vehículo (AAA-111): ')
    while not re.match(patron_patente, patente):
        print('La patente ingresada no es válida. Debe tener el formato AAA-111.')
        patente = input('Ingrese la patente del vehículo (AAA-111): ')

    marca = input('Ingrese la marca del vehículo (2 a 15 caracteres): ')
    while len(marca) < 2 or len(marca) > 15:
        print('La marca debe tener entre 2 y 15 caracteres.')
        marca = input('Ingrese la marca del vehículo (2 a 15 caracteres): ')

    precio = int(input('Ingrese el precio del vehículo (mayor a 5.000.000): '))
    while precio <= 5000000:
        print('El precio debe ser mayor a 5.000.000.')
        precio = int(input('Ingrese el precio del vehículo (mayor a 5.000.000): '))

    fecha_registro = input('Ingrese la fecha de registro del vehículo: ')

    multas = []
    cantidad_multas = int(input('Ingrese la cantidad de multas del vehículo: '))
    for _ in range(cantidad_multas):
        monto_multa = random.randint(monto_minimo_multa, monto_maximo_multa)
        fecha_multa = input('Ingrese la fecha de la multa: ')
        multa = {
            'monto': monto_multa,
            'fecha': fecha_multa
        }
        multas.append(multa)

    vehiculo = {
        'nombre_dueno': nombre_dueno,
        'tipo_vehiculo': tipo_vehiculo,
        'patente': patente,
        'marca': marca,
        'precio': precio,
        'fecha_registro': fecha_registro,
        'multas': multas
    }
    archivador_de_datos.append(vehiculo)

    print('Datos del vehículo guardados con éxito.')


def buscar_datos():
    patente_buscar = input('Ingrese la patente del vehículo a buscar: ')
    encontrado = False

    for vehiculo in archivador_de_datos:
        if vehiculo['patente'] == patente_buscar:
            print('Vehículo encontrado:')
            print('Nombre del dueño:', vehiculo['nombre_dueno'])
            print('Tipo de vehículo:', vehiculo['tipo_vehiculo'])
            print('Patente:', vehiculo['patente'])
            print('Marca:', vehiculo['marca'])
            print('Precio:', vehiculo['precio'])
            print('Fecha de registro:', vehiculo['fecha_registro'])
            print('Multas:')
            for multa in vehiculo['multas']:
                print('- Monto:', multa['monto'])
                print('  Fecha:', multa['fecha'])
            encontrado = True
            break

    if not encontrado:
        print('No se encontró ningún vehículo con la patente ingresada.')


def imprimir_certificado(tipo_certificado):
    monto_minimo_certificado = 1500
    monto_maximo_certificado = 3500

    print('Certificado:', tipo_certificado)

    for vehiculo in archivador_de_datos:
        nombre_dueno = vehiculo['nombre_dueno']
        patente = vehiculo['patente']
        monto_certificado = random.randint(monto_minimo_certificado, monto_maximo_certificado)

        print('Nombre del dueño:', nombre_dueno)
        print('Patente del vehículo:', patente)
        print('Monto del certificado:', monto_certificado)

        # Imprimir otros datos específicos del certificado si es necesario

        print('--------------------')


def main():
    print('Bienvenido al programa de registro de vehículos.')
    nombre_apellido = 'Nombre y Apellido'  # Reemplaza con tu nombre y apellido
    version_programa = '1.0'  # Reemplaza con la versión actual del programa

    while True:
        print('----- Menú -----')
        print('1. Grabar')
        print('2. Buscar')
        print('3. Imprimir certificado')
        print('4. Salir')

        opcion = input('Ingrese el número de la opción deseada: ')

        if opcion == '1':
            grabar_datos()
        elif opcion == '2':
            buscar_datos()
        elif opcion == '3':
            print('Tipos de certificado:')
            print('1. Emisión de contaminantes')
            print('2. Anotaciones vigentes')
            print('3. Multas')
            tipo_certificado = input('Ingrese el número del tipo de certificado: ')

            if tipo_certificado == '1':
                imprimir_certificado('Emisión de contaminantes')
            elif tipo_certificado == '2':
                imprimir_certificado('Anotaciones vigentes')
            elif tipo_certificado == '3':
                imprimir_certificado('Multas')
            else:
                print('Opción inválida.')
        elif opcion == '4':
            print('Gracias por utilizar el programa.')
            print('Desarrollado por', nombre_apellido)
            print('Versión:', version_programa)
            break
        else:
            print('Opción inválida. Por favor, ingrese un número válido.')


# Ejecutar el programa principal
main()
