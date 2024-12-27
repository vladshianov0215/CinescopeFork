a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /, %, //, **): ")

# Калькулятор
if operation == "+":
    print("Результат:", a + b)
elif operation == "-":
    print("Результат:", a - b)
elif operation == "*":
    print("Результат:", a * b)
elif operation == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Ошибка: Деление на 0")
elif operation == "%":
    print("Результат:", a % b)
elif operation == "//":
    print("Результат:", a // b)
elif operation == "**":
    print("Результат:", a ** b)
else:
    print("Ошибка: Неверная операция")