#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Написать функцию, которая принимает на вход число от 1 до 100.
Если число равно 13, функция поднимает исключительную ситуации ValueError,
иначе возвращает введенное число, возведенное в квадрат.
Далее написать основной код программы. Пользователь вводит число.
Введенное число передаем параметром в написанную функцию и печатаем результат,
который она вернула. Обработать возможность возникновения исключительной
ситуации, которая поднимается внутри функции.
'''

def check_number(num):
    # Проверка числа на соответствие условиям и возведение его в степень
    if num == 13:
        raise ValueError('Введено несчастливое число 13!')
    elif (100 < num or 1 > num):
        raise ValueError('Введеное число выходит за указанные пределы')
    else:
        return num ** 2


if __name__ == '__main__':
    number = int(input('Введите число от 1 до 100: '))
    try:
        result = check_number(number)
        print('Квадратный корень введенного числа:', result)
    except ValueError as err_text:
        print(err_text)
