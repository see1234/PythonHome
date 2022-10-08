from itertools import groupby
import math
import re
import os
from random import randint
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
def MakeArrayRand(num):
    array = [randint(0,100) for i in range(num+1)]
    return array
def ReadFile(name):
    array=[]
    data = open(name + '.txt', 'r')
    for line in data:
        array.append(line)
    data.close()
    return array
def WriteFile(name, string):
    if os.path.isfile(name + '.txt'): 
        os.remove(name + '.txt') 
    with open(name + '.txt', 'w') as data:
        data.write(string)
        data.close()
def MnogoChlen(k):
    my_arraykoffient=MakeArrayRand(k)
    result=''
    while k != 0:
        if k != 1:
            result+=str(my_arraykoffient[k])+'x^' + str(k) + '+'
        else:
            result+=str(my_arraykoffient[k])+'x'
        k-=1
    result+='+' + str(my_arraykoffient[0]) + '=0'
    return result
def Task1(): 
    
    # Вычислить число c заданной точностью d

    # Пример:

    # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

    d = float(re.sub("[^0-9.]", "", input("Введите число пример: 0.001, чтобы поняла программа: ")))
    if math.pow(10, -1) >= d and d >= math.pow(10, -10):
        i=0
        result=''
        for st in str(d):
            result+=str(math.pi)[i]
            i+=1
        print(result)
    else:
        print('В задании: $10^{-1} ≤ d ≤10^{-10}$')
def Task2():
    
    # Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

    number = int(re.sub("[^0-9.]", "", input("Введите число: ")))
    savenumb=number
    mult = 2
    my_array = []
    while mult != number + 1:
        if number % mult == 0:
            my_array.append(mult)
            number //= mult
            mult = 2
        else:
            mult+=1
    print(my_array)
def Task3():
    my_array = MakeFillArray(10, False, 10) 
    print(my_array)
    result_array = []
    for i in my_array:
        if not i in result_array:
            result_array.append(i)
    print(result_array)
def Task4():
    k = int(re.sub("[^0-9.]", "", input("Введите натуральное число k: ")))
    if k <= 0:
        print('Ошибка')
        return
    WriteFile('result',MnogoChlen(k))
    WriteFile('result2',MnogoChlen(k))
    print('в txt')
def Task5():
    p1=ReadFile('result')[0].replace('=0', '')
    p2=ReadFile('result2')[0].replace('=0', '')
    my_arr4=[]
    my_arr5=[]
    for i in p1.split('+'):
        if not 'x^' in i and not 'x' in i:
            my_arr4.append((int(i),1))
        elif 'x' in i and not 'x^' in i:
            my_arr4.append((int(i.replace('x','')),0))
        else:
            my_arr4.append((int(int(i.split('x^')[0])),int(i.split('x^')[-1])))
    for i in p2.split('+'):
        if not 'x^' in i and not 'x' in i:
            my_arr5.append((int(i),1))
        elif 'x' in i and not 'x^' in i:
            my_arr5.append((int(i.replace('x','')),0))
        else:
            my_arr5.append((int(int(i.split('x^')[0])),int(i.split('x^')[-1])))
    my_arr=(add_poly(my_arr4, my_arr5))
    result=''
    for i in my_arr:
        primer=str(i).replace(')','').replace('(','').replace(' ','').split(',')
        if int(primer[1]) == 0:
            result+=primer[0]+'+'
        elif int(primer[1]) == 1:
            result+=primer[0]+'x+'
        else:
            result+=primer[0]+'x^'+primer[1]+'+'
    print(result[:-1])
 
def add_poly(*args):
    expval = sorted([(e, v) for poly in args for v, e in poly])
    return [
        (sum(v for _, v in g), e)
        for e, g in groupby(expval, key=lambda kv: kv[0])
    ]
