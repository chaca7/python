def encontrar_vocales(palabra):
    vocales = 'aeiou'
    
    palabra = palabra.lower()

    vocales_encontradas = set()
    
    for letra in palabra:
        if letra in vocales:
            vocales_encontradas.add(letra)
    
    return vocales_encontradas

palabra_usuario = input("Introduce una palabra: ")

vocales = encontrar_vocales(palabra_usuario)
print(f"Las vocales encontradas en '{palabra_usuario}' son: {', '.join(vocales)}")
