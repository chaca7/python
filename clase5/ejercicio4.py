import random

while True:
    aleatorio = random.randrange(1,3)
    elijePc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Elige tu opcion"))
    
    if opcion == 1:
        elijeUsuario = "Piedra"
    elif opcion == 2:
        elijeUsuario = "Papel"
    elif opcion == 3:
        elijeUsuario = "Tijera"
    print("Elejiste: ",elijeUsuario)

    if aleatorio == 1:
        elijePc = "Piedra"
    elif aleatorio == 2:
        elijePc = "Papel"
    elif aleatorio == 3:
        elijePc = "Tijera"
    print("La maquina elijio: ", elijePc)
    print("...")
    if elijePc == "Piedra" and elijeUsuario == "Papel":
        print("Ganaste, Papel  envuelve Piedra")
    elif elijePc == "Papel" and elijeUsuario == "Tijera":
        print("Ganaste, Tijera corta papel")
    elif elijePc == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste, Piedra machaca Tijera")
    if elijePc == "Papel" and elijeUsuario == "Piedra":
        print("Perdiste, Papel envuelve piedra")
    elif elijePc == "Tijera" and elijeUsuario == "Papel":
        print("Perdiste, Tijera corta papel")
    elif elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("Perdiste, Piedra machaca Tijera")
    elif elijePc == elijeUsuario:
        print("empate")
    