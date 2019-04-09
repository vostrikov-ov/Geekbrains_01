#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Создайте модуль. В нем создайте функцию, которая принимает список и
возвращает из него случайный элемент. Если список пустой, функция
должна вернуть None. Проверьте работу функций в этом же модуле.

    Примечание: Список для проверки введите вручную.
    Или возьмите этот: [1, 2, 3, 4]
'''

from random import choice


def random_element(ingress_list):
    # Функция возвращающая случайный элемент списка
    return choice(ingress_list) if ingress_list else None


if __name__ == '__main__':
    base_list = [1, 2, 3, 4]
    print(random_element(base_list))
    print(random_element([]))
