# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
        
import random
from random import Random, randint

num1 = randint(4, 9)
array1 = []

for i in range(num1):
    num2 = random.uniform(1, 9)
    array1.append(round(num2, 2))

num_max = array1[0]
num_min = array1[0]

for i in range(num1):
    if num_max < array1[i]:
        num_max = array1[i]
    if num_min > array1[i]:
        num_min = array1[i]

num_max -= int(num_max)
num_min -= int(num_min)

print(array1)

if num_max > num_min:
    summa = num_max - num_min
    print(round(summa, 2))
    
elif num_max < num_min:
    summa = num_min - num_max
    print(round(summa, 2))