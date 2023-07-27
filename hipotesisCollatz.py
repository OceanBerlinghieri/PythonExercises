c0 = int(input("Introduce un numero mayor que cero: "))
pasos = 1
print(c0)
while(c0 <= 0):
    c0=int(input("El numero debe ser mayor a cero:"))

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3*c0+1

    print(c0)
    pasos+=1

print("Pasos =", round(pasos, 0))

