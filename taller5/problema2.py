porcentaje = 15
articulos = int(input("Ingrese la cantidad que se requiere del artículo\n"))
precioUnitario = float(input("Ingrese el precio unitario del articulo\n"))
costo = precioUnitario * articulos
if articulos > 50:
    descuento = (costo * porcentaje) / 100
    costo = costo - descuento
print("El costo total del pedido del articulo es de: %.2f" % costo)