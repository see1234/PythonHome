
from random import *
import time
 
def Task1():

    my_input = input("Введите текст:\n")
    print(f"Текст: {my_input}")
    my_array = []
    for i in my_input.split("абв"):
        if "абв" not in i:
            my_array.append(i)
    print(f'Результат: {"".join(my_array)}')


def Task2():
    print('ВАС ПРИВЕСТВУЕТ ИГРА, ОТЖМИ КОНФЕТЫ У ДРУГА ИЛИ У КОМПЬЮТЕРА')
    print('ВЫБЕРИТЕ БОТ ИЛИ ДВА ИГРОКА') 
    print('НУЖНО НАПИСАТЬ ЛИБО 0, ЛИБО 1')
    print('0 - БОТ, 1 - ДВА ИГРОКА')
    my_input = input()
    while my_input != '0' or my_input != '1':
        if my_input == '0':
            PlayerVsPlayer()
            break
        else:
            PlayerVsBot()
            break


def Task3():
    print('ВАС ПРИВЕСТВУЕТ ИГРА КРЕСТИКИ НОЛИКИ')
    print('ВЫБЕРИТЕ БОТ ИЛИ ДВА ИГРОКА') 
    print('НУЖНО НАПИСАТЬ ЛИБО 0, ЛИБО 1')
    print('0 - БОТ, 1 - ДВА ИГРОКА')
    my_input = input()
    while my_input != '0' or my_input != '1':
        if my_input == '1':
            PlayerVsPlayerOX()
            break
        else:
            PlayerVsBotOX()
            break


def Task4():
    my_input=input()
    print(rle(my_input))
    print(decode_rle(rle(my_input)))


def PlayerVsPlayerOX():
    my_array=[[1,2,3], [4,5,6], [7,8,9]]
    for i in my_array:
        print(i)
    print('Ходи')
    b=0
    while True:
        if b % 2 == 0:
            PlayerMoveOne(my_array)
            for i in my_array:
                print('Игрок №1:',i)
            stop=True
            for i in my_array:
                for j in i:
                    try:
                        o=int(j)
                        stop=False
                    except:
                        p=0
            if stop == True:
                print('Ничья')
                break
            print('Игрок №2 ходи')
        else:
            PlayerMoveTwo(my_array)
            for i in my_array:
                print('Игрок №2:',i)
            stop=True
            for i in my_array:
                for j in i:
                    try:
                        o=int(j)
                        stop=False
                    except:
                        p=0
            if stop == True:
                print('Ничья')
                break
            print('Игрок №1 ходи')

        b+=1
        my_arr2=[]
        my_arr3=[]
        a=0
        for i in my_array:
            for j in i:
                a+=1
                if j == 'X':
                    my_arr2.append(a)
                elif j == 'O':
                    my_arr3.append(a)
        if WhoWinPlayerVsPlayer(my_arr2, my_arr3) == True:
           break


def PlayerVsBotOX():
    my_array=[[1,2,3], [4,5,6], [7,8,9]]
    for i in my_array:
        print(i)
    print('Ходи')
    b=0
    while True:
        if b % 2 == 0:
            PlayerMove(my_array)
            for i in my_array:
                print('ВЫ:',i)
            stop=True
            for i in my_array:
                for j in i:
                    try:
                        o=int(j)
                        stop=False
                    except:
                        p=0
            if stop == True:
                print('Ничья')
                break
        else:
            BotMove(my_array)
            for i in my_array:
                print('БОТ:',i)
            stop=True
            for i in my_array:
                for j in i:
                    try:
                        o=int(j)
                        stop=False
                    except:
                        p=0
            if stop == True:
                print('Ничья')
                break
            print('Бот ответил, теперь вы')
        b+=1
        my_arr2=[]
        my_arr3=[]
        a=0
        for i in my_array:
            for j in i:
                a+=1
                if j == 'X':
                    my_arr2.append(a)
                elif j == 'O':
                    my_arr3.append(a)
        if WhoWinPlayerVsBot(my_arr2, my_arr3) == True:
           break

        
def WhoWinPlayerVsPlayer(player_array, bot_array):
    my_winarray=[[1,2,3], [2,5,7], [1,5,9], [3,5,7], [1,4,7], [3,6,9], [7,8,9], [3,4,5]]
    player_array.sort()
    bot_array.sort()
    numberB=0
    for i in my_winarray:
        numberA=0
        for j in i:
            for k in player_array:
                if k == j:
                    numberA+=1
                if numberA == 3:
                    print('WIN PLAYER №1')
                    return True
    for i in my_winarray:
        numberB=0
        for j in i:
            for k in bot_array:
                if j == k:
                    numberB+=1
                if numberB == 3:
                    print('WIN PLAYER №2')
                    return True
    return False
def WhoWinPlayerVsBot(player_array, bot_array):
    my_winarray=[[1,2,3], [1,5,9], [2,5,7], [3,5,7], [1,4,7], [3,6,9], [7,8,9], [3,4,5]]
    player_array.sort()
    bot_array.sort()
    numberB=0
    for i in my_winarray:
        numberA=0
        for j in i:
            for k in player_array:
                if k == j:
                    numberA+=1
                if numberA == 3:
                    print('WIN PLAYER')
                    return True
    for i in my_winarray:
        numberB=0
        for j in i:
            for k in bot_array:
                if j == k:
                    numberB+=1
                if numberB == 3:
                    print('WIN BOT')
                    return True
    return False

def BotMove(my_array):
    bot_input=randint(1,10)
    print('Бот думает...')
    time.sleep(randint(0,2))
    if bot_input < 4:
        if my_array[0][bot_input-1] != 'O' and my_array[0][bot_input-1] != 'X':   
            my_array[0][bot_input-1] = 'O'
        else:
            BotMove(my_array)
    elif bot_input < 7:
        if my_array[1][bot_input-4] != 'O' and my_array[1][bot_input-4] != 'X':   
            my_array[1][bot_input-4] = 'O'
        else:
            BotMove(my_array)
    elif bot_input < 10:
        if my_array[2][bot_input-7] != 'O' and my_array[2][bot_input-7] != 'X':   
            my_array[2][bot_input-7] = 'O'
        else:
            BotMove(my_array)
def PlayerMove(my_array):
    my_input=int(input())
    if my_input < 4:
        if my_array[0][my_input-1] != 'O' and my_array[0][my_input-1] != 'X':   
            my_array[0][my_input-1] = 'X'
        else:
            print('уже заполнена')
            PlayerMove(my_array)
    elif my_input < 7:
        if my_array[1][my_input-4] != 'O' and my_array[1][my_input-4] != 'X':   
            my_array[1][my_input-4] = 'X'
        else:
            print('уже заполнена')
            PlayerMove(my_array)
    elif my_input < 10:
        if my_array[2][my_input-7] != 'O' and my_array[2][my_input-7] != 'X':   
            my_array[2][my_input-7] = 'X'
        else:
            print('уже заполнена')
            PlayerMove(my_array)
def PlayerMoveOne(my_array):
    my_input=int(input())
    if my_input < 4:
        if my_array[0][my_input-1] != 'O' and my_array[0][my_input-1] != 'X':   
            my_array[0][my_input-1] = 'X'
        else:
            print('уже заполнена')
            PlayerMoveOne(my_array)
    elif my_input < 7:
        if my_array[1][my_input-4] != 'O' and my_array[1][my_input-4] != 'X':   
            my_array[1][my_input-4] = 'X'
        else:
            print('уже заполнена')
            PlayerMoveOne(my_array)
    elif my_input < 10:
        if my_array[2][my_input-7] != 'O' and my_array[2][my_input-7] != 'X':   
            my_array[2][my_input-7] = 'X'
        else:
            print('уже заполнена')
            PlayerMoveOne(my_array)


def PlayerMoveTwo(my_array):
    my_input=int(input())
    if my_input < 4:
        if my_array[0][my_input-1] != 'O' and my_array[0][my_input-1] != 'X':   
            my_array[0][my_input-1] = 'O'
        else:
            print('уже заполнена')
            PlayerMoveTwo(my_array)
    elif my_input < 7:
        if my_array[1][my_input-4] != 'O' and my_array[1][my_input-4] != 'X':   
            my_array[1][my_input-4] = 'O'
        else:
            print('уже заполнена')
            PlayerMoveTwo(my_array)
    elif my_input < 10:
        if my_array[2][my_input-7] != 'O' and my_array[2][my_input-7] != 'X':   
            my_array[2][my_input-7] = 'O'
        else:
            print('уже заполнена')
            PlayerMoveTwo(my_array)


def PlayerVsPlayer():
    total_candy = 2021
    max_take=28
    array_playernames = [input('Введите ваше имя игрок №1: '),input('Введите ваше имя игрок №2: ')]
    vs = randint(0, 1)
    while True:
        vs+=1
        candy=LimitCandyPickupPlayer(vs,array_playernames, max_take,total_candy)
        if candy > total_candy:
            print(f'Игрок {array_playernames[vs%2]} слишком много конфет просите!!!')
            candy=LimitCandyPickupPlayer(vs,array_playernames, max_take,total_candy)
            
        total_candy = total_candy - candy
        if total_candy <= 0:
            print(f'Игрок {array_playernames[(vs+1)%2]} проиграл')
            break


def LimitCandyPickupPlayer(vs, array_playernames, max_take, total_candy):
    print(f'Осталось конфет: {total_candy}')
    my_input=input(f'Игрок {array_playernames[vs%2]} введите сколько вы конфет хотите взять: ')
    if my_input == '':
        print(f'че пусто, то {max_take}')
        return LimitCandyPickupPlayer(vs, array_playernames, max_take, total_candy)
    candy = 0
    try:
        candy=int(my_input)
    except Exception:
        print('вы ошибка!! вы че попутали, вводите цифру')
        return LimitCandyPickupPlayer(vs, array_playernames, max_take, total_candy)
    if max_take >= candy and max_take > 0:
        return candy
    else:
        print(f'вы ошиблись, максимум {max_take}')
        return LimitCandyPickupPlayer(vs, array_playernames, max_take, total_candy)


def PlayerVsBot():
    total_candy = 2021
    max_take=28
    array_playernames = [input('Введите ваше имя игрок: '),'БОТ']
    vs = randint(0, 1)
    while True:
        vs+=1
        candy=0
        if array_playernames[vs%2] == 'БОТ':
            candy=LimitCandyPickupBot(vs,array_playernames, max_take,total_candy)
        else:
            candy=LimitCandyPickupPlayer(vs,array_playernames, max_take,total_candy)
        if candy > total_candy:
            print(f'Игрок {array_playernames[vs%2]} слишком много конфет просите!!!')
            if array_playernames[vs%2] == 'БОТ':
                candy=LimitCandyPickupBot(vs,array_playernames, max_take,total_candy)
            else:
                candy=LimitCandyPickupPlayer(vs,array_playernames, max_take,total_candy)
            
        total_candy = total_candy - candy
        if total_candy <= 0:
            print(f'{array_playernames[(vs+1)%2]} проиграл')
            break


def LimitCandyPickupBot(vs, array_playernames, max_take, total_candy):
    print(f'Осталось конфет: {total_candy}')
    print(f'Умный БОТ думает')
    time.sleep(randint(1,2))
    candy=0
    if total_candy >= max_take:
        candy=randint(1, max_take)
    else:
        candy=randint(1, total_candy)
    print(f'{array_playernames[vs%2]} ввел: {candy}')
 
    if max_take >= candy and max_take > 0:
        return candy
    else:
        print(f'Бот ошибся, максимум {max_take}')
        return LimitCandyPickupBot(vs, array_playernames, max_take, total_candy)

def rle(data): 
    encoding = ''
    prev_char = ''
    count = 1 
    if not data: return ''
    for char in data: 
        if char != prev_char:
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1
            prev_char = char 
        else:  
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding
def decode_rle(data: str) -> str:
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():  
            count += char 
        else:
            decode += char * int(count)
            count = '' 
    return decode
Task3()