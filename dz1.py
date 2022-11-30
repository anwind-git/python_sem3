# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import Random, randint

array = []
summa = 0

for i in range(5):
    array.append(randint(1, 10))
    if i % 2 != 0:
        summa += array[i]


print(f"Список из нескольких чисел {array}")
print(f"Сумму элементов списка, стоящих на нечётной позиции {summa}")