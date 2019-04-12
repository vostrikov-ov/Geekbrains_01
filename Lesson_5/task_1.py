#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке,
из которой запущен данный код. Затем создайте вторую функцию, удаляющую эти папки.
Проверьте работу функций в этом же модуле.
'''

import os


def make_dirs():
    # Функция создающая директории
    for num in range(1, 10):
        os.mkdir(f"dir_{num}")
    print('Директории созданы')


def rm_dirs():
    # Функция удаляющая директории
    for num in range(1, 10):
        os.rmdir(f"dir_{num}")
    print('Директории удалены')


if __name__ == '__main__':

    make_dirs()
    print(os.listdir())
    print('=' * 30)
    rm_dirs()
    print(os.listdir())
