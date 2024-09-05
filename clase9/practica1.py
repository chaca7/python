"""Leer tres notas por teclado y cargarlos en una lista.
Calcular el promedio y si esta aprobado o reprobado.
si promedio >1.7 = aprobado sino reprobado"""

notas = []

#leer datos
for x in range(3):
    nota = float(input(f"ingrese la nota {x}: "))
    notas.append(nota)

#calcular el promedio y si esta aprobado o reprobado

sumNotas = sum(notas)

cantNotas = len(notas)

p=rom  sumNotas / cantNotas

if (prom >= 1.7):
    print(f"aprobaste tu promedio es de {prom:.2f}")
else:
    print(f"has reprobado tu promedio es de {prom:.2f}")