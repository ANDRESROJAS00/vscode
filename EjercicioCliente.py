#Ejercicio

#Crear un programa en funcion a la categoria declientes del banco
#1) Clientes Elites
#2)Clientes Gold
#3)Clientes Life

#El programa debe contener dentro elementos que almacenen los datos del cliente como nombre, rut, renta.

#Los datos ingresados de teclado deben ser,
# *Nombre
# *Rut
# *Renta

#Si la renta esta entre 0 a 599.999 debe entrar a la categoria de Life, si la renta 
#esta entre 600.000 a 1.699.999 sera Gold y si esta entre $1.700.000 en adelante elite.

#Por ultimo el programa debe poder hacer la consulta 
#por el rut del cliente para saber sus datos categorias

clienteElite = []
clienteGold = []
clienteLife = []


print("------------------------------")
print("Bienvenido al Menu de Cliente-")
print("(1)-Ingresar sus datos--------")
print("(2)-Consulta de datos por RUT-")
print("(3)-Exit----------------------")
print("------------------------------")

menu = input("Elija el opción del menu: ")

try:
    menu = int(menu)

    if menu == 1:

        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        rut = input("Ingrese su rut: ")
        renta = int(input("Ingrese su renta"))

        rut = rut[:-1] + "-" + rut[-1]
        rut = str(rut)

        nombre = nombre.upper()
        apellido = apellido.upper()
        rut = rut.upper()

        addLista = [nombre, apellido, rut, renta]

        if renta >= 0 and renta <= 599999:
            clienteLife.append(addLista)
        elif renta >= 600000 and renta <= 1699999:
            clienteGold.append(addLista)
        elif renta >= 1700000:
            clienteElite.append(addLista)
        else:
            print("Valor no valido")

        for i in clienteLife:
            nombre, apellido, rut, renta = i
            print("Nombre: ",nombre)
            print("Apellido: ", apellido)
            print("Rut: ", rut)
            print("Renta: ", renta)


except ValueError:
    print("Debe ingresar un valor del menu")






















  

    

    


    







