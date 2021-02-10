marca = input("Ingrese la marca del vehiculo\n")
origen = int(input("Seleccione el numero del origen de su auto\n"
                   f"1.Alemania\n2.Japon\n3.Italia\n4.USA\n5.Otro Pais\n"))
costo = float(input("Ingrese el costo del vehiculo\n"))
if origen == 1:
    porcentaje = 20
    impuesto = (porcentaje * costo) / 100
    precioVenta = costo + impuesto
    print(f"El impuesto por pagar es: {impuesto:.2f} y el precio de "
          f"venta es: {precioVenta:.2f}")
if origen == 2:
    porcentaje = 30
    impuesto = porcentaje * costo / 100
    precioVenta = costo + impuesto
    print(f"El impuesto por pagar es: {impuesto:.2f} y el precio de "
          f"venta es: {precioVenta:.2f}")
if origen == 3:
    porcentaje = 15
    impuesto = (porcentaje * costo) / 100
    precioVenta = costo + impuesto
    print(f"El impuesto por pagar es: {impuesto:.2f} y el precio de "
          f"venta es: {precioVenta:.2f}")
if origen == 4:
    porcentaje = 8
    impuesto = (porcentaje * costo) / 100
    precioVenta = costo + impuesto
    print(f"El impuesto por pagar es: {impuesto:.2f} y el precio de "
          f"venta es: {precioVenta:.2f}")
if origen == 5:
    impuesto = 0
    precioVenta = costo + impuesto
    print(f"El impuesto por pagar es: {impuesto:.2f} y el precio de "
          f"venta es: {precioVenta:.2f}")