
#definimos la función
def print_hello_world():  # esta función no recibe parámetros
    print("Hola cohorte 19!!")
    print("Esta es otra línea1")


#invocarla

#print("Imprimiendo después de la función!!! ")

#print_hello_world()

# Definiendo la función
def hola_estudiante(name):  # función que recibe parámetros
    print(f"Hola, ¿cómo estas {name}?")


#invocar función hola_estudiante
#hola_estudiante("Alberto")
#hola_estudiante("Luisa")
#hola_estudiante("Moises")

# nombre = input("Ingresa tu nombre: ")

# hola_estudiante(nombre)

#definimos la función
def sumar_dos_numeros(num1, num2):
    resultado = num1 + num2
    return resultado  # return retorna el valor fuera de la función

def restar(num1, num2):
    resultado = num2 - num1
    return resultado

def multiplicar(num1, num2):
    resultado = num2 * num1
    return resultado


#invocamos
resultado1 = sumar_dos_numeros(2,3) # en esta invocación num1 = 2 y num2 = 3   --> 6
resultado2 = sumar_dos_numeros(4,6) # --> 10

#print(f"El resultado de primera suma es: {resultado1} y el resultado de la segunda suma es: {resultado2}")


print("Bienvenidos al servicio de cálculo!!")
operacion = input("Indica que operación quieres realizar: sumar o restar: ")



num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))


if operacion == "sumar":
    resultado = sumar_dos_numeros(num1, num2)
    print(f"La suma es : {resultado}")
elif operacion == "restar":
    resultado = restar(num1, num2)
    print(f"La resta es : {resultado}")
else:
    print("No se realizar esa operación")



resultado = sumar_dos_numeros(num1, num2)

#print(f"El resultado de la suma es: {resultado}")

