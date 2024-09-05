def criba_eratostenes(max_num):
    es_primo = [True] * (max_num + 1)
    es_primo[0] = es_primo[1] = False
    p = 2
    while p * p <= max_num:
        if es_primo[p]:
            for i in range(p * p, max_num + 1, p):
                es_primo[i] = False
        p += 1
    return [p for p in range(max_num + 1) if es_primo[p]]

def encontrar_primos_en_rango(rango_inferior, rango_superior):
    primos_totales = criba_eratostenes(rango_superior)
    primos_en_rango = [p for p in primos_totales if p >= rango_inferior]
    return primos_en_rango

rango_inferior = int(input("Ingrese el número inferior del rango: "))
rango_superior = int(input("Ingrese el número superior del rango: "))

primos_en_rango = encontrar_primos_en_rango(rango_inferior, rango_superior)

if primos_en_rango:
    print(f"Números primos entre {rango_inferior} y {rango_superior}:")
    print(", ".join(map(str, primos_en_rango)))
else:
    print(f"No se encontraron números primos entre {rango_inferior} y {rango_superior}.")
