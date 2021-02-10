num2 = -1
numero = 1
cadenaFinal = ""
for i in range(1, 7):
    num2 = num2 + 2
    numero = numero + num2
    cadenaFinal = "%s%d " % (cadenaFinal, numero)
print("\n%s" % cadenaFinal)