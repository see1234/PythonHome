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
    res=''
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            result=''
            for i in f.readlines():
                result+=i.replace('\n', '') + ',' # добавляем запятые
            id=filename.split('\\')[len(filename.split('\\'))-1].replace('.txt', '')
            res+='ID[' + id + ']: ' + result[:-1]+'\n' #убрать необходимо лишнию запятую было 
    return res
    

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
    file = open('exportfile' + '.txt','w')
    file.close()
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            result=''
            for i in f.readlines():
                result+=i.replace('\n', '') + ',' # добавляем запятые
            file = open('exportfile' + '.txt','a')
            file.write(result[:-2] + '\n')
            file.close()
    return open('exportfile' + '.txt','rb')
def ExportDBinFileCSV(path = "dbtxt/"):
    file = open('exportfile' + '.csv','w')
    file.close()
    array=[]
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            result=''
            for i in f.readlines():
                result+=i.replace('\n', '') + ',' # добавляем запятые
            array.append(result[:-2])
    with open('exportfile.csv', 'w', newline='') as myfile:    
        fieldnames = ['Телефон', 'ФИО', 'Комментарий']
        two_array=[]
        two_array.append(fieldnames)
        for i in array:
            two_array.append(i.split(',')) 
        writer = csv.writer(myfile, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(two_array)
    return open('exportfile' + '.csv','rb')
def ImportDBFileCSV(myfile): 
    line=0
    for i in myfile.readlines():
        if line != 0:
            add(insert_input = str(i.decode('cp866')).replace(';', ','), id = createUser())  
        line+=1
def ImportDBFileTxt(myfile):
    for i in myfile.readlines():
        add(insert_input = str(i.decode('cp866')), id = createUser())  