# Задание#1
# Создайте переменную text со значением "Hello, Python!".
# Получите из переменной text срез "Hello".
# Получите срез "Python".
# Получите срез "lo, Pyt
#
text = "Hello, Python!"

slice_hello = text[0:5]  # Берём символы с 0 по 4 индекс (5 не включается)
slice_python = text[7:13]  # Берём символы с 7 по 12 индекс
slice_lo_pyt = text[3:10]  # Берём символы с 3 по 9 индекс
print(slice_hello)
print(slice_python)
print(slice_lo_pyt)




# - Задание#2
#
#     Создайте переменную `alphabet` со значением `"abcdefghijklmnopqrstuvwxyz"`.26
#
#     1. Получите срез от `alphabet`, включающий только первые 10 букв.
#     2. Получите срез от `alphabet`, включающий последние 5 букв.
#     3. Получите каждый второй символ от `alphabet`."
#
#

alphabet = "abcdefghijklmnopqrstuvwxyz"
slice_1 = alphabet[0:10]
slice_2 = alphabet[21:26]
slice_3 = alphabet[::2]

print(slice_1)
print(slice_2)
print(slice_3)
#     - Задание#3
#
#     Создайте переменную `reversed_text`, в которой будет строка `text`, но в обратном порядке (используйте слайсинг).
#
#     **Подсказка:** Используйте шаг `-1` для обратного среза.

reversed_text = "text"

reverse_slice = reversed_text[::-1]

print(reverse_slice)