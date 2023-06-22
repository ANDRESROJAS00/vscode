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

monto_minimo = 1500
monto_maximo = 3500


def grabar_auto():
    
    tipo = input('Ingrese el tipo de auto: ')
    patente = input('Ingrese la patente en formato AAA-111: ')






