ingreso = float(input("Introduce tus ingresos: "))

if ingreso <= 85528:
    impuesto = ingreso * 0.18 -556.2
elif ingreso > 85528:
    impuesto = 14839.2 + (ingreso - 85528) *0.32

if impuesto <= 0:
    print("El impuesto es: 0.0 pesos")
else:
    print("El impuesto es:", round(impuesto,0), "pesos")
                
