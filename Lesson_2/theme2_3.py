#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
    Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]

В этом случае ответ будет:
[5, 8]
'''

my_list_1 = [2, 2, 5, 12, 8, 2, 12]

# Вариант 1
numbers_dict = {}
# Считаем количество элементов в исходном списке
for num in my_list_1:
    if numbers_dict.get(num):
        numbers_dict[num] += 1
    else:
        numbers_dict[num] = 1

result_list = []
# Элементы встретившиеся один раз добавляем в итоговый список
for num, count in numbers_dict.items():
    if count == 1:
        result_list.append(num)

print('Вариант #1')
print('Исходный список:', my_list_1, sep='\n')
print('Уникальные элементы исходного списка:', result_list, sep='\n')

# Вариант 2
result_list = []
for num in my_list_1:
    if my_list_1.count(num) == 1:
        result_list.append(num)

print('Вариант #2')
print('Исходный список:', my_list_1, sep='\n')
print('Уникальные элементы исходного списка:', result_list, sep='\n')
