#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Даны два произвольных списка. Удалите из первого списка элементы, присутствующие во втором.
    Примечание. Списки создайте вручную, например:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
'''

# Вариант 1
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for num in my_list_2:
    while num in my_list_1:
        my_list_1.remove(num)

print('Вариант 1:', my_list_1, sep='\n')

# Вариант 2
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

my_set_1 = set(my_list_1) - set(my_list_2)
my_list_1 = list(my_set_1)

print('Вариант 2:', my_list_1, sep='\n')
