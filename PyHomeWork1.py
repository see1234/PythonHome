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
    elif x < 0 and y > 0:
        print('Позиция в 2 четверти')
    elif x < 0 and y < 0:
        print('Позиция в 3 четверти')
    elif x > 0 and y < 0:
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
    else:
        print('x > 0, y < 0')


def Task5():
    print('Введите координаты A:')
    xa = float(input('  X: '))
    ya = float(input('  Y: '))
    print("Введите координаты B:")
    xb = float(input('  X: '))
    yb = float(input('  Y: '))
    print('Дистанция:', str(sqrt(((xa-xb)**2)+((ya-yb)**2)))[0:4])