
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
    my_input=int(re.sub("[^0-9]", "", input('Введите число: ')))
    result=''
    while my_input > 0:
        result+=str(my_input%2)
        my_input = my_input // 2
    print(result[::-1])
def Task4():
    my_array=MakeFillArray(int(re.sub("[^0-9]", "", input('Введите число: '))), True)
    print(my_array)
    numberMax = float('0.' + str(max(my_array)).split('.')[1])
    numberMin = float('0.' + str(min(my_array)).split('.')[1])
    difference=0
    if numberMax > numberMin:
        difference=round(numberMax-numberMin, 2)
    elif numberMax < numberMin:
        difference=round(numberMin-numberMax, 2)
    else:
        difference=0
    print(f'Min: {numberMin}, Max: {numberMax}, Difference: {difference}')
def Task5():
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
Task5()