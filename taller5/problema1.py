porcentaje = 10
costoHora = float(input("Ingrese el valor de costo por kilovatio/hora\n"))
kilovatiosConsumidos = int(input("Ingrese el número de kilovatios consumidos en el mes.\n"))
edadCliente = int(input("Cual es la edad del cliente?\n"))
costoTotal = costoHora * kilovatiosConsumidos
if edadCliente > 65:
    descuento = (costoTotal*porcentaje)/100
    costoTotal = costoTotal - descuento
print("El costo total es: %.2f" % costoTotal)
