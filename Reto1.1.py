# Crear una función que realice operaciones básicas (suma, resta, multiplicación
# , división) entre dos números, según la elección del usuario, la forma de 
# entrada de la función será los dos operandos y el caracter usado para la 
# operación. entrada: (1,2,"+"), salida (3).

# Definicion de variables
num1 = 0
num2 = 0
operacion = ""

# Definicion de la funcion
def calculadora(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2
    else:
        return "Operacion no valida"    

# Solicitar datos al usuario
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion deseada (+, -, *, /): ")

# Realizar la operacion y mostrar el resultado
print("El resultado es: ", calculadora(num1, num2, operacion))


