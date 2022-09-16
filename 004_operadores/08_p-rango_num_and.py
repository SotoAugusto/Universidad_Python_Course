numero = int(input("Introduce un numero entero:\n"))
bool = False
if numero >= 0 and numero <= 5:
  print(f"El numero está dentro del rango 1-5 ")
  bool = True
  print(bool)
else:
    print(f"El numero esta fuera del rango 1 - 5")
    print(bool)