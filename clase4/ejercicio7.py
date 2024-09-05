def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos(rango_inferior, rango_superior):
    primos = []
    for numero in range(rango_inferior, rango_superior + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

rango_inferior = int(input("Ingrese el número inferior del rango: "))
rango_superior = int(input("Ingrese el número superior del rango: "))

primos_en_rango = encontrar_primos(rango_inferior, rango_superior)

if primos_en_rango:
    print(f"Números primos entre {rango_inferior} y {rango_superior}:")
    print(", ".join(map(str, primos_en_rango)))
else:
    print(f"No se encontraron números primos entre {rango_inferior} y {rango_superior}.")
