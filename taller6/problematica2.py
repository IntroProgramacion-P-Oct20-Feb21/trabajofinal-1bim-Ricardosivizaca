cadenaFinal = ""
contador = 1
denominador = 19
while contador <= 6:
    if (contador % 2) == 0:
        denominador = denominador + 10
        cadenaFinal = "%s %d/%d   " % (cadenaFinal, contador, denominador)
    else:
        denominador = denominador - 9
        cadenaFinal = "%s %d/%d   " % (cadenaFinal, contador, denominador)
    contador = contador + 1
print(f"{cadenaFinal}")