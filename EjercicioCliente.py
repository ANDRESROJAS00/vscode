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
#Si la renta esta entre 0 a 599.999 debe entrar a la categoria de Life, si la renta esta entre 600.000 a 1.699.999 sera Gold y si esta entre
# $1.700.000 en adelante elite.
#Por ultimo el programa debe poder hacer la consulta por el rut del cliente para saber sus datos  categorias

clienteElite = []
clienteGold = []
clienteLife = []

while True:


    nombre = input("Ingrese su nombre: ")
    if any(i.isdigit() for i in nombre):
        print("Ingresó un digito, ingrese solo letras.")
        continue

    rut = input("Ingrese su rut sin digito verificador: ")

    renta = input("Ingrese su renta: ")

    try:
        rut = int(rut)
        suma = 0
        multiplo = 2

        for i in (str(rut)):
            suma += int(i) * multiplo
            multiplo += 1
            if multiplo == 8:
                multiplo = 2
        resto = suma % 11
        verificador = 11 - resto

        conVerificador = str(rut) + str(verificador)

        rutConGuion = conVerificador[:8] + "-" + conVerificador[8]

        nombre = nombre.upper()
        conVerificador = rutConGuion.upper()

        


        






    except ValueError:
        continue

    

    


    







