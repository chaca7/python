total_calificaciones = 0
suma_calificaciones = 0
cantidad_calificaciones = 0

print("Introduce las calificaciones de los alumnos (entre 1 y 5). Introduce 0 para finalizar.")

while True:
    try:
        calificacion = float(input("Ingrese una calificación: "))
        
        if calificacion == 0:
            break
        
        if calificacion < 1 or calificacion > 5:
            print("La calificación debe estar entre 1 y 5. Por favor, ingrese una calificación válida.")
            continue
        
        suma_calificaciones += calificacion
        cantidad_calificaciones += 1
    
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

if cantidad_calificaciones > 0:
    promedio = suma_calificaciones / cantidad_calificaciones
    print(f"El promedio general de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")
