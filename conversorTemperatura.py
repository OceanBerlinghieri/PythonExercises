celsius = 100
fahrenheit = -185
kelvin = 25

fahrenheit_celsius = (fahrenheit - 32) *5 / 9
celsius_fahrenheit = (celsius * 9 / 5) + 32
kelvin_celsius = kelvin + 273.15
celsius_kelvin = celsius - 273.15
fahrenheit_kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
kelvin_fahrenheit = (kelvin - 273.15) * 9 / 5 + 32

print(fahrenheit, "grados fahrenheit son", round(fahrenheit_celsius, 2), "grados celsius")
print(celsius, "grados celsius son", round(celsius_fahrenheit), "grados fahrenheit")
print(kelvin, "grados kelvin son", round(kelvin_celsius), "grados kelvin")
print(celsius, "grados celsius son", round(celsius_kelvin), "grados kelvin")
print(fahrenheit, "grados fahrenheit son", round(fahrenheit_kelvin), "grados kelvin")
print(kelvin, "grados kelvin son", round(kelvin_fahrenheit), "grados fahrenheit")

