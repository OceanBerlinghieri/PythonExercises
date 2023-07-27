year = int(input("Escribe el año: "))

if year < 1582:
    print("Año no dentro de periodo gregoriano")
elif year % 4 != 0:
    print("Año comun")
elif year % 100 != 0:
    print("Año bisiesto")
elif year % 400 != 0:
    print("Año comun")
else:
    print("Año bisiesto")
    
