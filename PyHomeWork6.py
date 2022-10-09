from itertools import groupby
import math
import re
import os
from random import randint

def TaskUseLambda():
    # Вычислить число c заданной точностью d

    # Пример:

    # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

    # - Задача из семинара 4

    d = float(re.sub("[^0-9.]", "", input("Введите число пример: 0.001, чтобы поняла программа: ")))
    if math.pow(10, -1) >= d and d >= math.pow(10, -10):  
        get_number_with_d=lambda b: str(math.pi)[:len(b)]
        print(get_number_with_d(str(d)))
    else:
        print('В задании: $10^{-1} ≤ d ≤10^{-10}$')
#TaskUseLambda() #Задача с lambda


arr2=[]
def TaskUseFilter():

    # Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
  
    # - Задача из семинара 4

    my_array = MakeFillArray(10, False, 10) 
    print(my_array)
    print(list(filter(deleteNextNumbers, my_array)))
def deleteNextNumbers(i):
    if i in arr2:
        return False
    else:
        arr2.append(i)
    return True
def MakeFillArray(number, double, max):
    array=[]
    if not double:
        while number != 0:
            array.append(randint(1, max))
            number-=1
        return array
    else:
        while number != 0:
            array.append(randint(1, max * 10)/100)
            number-=1
        return array
def MakeFillArray(number, double):
    array=[]
    if not double:
        while number != 0:
            array.append(randint(1, 100))
            number-=1
        return array
    else:
        while number != 0:
            array.append(randint(1, 1000)/100)
            number-=1
        return array
#TaskUseFilter() #Задача с list и filter


def TaskUseEnumerate():

    #Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

    #Пример:

    #- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

    my_array=MakeFillArray(int(re.sub("[^0-9]", "", input('Введите число: '))), True)
    for val, i in enumerate(my_array, start=0):
        my_array[val] = float(str(i%1)[:4])
    print(my_array)
    numberMax = max(my_array)
    numberMin = min(my_array)
    difference=0
    if numberMax > numberMin:
        difference=round(numberMax-numberMin, 2)
    elif numberMax < numberMin:
        difference=round(numberMin-numberMax, 2)
    else:
        difference=0
    print(f'Min: {numberMin}, Max: {numberMax}, Difference: {difference}')
#TaskUseEnumerate() #Задача с enumerate, полезная штука


def TaskUseListMapLambdaAndZip():
    sub = re.sub("[^0-9]", "", input('Введите число: ')) #Удаляем не нужные символы
    n=int(sub)
    print(list(zip(FactorialString(n), Factorial(n))))


def FactorialString(number):
    res=range(1,number+1)
    result=list(map(lambda number: factstr(number), res))
    return result
def Factorial(number):
    res=range(1,number+1)
    result=list(map(lambda number: fact(number), res))
    return result
def fact(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
def factstr(n):
    fact = '1'
    for num in range(2, n + 1):
        fact += '*' + str(num)
    return fact
TaskUseListMapLambdaAndZip() #Задача с ламбадой и мапом и тд и зипом

def TaskUseListComprehension():
    #Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
    sub = re.sub("[^0-9]", "", input('Введите число: '))
    n=int(sub)
    print(lim(n))
    print(round(sum(lim(n)),2))
def lim(n):
    array=[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]
    return array   
#TaskUseListComprehension() #Задача с list comprehension