#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from time import sleep

'''
Давайте усложним предыдущее задание. Измените сущности, 
добавив новый параметр — armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять 
и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
1. Наносит урон. Это улучшенная версия функции из задачи 3.
2. Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 
для вычисления урона и вычитания его из здоровья персонажа.

'''

def attack(person1, person2):
    '''
    Атакующая функция
    '''
    if choice([True, False, True]):
        received_damage = damage_calc(person1['damage'], person2['armor'])
        print('{pers1} нанес {dmg1} единиц урона {pers2}'.format(
            pers1=person1['name'], dmg1=received_damage, pers2=person2['name']
        ))
        person2['health'] -= received_damage
    else:
        print('{} промахнулся'.format(person1['name']))
    return person1, person2

def damage_calc(damage, armor):
    '''
    Функция вычисляющая урон
    '''
    return int(damage / armor)  # Для красоты округляем до целого числа


if __name__ == '__main__':
    player = {
        'health': 100, 'damage': 30, 'armor': 1.2
    }
    enemy = {
        'health': 140, 'damage': 20, 'armor': 1.2
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
