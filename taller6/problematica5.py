contador = 1
cadenaFinal = ""
while contador <= 4:
    nombreEstudiante = input("Ingrese su nombre\n")
    promedioCiclo = float(input("Ingrese su promedio del ciclo\n"))
    if promedioCiclo >= 7:
        notaFinal = "Aprobado"
        cadenaFinal = "%s%s\t %.2f\t%s\n" % \
                      (cadenaFinal, nombreEstudiante, promedioCiclo, notaFinal)
    else:
        notaFinal = "Reprobado"
        cadenaFinal = "%s%s\t %.2f\t%s\n" % \
                      (cadenaFinal, nombreEstudiante, promedioCiclo, notaFinal)
    contador = contador + 1
print(cadenaFinal)