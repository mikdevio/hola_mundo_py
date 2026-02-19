print('0104 Metodos de variables tipo string')

# 1. Transformación de caractéres
# Estos métodos son ideales para estandarizar entrada de usuario (como emails o nombres).

# .upper() convierte todo a MAYÚSCULAS
original_text = "Hello, world for ultimate python course."
print(original_text.upper())

# .lower convierte todo a minúsculas
print(original_text.lower())

# .capitalize() Pone la primera letra en mayúsculas y el resto en minúsculas.
print(original_text.capitalize())

# .title() Pone la primera letra de cada palabra en mayúsculas
print(original_text.title())

# Las operaciones no alteran el texto original
print(original_text)

# 2. Limpieza de texto
# Estos métodos permiten eliminar expacios extra o caractéres indeseados
unclean_text = "    admin_123 "

# .strip() Elimina espacios en blanco al inicio y al final
print(unclean_text.strip())

# .lstrip() Solo elimina espacios a la izquierda
print(unclean_text.lstrip())

# .rstrip() Solo elimina espacios a la derecha
print(unclean_text.rstrip())

# 3. Búsqueda y remplazo de caracteres
# Estos métodos permiten buscar caracteres para remplazarlos
replasable_text = 'Python is a versatile programming language.'

# .replace(<cadena buscada>, <cadena de remplazo>) Intercambia una parte del texto por otra
print(unclean_text.replace("versatile", "all purpose"))

# .find(<cadena de busqueda>) Devuelve la posición (índice) donde comienza la palabra. Si no existe, devuelve -1.
print(unclean_text.find("programming"))

# .count(<cadena de buequeda>) Cuenta cuántas veces aparece un carácter o frase.
print(unclean_text.count("o"))

# 4. División y unión
# Fundamentales para proesar archivos o listas de datos ingresados como texto
divisible_text = "Python is the easiest programming langueage for begginers."

# .split(<separator>) Rompe el string y los convierte en una lista
print(divisible_text.split(' '))

# .join(<lista de cadenas de texto>) Une los elementos de una lista en un solo string (es el proeso inverso).
list_of_strings = divisible_text.split(' ')
print(", ".join(list_of_strings))