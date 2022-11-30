# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import Random, randint
import math

num = randint(4, 8)
array1 = []
array2 = []
summa = 0

for i in range(num):
    array1.append(randint(1, 9))

for i in range(math.ceil(num / 2)):
    summa = array1[i] * array1[(num - 1) - i]
    array2.append(summa)

print(array1)
print(array2)