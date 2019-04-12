#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Создать модуль music_deserialize.py.
В этом модуле открыть файлы group.json и group.pickle,
прочитать из них информацию. Получить объект — словарь из предыдущего задания.
'''
import json
import pickle
from pprint import pprint


with open('group.json') as f:
    group_from_json = json.load(f)

print('{:=^40}'.format(' FROM JSON '))
pprint(group_from_json)

with open('group.pickle', 'rb') as f:
    group_from_pickle = pickle.load(f)

print('{:=^40}'.format(' FROM PICKLE '))
pprint(group_from_pickle)
