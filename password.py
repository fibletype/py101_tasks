"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""
import re

if __name__ == '__main__':
    password = input('Enter password: ')
    if re.search('[A-Z]', password) and re.search('[a-z]', password) and \
        re.search('[0-9]', password) and len(password) >= 8:
        print('Strong password')
    else:
        print('Weak password')
