bloques = int(input("¿Cuántos bloques disponemos?"))
altura = 1
while(bloques > altura+1):
    altura += 1
    bloques -= altura

print("La altura de la piramide es:", altura)
