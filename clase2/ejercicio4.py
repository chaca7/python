nombre = "Tu nombre"
apellido = 'Apellido'

print(nombre + " " + apellido)

texto = "Este texto \n tiene salto de linea y \t tablulacion"
print(texto)

#Formateo

user, password, email = "moios", 12345, "admin@admin.com"
print("Su usuario y contraseña son {} {} y su email {}".format(user, password, email))
print("Su usuario y conrtraseña son %s %d y su email %s" %(user, password, email))
print("Su usuario y contraseña son " + user + " " + str(password) + "y su email" + email)
print("Su usuario y contraseña son {user} {password} y email {email}")