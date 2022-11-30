# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = int(input('Введите число: '))
fibo = [0]

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

for i in range(1, number + 1):
    fibo.append(Fibonacci(i))
    fibo.insert(0, NegaFibonacci(i))
print(fibo)