#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Создать модуль music_serialize.py.
В этом модуле определить словарь для вашей любимой музыкальной группы, например:

my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
вывести результаты в терминал. Записать результаты в файлы group.json,
group.pickle соответственно. В файле group.json указать кодировку utf-8.
'''
import json
import pickle
from pprint import pprint


my_favourite_group = {
    'name': 'Metallica',
    'tracks': ['Nothing Else Matters', 'Master Of Puppets'],
    'Albums': [{'name': 'Master Of Puppets', 'year': 1986},
               {'name': 'Garage Inc.', 'year': 1998}]
}

print('{:=^40}'.format(' Начальные данные '))
pprint(my_favourite_group)

print('{:=^40}'.format(' JSON '))
json_group = json.dumps(my_favourite_group)
pprint(json_group)

print('{:=^40}'.format(' PICKLE '))
pickle_group = pickle.dumps(my_favourite_group)
pprint(pickle_group)

# Записываем словарь в json файл
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

# Записываем словарь в pickle файл
with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
