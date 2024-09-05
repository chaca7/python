def imprimir(l):
    """Imprime el contenido de una lista en formato tabular."""
    for x in range(len(l)):
        print(f" | {l[x]}", end="")

def ordenar(ls, ord="ASC"):
    """Ordena una lista en orden ascendente o descendente.

    Args:
        ls: La lista a ordenar.
        ord: El tipo de ordenamiento ("ASC" para ascendente, "DESC" para descendente).
    """
    if ord not in ("ASC", "DESC"):
        raise ValueError("Tipo de ordenamiento inválido")

    n = len(ls)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if (ord == "ASC" and ls[i] > ls[i + 1]) or (ord == "DESC" and ls[i] < ls[i + 1]):
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True

lista = [45, 23, 25, 14, 44, 9, 8, 2, 1, 4, 300]
print("Vector original")
imprimir(lista)

orden = "ASC"
ordenar(lista, orden)
print(end="\n")
print(f"Vector ordenado {orden}")
imprimir(lista)