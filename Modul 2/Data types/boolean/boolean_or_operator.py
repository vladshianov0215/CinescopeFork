### **Задание #1**

#1. Создайте две переменные: `is_raining` и `has_umbrella`. Присвойте им значения `True` или `False`.
#2. Создайте переменную `can_go_outside`, которая будет `True` если либо `is_raining` равно `False`, либо `has_umbrella` равно `True`.
#3. Выведите результат `can_go_outside`.


is_raining = False

has_umbrella = False

can_go_outside = is_raining or has_umbrella

print(can_go_outside)
### **Задание #2**

#1. Создайте переменные `is_hungry` и `has_snack` и присвойте им значения `True` или `False`.
#2. Создайте переменную `can_eat_now`, которая будет равна `True` если `is_hungry` или `has_snack` равно `True`.
#3. Измените значения переменных и проверьте, как это влияет на `can_eat_now`.

is_hungry = True
has_snack = True
can_eat_now = is_hungry or  has_snack
print(can_eat_now)
### **Задание #3**

#1. Напишите программу, которая принимает от пользователя два числа.
#2. Проверьте, больше ли первое число 50 или второе число меньше 30, и выведите результат. Используйте оператор `or` для проверки.
#3. Измените введённые числа и проверьте, как это влияет на результат.

x = int(input("Введите первое число: "))
y = int(input("Введите втрое число: "))

result = x > 50 or y < 30


print(result)




