contador = "1"
cadenaFinal = ""
while contador == "1":
    nombre = input("Ingrese el nombre del empleado\n")
    numeroDias = int(input("Ingrese el número de días trabajados\n"))
    costoDia = float(input("Ingrese el costo del día trabajado\n"))
    pagoEmpleados = numeroDias * costoDia
    cadenaFinal = "%s%s\t%d\t$%.2f\t\t$%.2f\n" % \
                  (cadenaFinal, nombre, numeroDias, costoDia, pagoEmpleados)
    contador = input("Ingrese el numero 1 si hay otro empleado "
                     "o Ingrese cualquier numero o letra exepto el 1 "
                     "para mostrar la tabla\n")
print("%s\n" % cadenaFinal)