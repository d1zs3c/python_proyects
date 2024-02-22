import random


operators = ["+", "-", "*"]
min_number = 3
max_number = 10
total_calculos = 3

def calculos():
    izquierda = random.randint(min_number, max_number)
    derecha = random.randint(min_number, max_number)
    operador = random.choice(operators)

    operacion = str(izquierda) + " " + operador + " " + str(derecha)
    resultado = eval(operacion)
    return operacion, resultado


for i in range(total_calculos):
    operacion, resultado = calculos()
    while True:
        guess = input("Problem " + str(i + 1) + ": " + operacion + " = ")
        if guess == str(resultado):
            break