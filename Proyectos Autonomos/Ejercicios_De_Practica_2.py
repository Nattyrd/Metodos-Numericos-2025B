import math

# EJE 21 Multiplica una cadena por un numero entero y muestra el resultado}

cadena = "Hola"
numero = 3
resultado = cadena * numero # La cadena se repite 'numero' veces
print("Resultado de multiplicar la cadena por el número:", resultado)

# EJE 22 Divide una cadena en una lista de subacadenas

cadena = "Hola, ¿cómo estás?"
subcadenas = cadena.split() # Divide la cadena en palabras usando el espacio como separador
print("Lista de subcadenas:", subcadenas)

# EJE 23 Verifica si una palabtra es un palíndromo
palabra = "radar"
es_palindromo = palabra == palabra[::-1] # Compara la palabra con su reverso
print(f"¿La palabra '{palabra}' es un palíndromo?:", es_palindromo)

#EJE 23 Eliminar un elementos especifico de una lista
mi_lista = [1, 2, 3, 4, 5, 3, 6]
elemento_a_eliminar = 3
mi_lista.remove(elemento_a_eliminar) # Elimina la primera ocurrencia del elemento
print("Lista después de eliminar el elemento", elemento_a_eliminar, ":", mi_lista)  

# EJE 24 Genera una lista de numeros del 1 al 200
numeros = list(range(1, 201)) # Genera una lista de números del 1 al 200
print("Lista de números del 1 al 200:", numeros)

# EJE 26 Intercambia los valores de dos variables con asignación múltiple
a = 5
b = 10
a, b = b, a # Intercambia los valores
print("Después del intercambio, a es:", a, "y b es:", b)

# EJE 27 Realiza operaciones de conjuntos union, intersección y diferencia
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
union = conjunto1 | conjunto2
interseccion = conjunto1 & conjunto2
diferencia = conjunto1 - conjunto2
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia (conjunto1 - conjunto2):", diferencia)

# EJE 28 Extrae un elemento especifico de una tupla
mi_tupla = (10, 20, 30, 40, 50)
elemento = mi_tupla[2] # Extrae el tercer elemento (índice
print("Elemento extraído de la tupla:", elemento)

# EJE 29 Combina dos listas en pares usando zip
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
combinados = list(zip(lista1, lista2)) # Combina las listas en pares
print("Listas combinadas en pares:", combinados)

# EJE 3O Eliminar duplicados de una lista
mi_lista = [1, 2, 2, 3, 4, 4, 5]
mi_lista_sin_duplicados = list(set(mi_lista)) # Convierte la lista a un conjunto y luego de vuelta a lista 
print("Lista sin duplicados:", mi_lista_sin_duplicados)

