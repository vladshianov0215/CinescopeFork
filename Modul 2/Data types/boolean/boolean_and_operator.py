#**Задания:**

#- **Задание #1**
#    1. Создайте две переменные: `has_ticket` и `has_passport`. Присвойте им значения `True` или `False`.
#   2. Создайте переменную `can_board_plane`, которая будет `True` только если обе переменные `has_ticket` и `has_passport` равны `True`.
#   3. Выведите результат `can_board_plane`.

# Создаём переменные
has_ticket = True
has_passport = True

# Переменная can_board_plane будет True, только если обе переменные равны True
can_board_plane = has_ticket and has_passport

# Выводим результат
print(can_board_plane)



#- **Задание #2**
#   1. Создайте переменные `is_adult` и `has_permission` и присвойте им значения `True` или `False`.
#  2. Создайте переменную `can_access_content`, которая будет равна `True` только если `is_adult` и `has_permission` оба равны `True`.
#  3. Измените значения переменных и проверьте, как это влияет на `can_access_content`.

is_adult = True
has_permission = True
can_access_content = is_adult and has_permission
print(can_access_content)
#- **Задание #3**
# 1. Напишите программу, которая принимает два числа от пользователя.
    #2. Проверьте, оба ли числа больше 10, и выведите результат. Используйте оператор `and` для проверки.
# 3. Объясните, что произойдёт, если хотя бы одно из чисел меньше или равно 10.

number = 10
number2 = 9

result_number = number >10 and number2 > 10

print(result_number)