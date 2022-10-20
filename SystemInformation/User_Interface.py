def userHelp():
    print('Программа работает с помощью консоли:')
    print('1 - добавить нового ученика в базу.')
    print('2 - добавить оценку ученику за предмет.')
    print('3 - посмотреть учеников, и их оценки за предметы.')
    print('exit(), quit, q - выход из системы')
    return input()
def getClass():
    print('скажите ваш класс, типа "5А"')
    inp=input()
    if len(inp) > 3:
        print('класс не может быть больше 3 символов')
        getClass()
    if not inp[0:1] in '0123456789':
        print('Вы не ввели цифру')
        getClass()
    return inp
def getFIO():
    print('Введите ФИО:')
    inp=input()
    if not ' ' in inp:
        getFIO()
    if len(inp.split(' ')) > 3:
        print('ФИО не может быть больше 3 пробелов')
        getFIO()
    return inp
def getInputFIO():
    print('Введите ФИО:')
    inp=input()
    return inp
def getScore():
    print('Введите оценку:')
    inp=input()
    if not inp in '0123456789':
        print('Вы не ввели цифру')
        getScore()
    if int(inp) > 5:
        print('максимум только 5')
    return inp
def getItem():
    print('Введите предмет')
    inp=input()
    return inp
def getStudentId():
    print('Введите айди ученика')
    inp=input()
    try:
        inp = int(inp)
    except ValueError:
        print("Это не число")
        getStudentId()
    return inp