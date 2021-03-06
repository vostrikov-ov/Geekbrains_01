#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Создайте функцию, принимающую на вход имя, возраст и город проживания
человека. Функция должна возвращать строку вида
«Василий, 21 год(а), проживает в городе Москва»
'''

def person_info(name, age, city):
    '''
    Функция возвращающая персональные данные одной строкой
    '''
    return f'{name}, {age} год(а), проживает в городе {city}'


if __name__ == '__main__':

    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    city = input('Введите город проживания: ')

    print(person_info(name, age, city))
