from time import sleep

# Función para realizar la operación matemática
def operate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        print("El signo que has introducido es incorrecto")
        return None

number1 = input("Introduce el primer número: ")
math_operator = input("Qué quieres hacer (+, -, * o /):")
number2 = input("Introduce el segundo número: ")

additional_operation = input("¿Necesitas entrar más números o símbolos? (Si/No): ")

# Inicializar listas para números y operadores
numbers = [int(number1), int(number2)]
operators = [math_operator]

# Question for know if he need more lines
if additional_operation == 'Si' or additional_operation == 'Yes':
    extra_things = input("¿Cuántas cosas más quieres agregar (2, 3, 4, 5)?: ")

    # Conditionals for add new lines
    if extra_things == '2':
        zero_extra = input("Introduce el segundo símbolo que quieras añadir (+ , - * o /): ")
        one_extra = input("Introduce el tercer número que quieras añadir: ")
        operators.append(zero_extra)
        numbers.append(int(one_extra))
    elif extra_things == '3':
        zero_extra = input("Introduce el segundo símbolo que quieras añadir (+ , - * o /): ")
        sleep(1)
        one_extra = input("Introduce el tercer número que quieras añadir: ")
        sleep(1)
        two_extra = input("Introduce el tercer símbolo que quieras añadir (+ , - * o /): ")
        operators.append(zero_extra)
        numbers.append(int(one_extra))
        operators.append(two_extra)
    elif extra_things == '4':
        zero_extra = input("Introduce el segundo símbolo que quieras añadir (+ , - * o /): ")
        sleep(1)
        one_extra = input("Introduce el tercer número que quieras añadir: ")
        sleep(1)
        two_extra = input("Introduce el tercer símbolo que quieras añadir (+ , - * o /): ")
        sleep(1)
        three_extra = input("Introduce el cuarto número que quieras añadir: ")
        operators.append(zero_extra)
        numbers.append(int(one_extra))
        operators.append(two_extra)
        numbers.append(int(three_extra))
    elif extra_things == '5':
        zero_extra = input("Introduce el segundo símbolo que quieras añadir (+ , - * o /): ")
        sleep(1)
        one_extra = input("Introduce el tercer número que quieras añadir: ")
        sleep(1)
        two_extra = input("Introduce el tercer símbolo que quieras añadir (+ , - * o /): ")
        sleep(1)
        three_extra = input("Introduce el cuarto número que quieras añadir: ")
        sleep(1)
        four_extra = input("Introduce el cuarto símbolo que quieras añadir (+ , - * o /): ")
        sleep(1)
        five_extra = input("Introduce el quinto número que quieras añadir: ")
        operators.append(zero_extra)
        numbers.append(int(one_extra))
        operators.append(two_extra)
        numbers.append(int(three_extra))
        operators.append(four_extra)
        numbers.append(int(five_extra))
    else:
        print("Lo que acabas de introducir es incorrecto")

# Conditionals for operate
if math_operator == '+':
    sum_result = print(int(number1) + int(number2))
elif math_operator == '-':
    substraction_result = print(int(number1) - int(number2))
elif math_operator == '*':
    multiplicator_result = print(int(number1) * int(number2))
elif math_operator == '/':
    divide_result = print(int(number1) / int(number2))
else:
    print("El signo que has introducido es incorrecto")

# Logic for operate all
result = numbers[0]
for i in range(1, len(numbers)):
    result = operate(result, operators[i-1], numbers[i])

print(f"El resultado final es: {result}")
