# #- Задание#5
#
#     Создайте переменную `text` со значением `"hElLo, PyThOn!"`.
#
#     1. Примените к `text` метод `lower()` и сохраните результат в переменную `text_lower`. Проверьте результат.
#     2. Примените к `text` метод `upper()` и сохраните результат в переменную `text_upper`. Проверьте результат.

text = "hElLo, PyThOn!"
text_lover = text.lower()
text_upper = text.upper()

print(text_lover)
print(text_upper)


# - Задание#5.1
#
#     Создайте переменную `sentence` со значением `"this is a test sentence."`.
#
#     1. Примените к `sentence` метод `capitalize()` и сохраните результат в переменную `sentence_cap`. Проверьте результат.
#     2. Примените к `sentence` метод `title()` и сохраните результат в переменную `sentence_title`. Проверьте результат.

sentence = "this is a test sentence."
sentence_cap = sentence.capitalize()
sentence_title = sentence.title()
print(sentence_cap)
print(sentence_title)

# - Задание#5.2
#
#     Создайте переменную `mixed_case` со значением `"PYTHON programming IS Fun"`.
#
#     1. Используйте методы, чтобы сделать всю строку `mixed_case` строчной (`lower()`), а затем — заглавной (`upper()`).
#     2. Примените `capitalize()` к `mixed_case` и посмотрите, что произойдёт.
#
# # Создаём переменную mixed_case
# mixed_case = "PYTHON programming IS Fun"
#
# # 1. Применяем метод lower(), чтобы сделать строку строчной
# lower_case = mixed_case.lower()
#
# # Применяем метод upper(), чтобы сделать строку заглавной
# upper_case = mixed_case.upper()
#
# # 2. Применяем метод capitalize(), чтобы сделать первую букву заглавной, а остальные строчными
# capitalized_case = mixed_case.capitalize()
#
# # Выводим результаты
# print("Строчная строка (lower):", lower_case)
# print("Заглавная строка (upper):", upper_case)
# print("Capitalize:", capitalized_case)




# Создаём переменную mixed_case
mixed_case = "PYTHON programming IS Fun"

# Применяем все методы и выводим их результаты через один print
print(
    f"Строчная строка (lower): {mixed_case.lower()}\n"
    f"Заглавная строка (upper): {mixed_case.upper()}\n"
    f"Capitalize: {mixed_case.capitalize()}"
)
