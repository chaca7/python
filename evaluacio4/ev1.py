MONTOIRP = 80000000
sueldo = int(input("Ingrese la cantidad de su sueldo: "))

sueldoAnual = sueldo * 12
if sueldoAnual >= MONTOIRP :
    print(f"Esta persona debe pagar impuestos por que su sueldo es de {sueldoAnual}")
else:
    print(f"Esta persona no debe pagar los impuestos por que su sueldo es de {sueldoAnual}")
    