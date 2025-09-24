#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

# СТОЛ (две позиции на складе)
table_code = goods['Стол']

# Первая партия столов
table_item1 = store[table_code][0]
table_quantity1 = table_item1['quantity']
table_price1 = table_item1['price']
table_cost1 = table_quantity1 * table_price1

# Вторая партия столов  
table_item2 = store[table_code][1]
table_quantity2 = table_item2['quantity']
table_price2 = table_item2['price']
table_cost2 = table_quantity2 * table_price2

# Суммируем все партии
table_total_quantity = table_quantity1 + table_quantity2
table_total_cost = table_cost1 + table_cost2
print('Стол -', table_total_quantity, 'шт, стоимость', table_total_cost, 'руб')

# ДИВАН (две позиции на складе)
sofa_code = goods['Диван']

sofa_item1 = store[sofa_code][0]
sofa_quantity1 = sofa_item1['quantity']
sofa_price1 = sofa_item1['price']
sofa_cost1 = sofa_quantity1 * sofa_price1

sofa_item2 = store[sofa_code][1] 
sofa_quantity2 = sofa_item2['quantity']
sofa_price2 = sofa_item2['price']
sofa_cost2 = sofa_quantity2 * sofa_price2

sofa_total_quantity = sofa_quantity1 + sofa_quantity2
sofa_total_cost = sofa_cost1 + sofa_cost2
print('Диван -', sofa_total_quantity, 'шт, стоимость', sofa_total_cost, 'руб')

# СТУЛ (три позиции на складе)
chair_code = goods['Стул']

chair_item1 = store[chair_code][0]
chair_quantity1 = chair_item1['quantity']
chair_price1 = chair_item1['price']
chair_cost1 = chair_quantity1 * chair_price1

chair_item2 = store[chair_code][1]
chair_quantity2 = chair_item2['quantity'] 
chair_price2 = chair_item2['price']
chair_cost2 = chair_quantity2 * chair_price2

chair_item3 = store[chair_code][2]
chair_quantity3 = chair_item3['quantity']
chair_price3 = chair_item3['price']
chair_cost3 = chair_quantity3 * chair_price3

chair_total_quantity = chair_quantity1 + chair_quantity2 + chair_quantity3
chair_total_cost = chair_cost1 + chair_cost2 + chair_cost3
print('Стул -', chair_total_quantity, 'шт, стоимость', chair_total_cost, 'руб')
