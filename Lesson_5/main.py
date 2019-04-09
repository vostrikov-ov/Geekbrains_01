#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2,
сделайте импорт в main.py всех функций. Вызовите каждую функцию
в main.py и проверьте, что все работает как надо.

Примечание: Попробуйте импортировать как весь модуль целиком
(например из задачи 1), так и отдельные функции из модуля.
'''
import os

import task_1
from task_2 import random_element


if __name__ == '__main__':
    task_1.make_dirs()
    print(os.listdir())
    print('=' * 30)
    task_1.rm_dirs()
    print(os.listdir())
    print('=' * 30)

    base_list = ['aaa', 1, 10, 99, 'test']
    print(random_element(base_list))
    print(random_element([]))
