costoCpu = float(input("Ingrese el valor del CPU\n"))
costoTeclado = float(input("Ingrese el valor del teclado\n"))
costoPantalla = float(input("Ingrese el valor del pantalla\n"))
costoRaton = float(input("Ingrese el valor del raton\n"))
costoTotal = costoCpu + costoTeclado + costoPantalla + costoRaton
print("El costo total de la computadora es: %.2f $" % costoTotal)