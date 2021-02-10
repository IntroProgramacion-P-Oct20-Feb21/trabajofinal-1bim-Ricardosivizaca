cadenaFinal = ""
totalEdades = ""
bandera = True
sumaEstaturas = 0.00
contador = 0
sumaEdades = 0
cadenaFinal = "%s%s\n" % (cadenaFinal, "Listado de Jugadores")
while bandera:
    nombreJugador = input("Ingrese el nombre del jugador\n")
    posicion = input("Cual es la posición que juega en el campo?\n")
    edad = int(input("Cual es la edad del jugador?\n"))
    estatura = float(input("Cual es la estatura del jugador?\n"))
    sumaEstaturas = sumaEstaturas + estatura
    sumaEdades = sumaEdades + edad
    contador = contador + 1
    cadenaFinal = "%s%d. %s - %s-, edad %d, estatura %.2f\n" % \
                  (cadenaFinal, contador, nombreJugador,
                   posicion, edad, estatura)
    totalEdades = "%s%d\n" % (totalEdades, edad)
    salir = int(input("Si no hay mas jugadores que añadir escriba "
                      "cualquier numero mayor a 1\n"))
    if salir >= 1:
        bandera = False
promedioEdad = sumaEdades / contador
promedioEstatura = sumaEstaturas / contador
cadenaFinal = "%sListado de Edades\n%sPromedio de edades: %.2f\n" \
            "Promedio de estaturas: %.2f" % \
            (cadenaFinal, totalEdades, promedioEdad, promedioEstatura)
print("%s" % cadenaFinal)