def calcular_iva(precio_objeto):
    iva = precio_objeto * 0.19
    print(f'El valor del IVA del producto es: {iva}')
    return iva

def descuento(precio_producto, descuento_aplicar):
    des = precio_producto * (descuento_aplicar/100)
    total_descuento = precio_producto - des
    print('El total de su descuento es: ', total_descuento)
    return total_descuento

def calcular_imc(peso, estatura):   
    imc = peso / (estatura ** 2)
    print('Su IMC es: ', imc)
    return imc

while True:

    print('(1)Calcular IVA')
    print('(2)Descuento')
    print('(3)Calcular IMC')
    print('(4)Salir')


    menu = int(input('Elija las opciones del menu: '))

    if menu == 1:
        precio_objeto = int(input('Ingrese el valor para calcular el IVA: '))
        calcular_iva(precio_objeto)

    elif menu == 2:
        precio_producto = int(input('Ingrese el precio del producto para el descuento: '))
        descuento_aplicar = int(input('Ingrese el descuento: '))
        descuento(precio_producto, descuento_aplicar)

    elif menu == 3:
        peso = int(input('Ingrese su peso: '))
        estatura = int(input('Ingrese si estatura: '))
        calcular_imc(peso, estatura)
    
    elif menu == 4:
        print('Saliendo del menu...')
        break

    else:
        print('Error valor no valido')
        

    







    






