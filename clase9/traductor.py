diccionario = {"hola":"hello", "chau":"bye"}
terminaBucle = False

while True:
    palabra = input("Introduce la plalabra: ")

    if (palabra in diccionario):
        print("Español : ingles")
        print(f"{palabra} : {diccionario[palabra]}")

    else:
        print("La palabra no existe")
        resp = input("Desea registrarlo (si/no), salir(x): ")
        if resp == "si" or resp == "yes":
            #registrar
            traduccion = input("Ingrese la traduccion: ")
            if traduccion != "":
                diccionario[palabra] = traduccion
        elif (resp == "x"):
            break