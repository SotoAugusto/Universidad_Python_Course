# instrucciones
# calcular area, y perimetro
# crear alto y ancho int

# usuario proporciona valores a las variables
# formulas: area = alto * ancho
# perimetro = (alto + ancho) * 2


alto = int(input("Proporciona el alto del rectángulo: "))
ancho = int(input("Proporciona el ancho del rectángulo: "))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")