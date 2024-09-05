import os
resp = 1
while resp != 0:
    print("paint (1)")
    print("Calc (2)")
    print("Apagar PC en 2 hora (3)")
    print("Salir (0)")
    resp = int(input("Seleccione: "))
    if(resp == 1):
        os.system("mspaint")
    elif(resp == 2):
        os.system("calc")
    elif(resp == 3):
        os.system("shutdowm -s -t 7200")
    else:
        print("No entendido esa orden")