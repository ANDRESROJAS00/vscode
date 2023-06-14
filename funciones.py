def calcular_iva(precio_objeto):
    iva = precio_objeto * 0.19
    return iva

def descuento(precio_producto, descuento_aplicar):
    des = precio_producto * (descuento_aplicar/100)
    total_descuento = precio_producto - des

def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc




