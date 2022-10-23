import os
def help():
    result=''
    result+='Добро пожаловать, программа работает с помощью консоли:\n'
    result+='/list - выводит список телефонов.\n'
    result+='/add <Номер телефона> <Коммент> <ФИО> - добавить в список новый телефон.\n'
    result+='/remove <Номер телефона/ФИО/Айди> <Номер телефона Y/n> <ФИО Y/n> <Айди Y/n> - удалить номер телефона, по номеру, по фио, по айди.\n'
    result+='/export - экспортировать\n'
    result+='Просто киньте фаил (.txt, .csv) - импортировать фаил\n'
    return result
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