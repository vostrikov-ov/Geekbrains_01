#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from time import sleep

'''
Давайте опишем пару сущностей player и enemy через словарь,
который будет иметь ключи и значения:

    name — строка, полученная от пользователя,
    health = 100,

    damage = 50.
    Поэкспериментируйте с значениями урона и жизней по желанию.
    Теперь надо создать функцию attack(person1, person2).

    Примечание: имена аргументов можете указать свои.

    Функция в качестве аргумента будет принимать атакующего и атакуемого.
    В теле функция должна получить параметр damage атакующего и отнять
    это количество от health атакуемого. Функция должна сама работать
    со словарями и изменять их значения.
'''

def attack(person1, person2):
    '''
    Атакующая функция
    '''
    if choice([True, True, False]):
        print('{pers1} нанес {dmg1} единиц урона {pers2}'.format(
            pers1=person1['name'], dmg1=person1['damage'], pers2=person2['name']
        ))
        person2['health'] -= person1['damage']
    else:
        print('{} промахнулся'.format(person1['name']))
    return person1, person2


if __name__ == '__main__':
    player = {
        'health': 100, 'damage': 30
    }
    enemy = {
        'health': 140, 'damage': 20
    }
    player['name'] = input('Введите имя игрока: ')
    enemy['name'] = input('Введите имя противника: ')

    print('{:=^35}'.format(' БОЙ НАЧИНАЕТСЯ '))
    counter = 1
    while player['health'] > 0 and enemy['health'] > 0:
        if counter % 2 != 0:
            player, enemy = attack(player, enemy)
        else:
            enemy, player = attack(enemy, player)
        counter += 1
        sleep(1)
    else:
        print('{:=^35}'.format(' БОЙ ОКОНЧЕН '))
        if player['health'] > 0:
            print(f"{player['name']} одержал победу!")
        else:
            print(f"{enemy['name']} одержал победу!")
