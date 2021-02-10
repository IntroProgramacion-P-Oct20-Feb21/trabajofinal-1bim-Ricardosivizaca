plazo = 12
cantidadPrestamo = int(input("Ingrese la cantidad del prestamo a pedir\n"))
interesMensual = float(input("Cual es el interes mensual a cobrar?\n"))
pagoMensual = (cantidadPrestamo / plazo) + interesMensual
print(f"El valor a pagar mensualmente del prestamo con 1 año de plazo es de: {pagoMensual} $")