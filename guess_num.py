"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

import random as rnd


def read():
    while True:
        inp = input('Guess number form 0 to 10^6 ')
        if inp != "exit" and inp != '':
            if not inp.isdigit():
                print('Error: not a number')
                continue
            if not (0 <= int(inp) <= 1000000):
                print('Error: not in range')
                continue
            else:
                return int(inp)
        else:
            print('exit')
            exit()


if __name__ == '__main__':
    desired_num = rnd.randint(0, 1000000)
    inp = read()
    while inp != desired_num:
        if inp > desired_num:
            print("Your number is bigger")
        else:
            print("Your number is smaller")
        inp = read()
    print(f"You are right! Number = {desired_num}")
