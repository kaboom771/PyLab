#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

for city1, coordintaion1 in sites.items(): # возвращает в city1 - города по списку, coordination1 - координаты корода (x,y)
    distances[city1] = {} # словарь городов
    for city2, coordination2 in sites.items():
        if city1 != city2:
            distance = ((coordintaion1[0] - coordination2[0]) ** 2 + (coordintaion1[1] - coordination2[1]) ** 2) ** 0.5
            distances[city1][city2] = round(distance, 3)

print(distances)
