import re
import os
import random 
from random import randint


def Task1():
    sub = re.sub("[^0-9]", "", input('Введите число: ')) #Удаляем не нужные символы
    sum=0 #задаем счетчик подсчета суммы
    for text in sub: #Перебираем текст
        sum+=int(text) #добавляем в сумму цифру
    print(sum) #выводим итоговый результат
def Task2():
    sub = re.sub("[^0-9]", "", input('Введите число: ')) #Удаляем не нужные символы
    n=int(sub)
    print(ReturningABeautifulText(n, True), ReturningABeautifulText(n, False))
def Task3():
    sub = re.sub("[^0-9]", "", input('Введите число: '))
    n=int(sub)
    print(lim(n))
    print(round(sum(lim(n)),1))
def Task4():
    sub = re.sub("[^0-9]", "", input('Введите число: '))
    n=int(sub)
    fillarray = FillArrayN(n)
    array = [randint(-n, n), randint(-n, n),randint(-n, n)]
    WriteFile('file', array)
    readarray = ReadFile('file')
    print('Рандомный массив записывается в фаил:',array)
    print('Заполненный массив:',fillarray)
    print('Массив из фаила:', readarray)
    print('Итог:', getMult(fillarray, readarray))
def Task5():
    array = [1, 4, 5, 6]
    print(array)
    print(Algorithm(array))
    
def Algorithm(array):
    for i in range(len(array)-1, 0, -1):
        j = random.randint(0, i + 1) 
        array[i], array[j] = array[j], array[i]  
    return array
def getMult(filledarray, readedarray):
    mult=1
    for i in readedarray:
        mult*=int(filledarray[i])
    return mult
def FillArrayN(n):
    array=[]
    i=n+1
    n=-n
    while n != i:
        array.append(n)
        n+=1
    return array
def ReadFile(name):
    array=[]
    data = open(name + '.txt', 'r')
    for line in data:
        array.append(int(line))
    data.close()
    return array
def WriteFile(name, array):
    if os.path.isfile(name + '.txt'): 
        os.remove(name + '.txt') 
    with open(name + '.txt', 'w') as data:
        for i in array:
            data.write(str(i) + '\n')
        data.close()
def lim(n):
    i=1
    array=[]
    while i != n + 1:
        if(i != 1):
            array.append(round(((1 + 1 / i)**i + array[i-2]),2))
        else:
            array.append((1 + 1 / i)**i)
        i+=1
    return array   
def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
def Factorial(number):
    result=1
    while number != 0:
        result*=number
        number-=1
    return str(result)
def FactorialString(number, NeedAnExample):
    if NeedAnExample == False:
        return Factorial(number)
    if number <= 0:
        return 'Ошибка...'
    i=1
    result=""
    while i != number:
        result+=str(i) + '*'
        i+=1
    result+=str(i)
    return result
def ReturningABeautifulText(n, AnExampleIsNeeded):
    i=n+1
    n=1
    if AnExampleIsNeeded:
        result='('
        while n != i:
            result+=FactorialString(n, True) + ', '
            n+=1
        result=result[:-2] + ')'
        return result
    else:
        result='[ '
        while n != i:
            result+=FactorialString(n, False) + ', '
            n+=1
        result=result[:-2] + ' ]'
        return result
Task3()
# from math import sqrt


# def Task1():
#     day = int(input())
#     if day == 6 or day == 7:
#         print('да')
#     else:
#         print('нет')


# def Task2():
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 boolean = not (x or y or z) == (not x and not y and not z)
#                 print(boolean, x, y, z)


# def Task3():
#     x = int(input('Напишите координату X: '))
#     y = int(input('Напишите координату Y: '))
#     if x > 0 and y > 0:
#         print('Позиция в 1 четверти')
#     if x < 0 and y > 0:
#         print('Позиция в 2 четверти')
#     if x < 0 and y < 0:
#         print('Позиция в 3 четверти')
#     if x > 0 and y < 0:
#         print('Позиция в 4 четверти')


# def Task4():
#     n = int(input('Введите четверть: '))
#     if n < 1 or n > 4:
#         print('А четверть такая существует?')
#         return
#     if n == 1:
#         print('x > 0, y > 0')
#     elif (n == 2):
#         print('x < 0, y > 0')
#     elif (n == 3):
#         print('x < 0, y < 0')
#     elif (n == 4):
#         print('x > 0, y < 0')


# def Task5():
#     print('Введите координаты A:')
#     Xa = float(input('  X: '))
#     Ya = float(input('  Y: '))
#     print("Введите координаты B:")
#     Xb = float(input('  X: '))
#     Yb = float(input('  Y: '))
#     print('Дистанция:', round(sqrt(((Xa-Xb)**2)+((Ya-Yb)**2)), 3))
#Задания из 1 семинара

