import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_OPERATIONS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    operation = str(left)+ " " + operator + " " + str(right)
    answer = eval(operation)
    return operation, answer

input("Press enter to start!")
print ("----------------------")

start_time = time.time()
trys = 0
for i in range(TOTAL_OPERATIONS):
    operation, answer = generate_problem()
    while True:
        guess = input("Problem " + str(i + 1) + ": " + operation + " = ")
        if guess == str(answer):
            break
        else:
            trys += 1
end_time = time.time()
total_time = end_time - start_time
print ("----------------------")
print ("You finished in", total_time, "seconds", "with", trys, "try´s failed")
