#Comentario
def parImpar(num):
    if num % 2 == 0:
        print("Es un número par")
                
    if num % 2 != 0:
        print("Es un número impar")

while True:
    opcion = input("Introduce 0 si quieres salir: ")
    
    if opcion == '0':
        break
    
    try:
        num = int(input("En que número estás pensando?: "))
        parImpar(num)
    except ValueError:
        print("El valor introducido debe ser un número entero")
  
