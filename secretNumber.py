secret_number = 777

print(
"""
+=========================================+
| ¡Bienvenido a mi juego, muggle!         |
| Introduce un número entero              |
| y adivina qué número he elegido para ti.|
|                                         |
| ¿Cuál es el número secreto?             |      
|                                         |
+=========================================+
""")

num = int(input("Introduce un numero: "))

while num != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    num = int(input("Introduce un numero: "))

print("Bien hecho, ¡ahora eres libre!")
