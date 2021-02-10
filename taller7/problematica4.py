numerador = 1
contadorDenominador = 3
cadena = ""
operacion = 1
cadena = "%s%d" % (cadena, numerador)
for i in range(1, 8):
    if (i % 2) == 0:
        cadena = "%s + %d/%d" % (cadena, numerador,
                                 contadorDenominador)
        operacion = operacion + (numerador / contadorDenominador)
    else:
        cadena = "%s - %d/%d" % (cadena, numerador,
                                 contadorDenominador)
        operacion = operacion - numerador / contadorDenominador
    contadorDenominador = contadorDenominador + 2
cadena = "%s = %.2f" % (cadena, operacion)
print("\n%s" % cadena)
