from math import sqrt


def Task1():
    day = int(input())
    if day == 6 or day == 7:
        print('да')
    else:
        print('нет')


def Task2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                boolean = not (x or y or z) == (not x and not y and not z)
                print(boolean, x, y, z)


def Task3():
    x = int(input('Напишите координату X: '))
    y = int(input('Напишите координату Y: '))
    if x > 0 and y > 0:
        print('Позиция в 1 четверти')
    if x < 0 and y > 0:
        print('Позиция в 2 четверти')
    if x < 0 and y < 0:
        print('Позиция в 3 четверти')
    if x > 0 and y < 0:
        print('Позиция в 4 четверти')


def Task4():
    n = int(input('Введите четверть: '))
    if n < 1 or n > 4:
        print('А четверть такая существует?')
        return
    if n == 1:
        print('x > 0, y > 0')
    elif (n == 2):
        print('x < 0, y > 0')
    elif (n == 3):
        print('x < 0, y < 0')
    elif (n == 4):
        print('x > 0, y < 0')


def Task5():
    print('Введите координаты A:')
    Xa = float(input('  X: '))
    Ya = float(input('  Y: '))
    print("Введите координаты B:")
    Xb = float(input('  X: '))
    Yb = float(input('  Y: '))
    print('Дистанция:', round(sqrt(((Xa-Xb)**2)+((Ya-Yb)**2)), 3))


Task5()
