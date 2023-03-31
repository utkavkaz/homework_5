"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random
random_number = random.randint(0, 100)
try:
    def my_func(n):
        m = int(input('Введте число от 0 до 100: '))
        if n == 0:
            if m == random_number:
                return print('Вы отгадали число!')
            else:
                return print(f'Загаданное число: {random_number}')
        if m == random_number:
            return print('Вы отгадали число!')
        else:
            if m > random_number:
                n -= 1
                print('Введенное число больше загаданного'), my_func(n)
            if m < random_number:
                n -= 1
                print('Введенное число меньше загаданного'), my_func(n)
    my_func(9)
except ValueError:
    print("Вы ввели не число!")
