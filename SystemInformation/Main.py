
from asyncio.windows_events import NULL
import User_Interface
import datetime
import time
from modules.DBSQLiteExecutor import *
def consoleMenu():
    while True:
        inp = User_Interface.userHelp()
        if inp == '1':
            FIO = User_Interface.getFIO()
            Class = User_Interface.getClass()
            student_id = lenTable('db_students')+1
            executeSQL(f"""INSERT INTO db_students(student_id,full_name, class_id) 
   VALUES('{student_id}','{FIO}', '{Class}');""")
        elif inp == '2':
            item = User_Interface.getItem()
            score = User_Interface.getScore()
            student_id = User_Interface.getStudentId()
            date = round(time.time() * 1000)
            id = lenTable('db_items')+1
            executeSQL(f"""INSERT INTO db_items(id,item_name,date,score,student_id ) 
   VALUES('{id}','{item}', {date}, {score}, {student_id});""")
        elif inp == '3':
            arr=exandinarraySQL(f"SELECT * FROM db_students")
             
            for i in arr:
                student_id=i[0]
                fio=i[1]
                Class=i[2]
                print(f'ID: {student_id}, ФИО: "{fio}", Класс: {Class}')
                arr2=exandinarraySQL(f"SELECT * FROM db_items WHERE student_id={student_id}")
                for j in arr2:
                    item=j[1]
                    date=str(datetime.datetime.fromtimestamp(j[2]/1000.0)).split('.')[0]
                    score=j[3]
                    print(f'  - {item} {date}: {score}')
def init():
    connect()
    loadSQLite()
    consoleMenu()
init()
 