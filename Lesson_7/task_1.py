#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Даны два списка фруктов.
Получить список фруктов, присутствующих в обоих исходных списках.

    Примечание: Списки фруктов создайте вручную в начале файла.
'''

citrus_fruits = [
    'Апельсин', 'Лайм', 'Нони', 'Гуава', 'Помело'
]
exotic_fruits = [
    'Эшта', 'Гуанабана', 'Пепино', 'Нони', 'Карамбола', 'Гуава'
]

cross_fruits = [x for x in citrus_fruits if x in exotic_fruits]

print('{:#^50}'.format(' Исходные списки '))
print(citrus_fruits)
print(exotic_fruits)
print('{:#^50}'.format(' Пересечение списков '))
print(cross_fruits)
