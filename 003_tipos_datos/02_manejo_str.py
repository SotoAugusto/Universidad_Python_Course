# string

Grupo = "Dream Theater"
Genero = "Progressive Metal"
info = Grupo + " " + Genero

# Concatenación con +
print("Mi grupo favorito es: " + info)

# Concatenación en print

print("Mi grupo favorito es: ", Grupo, Genero)

# Esto NO es concatenacion de numeros
variable1 = "22"
print(variable1)
variable2 = "44"
print(variable2)
print("CONCATENACION DE CADENA, NO SON NUMEROS: ", variable1 + variable2)

# convertir string a int
int(variable1)
int(variable2)

print("al convertir las cadenas a numeros, el + ahora representa una suma :\n", variable1, "\n", variable2, "\n",
      (variable1 + variable2))
