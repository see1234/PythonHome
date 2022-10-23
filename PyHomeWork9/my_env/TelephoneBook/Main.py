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
from email.message import Message
import sys
sys.path.append("modules")
import Userinterface
import modules.DBtxt 
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
 
    modules.DBtxt.createTableIfNot()
    if not update.message.document is None:
        if '.csv' in update.message.document.file_name or '.txt' in update.message.document.file_name:
            myfile=await update.message.document.get_file()
            await myfile.download(custom_path = sys.path[0] + '/' + update.message.document.file_name )
            while True:
                if os.path.exists(sys.path[0] + '/' + update.message.document.file_name):
                    filem=open(update.message.document.file_name, 'rb')
                    myfilename=update.message.document.file_name
                    if '.csv' in myfilename:
                        modules.DBtxt.ImportDBFileCSV(filem)
                    elif '.txt' in myfilename:
                        modules.DBtxt.ImportDBFileTxt(filem)
                    await update.message.reply_text('все')
                    break
    elif update.message.text == '/start':
        await update.message.reply_text(Userinterface.help())
    elif update.message.text.split(' ')[0] == '/list':
         
        await update.message.reply_text(modules.DBtxt .printlines())
    elif update.message.text.split(' ')[0] == '/add':
        nomer=update.message.text.split(' ')[1]
        comm=update.message.text.split(' ')[2]
        fio=update.message.text.replace('/add ', '').replace(nomer + ' ', '').replace(comm + ' ','')
        res=nomer +','+comm + ',' + fio
        modules.DBtxt.add(insert_input = res, id = modules.DBtxt.createUser())   
        await update.message.reply_text('все хорошо')
    elif update.message.text.split(' ')[0] == '/remove':
        msg=update.message.text.split(' ')
        if len(msg) != 5:
           await update.message.reply_text('Error')
           return
         
        if msg[3] == 'Y':
            modules.DBtxt.deleteUser(deleteFromFio = True,fio = msg[1])
        elif msg[2] == 'Y':
            modules.DBtxt.deleteUser(deleteFromTelephone = True,telephone = msg[1])
        elif msg[4] == 'Y':
            modules.DBtxt.deleteUser(deleteFromId = True,id = msg[1])
        await update.message.reply_text('все')
    elif update.message.text.split(' ')[0] == '/export':
        await update.message.reply_document(modules.DBtxt.ExportDBinFileCSV())
        await update.message.reply_document(modules.DBtxt.ExportDBinFileTxt())
        await update.message.reply_text('все')
     
def start_():
    app = ApplicationBuilder().token('5749932159:AAFxbBj9agGbBEFOzSIifzIELxhKzDorXfE').build()
    app.add_handler(MessageHandler(filters.ALL, start))

    app.run_polling()

start_()
