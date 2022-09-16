
numero = int(input("Ingrese un número entero: "))

# el resultado de dividir a numero entre dos es cero?

if numero % 2 == 0:
    print(f"El valor de {numero} es un número par")
    print(f"El residuo de la operación es ", (numero % 2))
  
else:
    print(f"El valor de {numero} NO un número impar")
    print(f"El residuo de la operación es ", (numero % 2))
    