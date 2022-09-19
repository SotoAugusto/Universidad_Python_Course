numA = int(input("Introduce un el primer número: \n"))
numB = int(input("Introduce un el segundo número: \n"))

if numA != numB:
    if numA > numB:
     print(f"El primer número ({numA}) es mayor")
    else:
     print(f"El segundo número ({numB}) es mayor")
else:
    print("los numeros son iguales")
