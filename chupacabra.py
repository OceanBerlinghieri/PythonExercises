palabra = "chupacabra"

s = input("Introduce una palabra: ")
while(s != palabra):
    if(s == palabra):
        break;
    s = input("Introduce una palabra: ")

print("Has dejado el bucle con éxito")
