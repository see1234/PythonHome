import os, glob, csv
def add(path = "dbtxt/", insert_input = "NULL", id = 0):
    if insert_input == 'NULL':
        return False
    elif id == 0:
        return False
    else:
        if not os.path.exists(path):
            os.makedirs(path)
        file = open(path + str(id) + '.txt','a')
        file.write(insert_input)
        file.close()
        return True


def createTableIfNot(path = "dbtxt/"):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False


def delete(path = "dbtxt/", id = 0):
    if id == 0:
        return False
    else:
        if os.path.exists(path + str(id) + '.txt'):
            os.remove(path + str(id) + '.txt')
        return True


def set(path = "dbtxt/", insert_input = "NULL", id = 0):
    if insert_input == 'NULL':
        return False
    elif id == 0:
        return False
    else:
        if not os.path.exists(path):
            os.makedirs(path)
        file = open(path + str(id) + '.txt','w')
        file.writelines(insert_input)
        file.close()
        return True


def printlines(path = "dbtxt/"):
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            result=''
            for i in f.readlines():
                result+=i.replace('\n', '') + ',' # добавляем запятые
            id=filename.split('\\')[len(filename.split('\\'))-1].replace('.txt', '')
            print('ID[' + id + ']:', result[:-1]) #убрать необходимо лишнию запятую было 
    return True
    

def createUser(path = "dbtxt/"):
    count=0
    while True:
        count+=1
        if not os.path.exists(path + str(count) + '.txt'):
            file = open(path + str(count) + '.txt','w')
            file.close()
            return count # Данный код создан для создания фаила txt под специальным id.


def deleteFromFioMethod(path = "dbtxt/", fio = 'NULL'):
    for filename in glob.glob(os.path.join(path, '*.txt')):
        try:
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                if fio in f.readline().split(',')[1]:
                    if os.path.exists(filename):
                        os.remove(filename)
        except Exception:
            if os.path.exists(filename):
                os.remove(filename)

def deleteFromTelephoneMethod(path = "dbtxt/", telephone = 'NULL'):
    for filename in glob.glob(os.path.join(path, '*.txt')):
        try:
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                if telephone in f.readline().split(',')[0]:
                    if os.path.exists(filename):
                        os.remove(filename)
        except Exception:
            if os.path.exists(filename):
                os.remove(filename)


def deleteUser(deleteFromId = False, deleteFromFio = False, deleteFromTelephone = False, id = 'NULL', fio = 'NULL', telephone = 'NULL'):
    if deleteFromId:
        delete(id = id)
    if deleteFromFio:
        deleteFromFioMethod(fio = fio)
    if deleteFromTelephone:
        deleteFromTelephoneMethod(telephone = telephone)


def ExportDBinFileTxt(path = "dbtxt/"):
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            result=''
            for i in f.readlines():
                result+=i.replace('\n', '') + ',' # добавляем запятые
            file = open('exportfile' + '.txt','a')
            file.write(result[:-1])
            file.close()
def ExportDBinFileCSV(path = "dbtxt/"):
    array=[]
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            result=''
            for i in f.readlines():
                result+=i.replace('\n', '') + ',' # добавляем запятые
            array.append(result[:-1])
    with open('exportfile.csv', 'w', newline='') as myfile:    
        fieldnames = ['Телефон', 'ФИО', 'Комментарий']
        two_array=[]
        two_array.append(fieldnames)
        for i in array:
            two_array.append(i.split(',')) 
        print(two_array)
        writer = csv.writer(myfile, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(two_array)
def ImportDBFileCSV(path = "exportfile"):
    path = path + '.csv'
    a=0
    with open(path, 'r', newline='') as myfile:    
        for i in myfile.readlines():
            a+=1
            if a > 1:
                add(insert_input = i.replace(';', ','), id = createUser())  
def ImportDBFileTxt(path = "exportfile"):
    path = path + '.txt'
    with open(path, 'r', newline='') as myfile:    
        for i in myfile.readlines():
            add(insert_input = i, id = createUser())  