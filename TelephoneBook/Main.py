# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 

# - *под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель*
#     *Фамилия_1*
#     *Имя_1*
#     *Телефон_1*
#     *Описание_1*
#     *Фамилия_2*
#     *Имя_2*
#     *Телефон_2*
#     *Описание_2*
#     *и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***
#     *Фамилия_1,Имя_1,Телефон_1,Описание_1*
#     *Фамилия_2,Имя_2,Телефон_2,Описание_2*
#     *и т.д.*
    
#     ❗ Можно явно указать на использование CSV
    
#     *Если группа сильная, можно предложить внедрить JSON, XML*
import sys
sys.path.append("modules")
import Userinterface
import modules.DBtxt 
def init():
    modules.DBtxt .createTableIfNot()
    while True:
        number=Userinterface.help()
        if number == '1':
            modules.DBtxt .printlines()
        elif number == '2':
            modules.DBtxt .add(insert_input = Userinterface.addTelephone(), id = modules.DBtxt.createUser())   
        elif number == '3':
            num = Userinterface.remove()
            if num == 1:
                modules.DBtxt.deleteUser(deleteFromFio = True,fio = Userinterface.getFio())
            elif num == 2:
                modules.DBtxt.deleteUser(deleteFromTelephone = True,telephone = Userinterface.getTelephone())
            elif num == 3:
                modules.DBtxt.deleteUser(deleteFromId = True,id = Userinterface.getId())
        elif number == '4':
            num = Userinterface.typeexport()
            if num == 1:
                modules.DBtxt.ExportDBinFileCSV()
            elif num == 2:
                modules.DBtxt.ExportDBinFileTxt()
            print('сгенерированный фаил экспорта')
        elif number == '5':
            arg = Userinterface.getFileCSVorTxt()
            print(arg)
            if '.csv' in arg:
                modules.DBtxt.ImportDBFileCSV(arg.replace('.csv', ''))
            elif '.txt' in arg:
                modules.DBtxt.ImportDBFileTxt(arg.replace('.txt', ''))
            print('сгенерированный фаил импорта')
        elif number == 'q' or number == 'quit' or number == 'exit()':
            break
        else: 
            print(number)
init()
 