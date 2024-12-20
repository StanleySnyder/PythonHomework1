"""
n = int(input('Введите количество чисел в последовательности: '))

count = 0

for i in range(n):
    number = int(input('Введите очередное число: '))

    if number > 1:
        for divider in range(2, number):
            if number % divider == 0:
                break
    else:
        count += 1
print('Количество простых чисел:', count)
"""


# Запрос количества чисел в последовательности
n = int(input('Введите количество чисел в последовательности: '))
# Инициализация счётчика простых чисел
count = 0
# Основной цикл для ввода чисел
for i in range(n):
    # Запрос очередного числа от пользователя
    number = int(input('Введите очередное число: '))
    # Проверка числа на простоту
    if number > 1:  # Простые числа больше 1
        for divider in range(2, int(number ** 0.5) + 1):  # Проверка до корня из числа
            # Если число делится на divider, оно не является простым
            if number % divider == 0:
                break
        else:
            # Если цикл завершился без break, число простое
            count += 1
# Вывод количества простых чисел в последовательности
print('Количество простых чисел:', count)
