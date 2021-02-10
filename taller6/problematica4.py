contador = 1
cadenaFinal = ""
while contador <= 10:
    nombreJugador = input("Ingrese el nombre del jugador:\n")
    cantidadPuntos = int(input("Ingrese de Cantidad de los puntos>"
                               "que anoto en la temporada\n"))
    cantidadFaltas = int(input("Ingrese las faltas cometidas de la temporada\n"))
    cadenaFinal = "%s%s\t%d\t%d\n" % (cadenaFinal, nombreJugador, cantidadPuntos, cantidadFaltas)
    contador = contador + 1
print("\n%s" % cadenaFinal)