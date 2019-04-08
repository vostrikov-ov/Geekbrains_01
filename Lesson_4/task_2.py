#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Создайте функцию, принимающую на вход 3 числа
и возвращающую наибольшее из них.
'''

# Вариант 1
def find_max(num1, num2, num3):
    '''
    Функция возвращающая наибольшее число из трех
    '''
    nums_list = [num1, num2, num3]
    return max(nums_list)

# Вариант 2
def find_max_2(*nums):
    '''
    Функция возвращает наибольшее число
    '''
    return max(nums)

if __name__ == '__main__':
    # Запрашиваем три числа
    num1 = int(input('Введите число #1: '))
    num2 = int(input('Введите число #2: '))
    num3 = int(input('Введите число #3: '))
    print('Вариант #1')
    max_num = find_max(num1, num2, num3)
    print('Наибольшее число из введенных - {}'.format(max_num))

    print('Вариант #2')
    max_num = find_max_2(num1, num2, num3)
    print(f'Наибольшее число из введенных - {max_num}')

# Вариант 3
def find_max_3(nums):
    '''
    Функция возвращает наибольшее число
    '''
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[0]

if __name__ == '__main__':
    # Запрашиваем количество чисел
    nums_count = int(input('Введите количество цифр: '))
    nums_list = []
    for x in range(nums_count):
        nums_list.append(int(input('Введите число: ')))

    max_num = find_max_3(nums_list)
    print(f'Наибольшее число из введенных - {max_num}')
