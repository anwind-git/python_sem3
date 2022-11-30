# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите число: '))
 
num = ''
 
while number > 0:
    num = str(number % 2) + num
    number //= 2
 
print(num)