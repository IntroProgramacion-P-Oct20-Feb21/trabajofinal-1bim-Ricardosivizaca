nombreCliente = input("Ingrese el nombre del cliente\n")
numMensualidades = int(input("Cuantas mensualidades va a cancelar\n"))
contador = 1
valor = 0
cadenaFinal = ""
while contador <= numMensualidades:
    if contador > 1:
        input("Presione enter para pasar al siguiente pago")
    print("-----------------------------------------------"
          "\nSeleccione la empresa a la que va a cancelar\n"
          "Netflix\n"
          "Disney Plus \n"
          "Apple TV \n"
          "Amazon Prime \n")
    empresa = input("-")
    if empresa == "Netflix":
        valor = 10
        iva = (valor * 10) / 100
        totalCancelar = valor + iva
        cadenaFinal = "Usuario: %s\nEmpresa: %s \nPrecio " \
                      "base: $%.2f\nImpuesto: $%.2f\nTotal a cancelar: $%.2f\n" % \
                      (nombreCliente, empresa, valor, iva, totalCancelar)
    elif empresa == "Disney Plus":
        iva = (valor * 12) / 100
        totalCancelar = valor + iva
        cadenaFinal = "Usuario: %s\nEmpresa: %s \nPrecio " \
                      "base: $%.2f\nImpuesto: $%.2f\nTotal a cancelar: $%.2f\n" % \
                      (nombreCliente, empresa, valor, iva, totalCancelar)
    elif empresa == "Apple TV":
        valor = 5
        iva = (valor * 14) / 100
        totalCancelar = valor + iva
        cadenaFinal = "Usuario: %s\nEmpresa: %s \nPrecio " \
                      "base: $%.2f\nImpuesto: $%.2f\nTotal a cancelar: $%.2f\n" % \
                      (nombreCliente, empresa, valor, iva, totalCancelar)
    elif empresa == "Amazon Prime":
        valor = 4.50
        iva = (valor * 16) / 100
        totalCancelar = valor + iva
        cadenaFinal = "Usuario: %s\nEmpresa: %s \nPrecio " \
                      "base: $%.2f\nImpuesto: $%.2f\nTotal a cancelar: $%.2f\n" % \
                      (nombreCliente, empresa, valor, iva, totalCancelar)
    contador = contador + 1
    print("Su recibo es :\n%s" % cadenaFinal)