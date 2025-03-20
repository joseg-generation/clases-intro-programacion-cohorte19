# Las listas se pueden ocupar en multiples casos de uso:
# Listados de elemetos de un mismo tipo o tipos diferentes

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# listas o list

frutas = ["manzana", "banana", "naranja", "uva", "kiwi"]
#index         0         1         2         3     4


# print(frutas)

frutas.append("pera") # agrega un elemento al final de la lista

# print(frutas)

lista_supermercado = []

lista_frutas = ["pera", "mango", "sandía", "melón", "mango"]

lista_carne = ["res", "cerdo", "pollo"]

lista_supermercado.append(lista_frutas) # [ ["pera", "sandía", "melón", "mango"] ]

lista_supermercado.append(lista_carne) # [ ["pera", "sandía", "melón", "mango"], ["res", "cerdo", "pollo"] ]
#                                                           0                                1

# ["pera", "sandía", "melón", "mango"]
#    0        1         2        3

# print(lista_supermercado[0].index("mango")) # 3  Se busca el indice de mango cuando la lista esta dentro otra lista


# print(lista_frutas.index("mango")) # 3


lista_frutas.insert(1, "uva") # ["pera", "uva", "mango", "sandía", "melón", "mango"] agrega un elemento en la posición 1

lista_frutas.pop() # ["pera", "uva", "mango", "sandía", "melón"] Elimina el ultimo elemento de la lista
del lista_frutas[0] # ["uva", "mango", "sandía", "melón"] Elimina el elemento en la posición 0

# print(lista_frutas)


list_estudiantes = []

nombre_estudiante_1 = input("¿Cuál es tu nombre?: ")
nombre_estudiante_2 = input("¿Cuál es tu nombre?: ")
nombre_estudiante_3 = input("¿Cuál es tu nombre?: ")

## se agregan los nombres a la lista

list_estudiantes.append(nombre_estudiante_1) 
list_estudiantes.append(nombre_estudiante_2)
list_estudiantes.append(nombre_estudiante_3)

print(list_estudiantes)