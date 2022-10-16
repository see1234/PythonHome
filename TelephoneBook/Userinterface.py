import os
def help():
    print('Добро пожаловать, программа работает с помощью консоли:')
    print('1 - выводит список телефонов.')
    print('2 - добавить в список новый телефон.')
    print('3 - удалить номер телефона, по номеру, по фио, по айди.')
    print('4 - экспортировать')
    print('5 - импортировать фаил')
    print('exit(), quit, q - выход из системы')
    return input()
def addTelephone():
    print('Введите номер')
    telephone=input()
    print('Введите ФИО')
    fio=input()
    print('Введите комментарий')
    comment=input()
    return telephone + ',' + fio + ',' + comment
def remove():
    print('Выберите критерий')
    print('1 - ФИО')
    print('2 - ПО НОМЕРУ ТЕЛЕФОНА')
    print('3 - ПО АЙДИ')
    while True:
        user_input=input()
        if user_input == '1': 
            return 1
        elif user_input == '2':
            return 2
        elif user_input == '3':
            return 3
        else:
            print('Выберите критерий')
            print('1 - ФИО')
            print('2 - ПО НОМЕРУ ТЕЛЕФОНА')
            print('3 - ПО АЙДИ')
def typeexport():
    print('Выберите критерий')
    print('1 - CSV')
    print('2 - TXT')
    while True:
        user_input=input()
        if user_input == '1': 
            return 1
        elif user_input == '2':
            return 2
        else:
            print('Выберите критерий')
            print('1 - CSV')
            print('2 - TXT')
def getFileCSVorTxt():
    print('Назовите ваш фаил (он должен быть в одной папке с проектом)')
    while True:
        user_input=input()
        if os.path.exists(user_input):
            return user_input
        else:
            print('Назовите ваш фаил (он должен быть в одной папке с проектом)')
def getFio():
    print('Введите ФИО')
    return input()
def getTelephone():
    print('Введите телефон')
    return input()
def getId():
    print('Введите айди')
    try:
        return int(input())
    except Exception:
        return getId()