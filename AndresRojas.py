

print('-------------------------------------')
print('--------------PizzaDuoc--------------')
print('(1)Comprar---------------------------')
print('(2)Salir-----------------------------')
print('-------------------------------------')


pizzaTradicional = 12000
pizzaPeperoni = 14000
pizzaAllcarnes = 17000
total = 0
#----------------------------------
cantpizzaTradicional = 0
cantpizzaPeperoni = 0
cantpizzaAllCarnes = 0
#----------------------------------
totalTradicional = 0
totalPeperoni = 0
totalAllCarnes = 0
#----------------------------------
descuentoDiurno = 0
descuentoVespertino = 0

while True:

    menu = int(input("Ingrese una opción del menu: "))
    print()

    #ELEJIMOS LA OPCION DE COMPRA
    if menu == 1:

        print("Pizza Tradicional $12.000 c/u\n")

        opcion1 = int(input('Ingrese la cantidad de PizzaTradicional: '))
        print()

        cantpizzaTradicional += opcion1
        cantTradicional = opcion1 * pizzaTradicional
        totalTradicional += cantTradicional

        print('PizzaPeperoni $14.000 c/u\n')

        opcion2 = int(input('Ingrese la cantidad de PizzaPeperoni: '))
        print()

        cantpizzaPeperoni += opcion2
        cantPeperoni = opcion2 * pizzaPeperoni
        totalPeperoni += cantPeperoni

        print('PizzaAllCarnes $17.000 c/u\n')

        opcion3 = int(input('Ingrese la cantidad de Pizza All Carnes: '))
        print()

        cantpizzaAllCarnes += opcion3
        cantAllCarnes = opcion3 * pizzaAllcarnes
        totalAllCarnes += cantAllCarnes

        total =+ totalTradicional + totalPeperoni + totalAllCarnes

        #PREGUNTAMOS QUE TIPO DE ESTUDIANTES SOMOS
        tipo_estudiante = int(input('INGRESE EL TIPO DE ESTUDIANTE\n(1)Diurno descuento de 12%\n(2)Vespertino descuento de 10%\n(3)Admnistrativo sin descuento\n'))
        print()
        
        if tipo_estudiante == 1:
            descuentoDiurno = total * 0.88

            print('BOLETA DE SU COMPRA')
            print('*',cantpizzaTradicional, 'Pizza Tradicional', totalTradicional )
            print('*',cantpizzaPeperoni ,'Pizza Peperoni: ', totalPeperoni )
            print('*', cantpizzaAllCarnes,'Pizza All Carnes: ', totalAllCarnes )
            print('**********************************************')
            print('Total sin descuento: ', total)
            print('Total de su compra con descuento Diurno: ', descuentoDiurno)

        
        elif tipo_estudiante == 2:
            descuentoVespertino = total * 0.88
            

            print('BOLETA DE SU COMPRA')
            print('*',cantpizzaTradicional, 'Pizza Tradicional: ', totalTradicional )
            print('*',cantpizzaPeperoni ,'Pizza Peperoni: ', totalPeperoni )
            print('*',cantpizzaAllCarnes,'Pizza All Carnes: ', totalAllCarnes )
            print('**********************************************')
            print('Total sin descuento: ', total)
            print('Total de su compra con descuento Vespertino: ', descuentoVespertino)

        else:
            print('Valor no valido')

        
    elif menu  == 2:
        print('Fin del programa')
        break







        






