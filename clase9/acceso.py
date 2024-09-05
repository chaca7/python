acceso = {"admin": 111, "jose": 222}

user = input("ingresa tu usuario: ")
password = int(input("ingresa tu contraseña: "))

if user in acceso:
    if acceso[user] == password:
        print("Acceso concedido")
    else:
        contador = 2
        while contador <= 3:
            print(f"Contraseña incorrecta. Intento {contador}")
            password = int(input("ingresa tu contraseña: "))
            if acceso[user] == password:
                print("Acceso concedido")
                break # detener el buclue
            contador += 1
        if(contador > 3):
            print("Ya no tienes intentos... ")
        
else:
    print("Usuario no encontrado")
