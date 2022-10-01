# import random 
# import re
# from random import randint
# def Task1():
#     my_sum=0
#     my_array=MakeFillArray(int(re.sub("[^0-9]", "", input('Введите число: '))), False)
#     result=[]
#     i=0
#     print(my_array)
#     for arr in my_array:
#         if i % 2 == 0:
#             result.append(arr)
#             my_sum+=arr
#         i+=1
#     print(result, my_sum)
# def Task2():
#     my_array=MakeFillArray(4, False)
#     result=[]
#     print(my_array)
#     i=0
#     for arr in my_array:
#         if len(my_array)/2 <= i:
#             break
#         result.append(arr*my_array[len(my_array)-1-i])
#         i+=1
#     print(result)
# def Task3():
#     my_input=int(re.sub("[^0-9]", "", input('Введите число: ')))
#     result=''
#     while my_input > 0:
#         result+=str(my_input%2)
#         my_input = my_input // 2
#     print(result[::-1])
# def Task4():
#     my_array=MakeFillArray(int(re.sub("[^0-9]", "", input('Введите число: '))), True)
#     print(my_array)
#     numberMax = float('0.' + str(max(my_array)).split('.')[1])
#     numberMin = float('0.' + str(min(my_array)).split('.')[1])
#     difference=0
#     if numberMax > numberMin:
#         difference=round(numberMax-numberMin, 2)
#     elif numberMax < numberMin:
#         difference=round(numberMin-numberMax, 2)
#     else:
#         difference=0
#     print(f'Min: {numberMin}, Max: {numberMax}, Difference: {difference}')
# def Task5():
#     n = int(re.sub("[^0-9]", "", input('Введите число: ')))
#     my_array = Fibonachi(n)
#     print(Fibonachi(n))
# def Fibonachi(n):
#     n+=1
#     fibarray = []
#     numberA = 1
#     numberB = 1
#     for i in range(n-1):
#         fibarray.append(numberA)
#         savenum=numberA
#         numberA = numberB
#         numberB = savenum + numberB
#     numberA = 0
#     numberB = 1
#     for i in range (n):
#         fibarray.insert(0, numberA)
#         savenum=numberA
#         numberA = numberB
#         numberB = savenum - numberB
#     return fibarray
# def MakeFillArray(number, double):
#     array=[]
#     if not double:
#         while number != 0:
#             array.append(randint(1, 100))
#             number-=1
#         return array
#     else:
#         while number != 0:
#             array.append(randint(1, 1000)/100)
#             number-=1
#         return array
#Задания из 3 семинара
import re
import os
import random 
from random import randint

def Task1():
    sub = re.sub("[^0-9]", "", input('Введите число: ')) #Удаляем не нужные символы
    my_sum=0 #задаем счетчик подсчета суммы
    for text in sub: #Перебираем текст
        my_sum+=int(text) #добавляем в сумму цифру
    print(my_sum) #выводим итоговый результат
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
    array = [randint(1,100),randint(1,100),randint(1,100)]
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
        array.append(int_r((1 + 1 / i)**i))
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
#Задания из 2 семинара
#from math import sqrt


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
#     elif x < 0 and y > 0:
#         print('Позиция в 2 четверти')
#     elif x < 0 and y < 0:
#         print('Позиция в 3 четверти')
#     elif x > 0 and y < 0:
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
#     else:
#         print('x > 0, y < 0')


# def Task5():
#     print('Введите координаты A:')
#     xa = float(input('  X: '))
#     ya = float(input('  Y: '))
#     print("Введите координаты B:")
#     xb = float(input('  X: '))
#     yb = float(input('  Y: '))
#     print('Дистанция:', str(sqrt(((xa-xb)**2)+((ya-yb)**2)))[0:4])
#Задания из 1 семинара
 