import math
from random import randint

def multi(number):
    multipliers = []
    for i in range(3,number + 1):
        if number % i == 0:
            multipliers.append(i)
    return multipliers

def print_(list_):
    for i in list_:
        print(i, end=' ')

first_number = randint(3,20)
print('Число на первой табличке:', first_number)

multipliers = multi(first_number)
print('Множители данного числа:', end=' ')
print_(multipliers)
print()


pairs = []
for multi_ in multipliers:
    for first_in_pair in range(1, math.floor(multi_ / 2) + 1):
        if multi_ - first_in_pair != first_in_pair:
            pairs.append([first_in_pair, multi_ - first_in_pair])

print('Пары:', end=' ')
print_(pairs)