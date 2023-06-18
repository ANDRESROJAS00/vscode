examenes_agendados = []

examenes_disponibles = {
    "ECO": 15000,
    "SCANNER": 25000,
    "RAYO": 10000
}

def agendar_examen():
    nombre = input("Ingrese su nombre: ")
    rut = input("Ingrese su rut: ")
    print("Exámenes disponibles:")
    for examen, valor in examenes_disponibles.items():
        print(examen, "- Valor:", valor)
    tipo_examen = input("Ingrese el tipo de examen que desea agendar: ")
    
    if tipo_examen in examenes_disponibles:
        examen_agendado = {
            "nombre": nombre,
            "rut": rut,
            "tipo_examen": tipo_examen,
            "pagado": False
        }
        examenes_agendados.append(examen_agendado)
        print("Examen agendado con éxito.")
    else:
        print("El tipo de examen ingresado no es válido.")

    
def pagar_examen():
    rut = input("Ingrese su rut: ")
    encontrado = False
    
    for examen in examenes_agendados:
        if examen["rut"] == rut and not examen["pagado"]:
            tipo_examen = examen["tipo_examen"]
            valor = examenes_disponibles[tipo_examen]
            print("Examen a pagar:", tipo_examen)
            print("Valor a pagar:", valor)
            examen["pagado"] = True
            encontrado = True
            break
    
    if not encontrado:
        print("No se encontró ningún examen pendiente de pago para el rut ingresado.")


def consultar_examenes_disponibles():
    print("Exámenes disponibles:")
    for examen, valor in examenes_disponibles.items():
        print(examen, "- Valor:", valor)


def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agendar examen")
        print("2. Pagar examen")
        print("3. Consultar exámenes disponibles")
        print("4. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            agendar_examen()
        elif opcion == "2":
            pagar_examen()
        elif opcion == "3":
            consultar_examenes_disponibles()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")