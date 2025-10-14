import math
# hola mundo
print("Hola, mundo!")

# EJE1 Suma de dos números y mostrar el resultado
numero1 = 12
numero2 = 9
suma = numero1 + numero2
print("La suma de", numero1, "y", numero2, "es:", suma)

# EJE 2 Calcular el area de un círculo dado su radio
radio = 12
area_circulo = math.pi * radio ** 2
print("El área de un círculo con radio", radio, "es:", area_circulo)

# EJE 3 Concatena dos cadenas de texto y muestra el resultado
cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2
print("Cadena concatenada:", cadena_concatenada)

#EJE 4 Crea una lista con diferentes elementtos e imprimela
mi_lista = [1, 2, 3, "cuatro", True, 6.0]
print("Mi lista es:", mi_lista)

# EJE 5 Realiza una multiplicación de dos números y muestra el resultado
num1 = 12
num2 = 9
multiplicacion = num1 * num2
print("La multiplicación de", num1, "y", num2, "es:", multiplicacion)

# EJE 6 Crea una cadena de texto y muestra su longitud
mi_cadena = "Hola, ¿cómo estás?"
longitud_cadena = len(mi_cadena)
print("La longitud de la cadena es:", longitud_cadena)

# EJE 7 Calcula el promedo de una lista de números y su resultado (Las listas son mutables)
numeros = [10, 20, 30, 40, 50]
promedio = sum(numeros) / len(numeros)
print("El promedio de la lista es:", promedio)

# EJE 8 Crea una tupla con elementos e imprimela (Las tuplas son inmutables)
mi_tupla = (1, 2, 3, "cuatro", False, 6.0)
print("Mi tupla es:", mi_tupla)

# EJE 9 Realiza la potencia de un número y muestra el resultado
base = 10
exponente = 8
potencia = base ** exponente
print(base, "elevado a la", exponente, "es:", potencia)

# EJE 10 Invertir una cadena de texto y mostrar el resultado
cadena_original = "Hola, mundo, viva Ecuador"
cadena_invertida = cadena_original[::-1] # Invertir la cadena usando slicing 
print("Cadena invertida:", cadena_invertida)

# EJE 11 Calcular el área de un triángulo dado su base y altura al usuario
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = (base * altura) / 2
print("El área del triángulo es:", area_triangulo)

# EJE 12 Convierte un numero en cadena
numero = 123444
cadena_numero = str(numero)
print("El número como cadena es:", cadena_numero)

# EJE 13 Remplaza un caracter en una cadena de texto
cadena = "Hola a todos"
cadena_modificada = cadena.replace("a", "@") # Reemplazar 'a' por '@' y guardar en una nueva variable
print("Cadena modificada:", cadena_modificada)

# EJE 14 Pasa una cadena de mayusculas a minusculas
cadena_mayusculas = "HOLA AMIGOS"
cadena_minusculas = cadena_mayusculas.lower() # Convertir a minúsculas y guardar en una nueva variable LOWER()
print("Cadena en minúsculas:", cadena_minusculas)

# EJE 15 Ordenar una lista de números de menor a mayor
lista_numeros = [34, 12, 5, 67, 23, 89]
lista_numeros.sort() # Ordenar la lista en su lugar #SORT()
print("Lista ordenada de menor a mayor:", lista_numeros)

#EJE 16 Calcular el elevado a la 4 potencia sin usar el operador **
base = 3
exponente = 4
potencia = pow(base, exponente) # Usar la función pow() para calcular la potencia #POW()
print(base, "elevado a la", exponente, "es:", potencia)

# EJE 17 Extraer una subcadena de una cadena de texto
cadena = "Hola, bienvenidos a Python"
subcadena = cadena[6:16] # Extraer desde el índice 6 hasta el 15 usando slicing
print("Subcadena extraída:", subcadena) 

# EJE 18 numero decimal a entero
numero_decimal = 45.67
numero_entero = int(numero_decimal) # Convertir a entero usando int()
print("Número entero:", numero_entero)

# EJE 19 Cuenta las concurrencias de un caracter en una cadena de texto
cadena = "banana"
caracter = "a"
concurrencias = cadena.count(caracter) # Contar las ocurrencias usando count()
print("El caracter", caracter, "aparece", concurrencias, "veces en la cadena.")

# EJE 20 Encuentra y miestra el ultimo digito de una cadena de texto
cadena = "Hola, amigas"
ultimo_caracter = cadena[-1] # Acceder al último carácter usando indexación negativa
print("El último carácter de la cadena es:", ultimo_caracter)




