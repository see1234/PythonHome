
import random 
import re
from random import randint
def Task1():
    my_sum=0
    my_array=MakeFillArray(int(re.sub("[^0-9]", "", input('Введите число: '))), False)
    result=[]
    i=0
    print(my_array)
    for arr in my_array:
        if i % 2 == 0:
            result.append(arr)
            my_sum+=arr
        i+=1
    print(result, my_sum)

    
def Task2():
    

   # Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

   # Пример:
   # - [2, 3, 4, 5, 6] => [12, 15, 16];
   # - [2, 3, 5, 6] => [12, 15]

    my_array=MakeFillArray(4, False)
    result=[]
    print(my_array)
    i=0
    for arr in my_array:
        if len(my_array)/2 <= i:
            break
        result.append(arr*my_array[len(my_array)-1-i])
        i+=1
    print(result)


def Task3():
    
    # Напишите программу, которая будет преобразовывать десятичное число в двоичное.

    # Пример:

    # - 45 -> 101101
    # - 3 -> 11
    # - 2 -> 10

    my_input=int(re.sub("[^0-9]", "", input('Введите число: ')))
    result=''
    while my_input > 0:
        result+=str(my_input%2)
        my_input = my_input // 2
    print(result[::-1])


def Task4():

    #Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

    #Пример:

    #- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

    my_array=MakeFillArray(int(re.sub("[^0-9]", "", input('Введите число: '))), True)
    a=0
    for i in my_array:
        my_array[a] = float(str(my_array[a]%1)[:4])
        a+=1
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


def Task5():

    #Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

    #Пример:

    #- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

    n = int(re.sub("[^0-9]", "", input('Введите число: ')))
    my_array = Fibonachi(n)
    print(Fibonachi(n))


def Fibonachi(n):
    n+=1
    fibarray = []
    numberA = 1
    numberB = 1
    for i in range(n-1):
        fibarray.append(numberA)
        savenum=numberA
        numberA = numberB
        numberB = savenum + numberB
    numberA = 0
    numberB = 1
    for i in range (n):
        fibarray.insert(0, numberA)
        savenum=numberA
        numberA = numberB
        numberB = savenum - numberB
    return fibarray
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
Task4()