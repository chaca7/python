num = 2
print("Numeros pares con while")
while num < 100:
    if( num % 2 == 0):
        print (num)
    num+=1
print("Numeros pares con for")
for num  in range(2,101,2):
    print(num)