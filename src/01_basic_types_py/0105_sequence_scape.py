print('0105 Secuencias de escape.')

# Las secuencias de escape son como codigos secretos que emplean el operador \ para representar dentro de un string simbolos especiales que dependiendo de las codificacion no se presentan.

# La barra invertida es el caraácter de escape. 

# 1. Las secuencias mas utilizadas
# \n Salto de linea, para crear espacios horizontales o sangrias
print("Line 1\nLine 2\nLine 3")

# \t Tabulación, para crear espacios horizontales o sangrias
print("Name:\tJhon")
print("Edad:\t25.00")

# \' Cómilla simple, para usar comillas simples dentro de un string de comillas simples.
print("She says: \"Hola\"")

# \" comilla doble, para usar comillas dobles dentro de un string de comillas dobles.
print("She says: \'Hola\'")

# \\ Barra invertida, para imprimir una barra literal (como en rutas de archivos).
print("C:\\Users\\Documents")

# 3. Truco de raw strings (r)
# A veces, especialmente cuando trabajas con rutas de archivos o expresiones regulares, poner \\ en todos lados es un dolor de cabeza. Para estoexisten los raw strings (strings crudos)
# Si pones una r antes de las comillas, Python igonorá todas las secuencias de escape.

# Sin Raw String
print("C:\\names\\file.txt")

# Con Raw String (Python lo imprime como esta)
print(r"C:\\names\\file.txt")

# Ejercicio:
# Intenta imprimir en una sola línea de código (un solo print) lo siguiente, respetando los espacios y las líneas:
# LISTA DE COMPRA:
#     * Pan
#     * Leche
#     * "Huevos"

# Solución:
print("LISTA DE COMPRA\n\t* Pan\n\t* Leche\n\t* \"Huevos\"")