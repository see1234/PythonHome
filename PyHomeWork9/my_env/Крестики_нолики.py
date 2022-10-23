#Крестики нолики QT edition
 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

 
class main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
 
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Крестики нолики')
        self.player = 'X'
        self.buttons = []
        for i in range(3):
            self.buttons.append([])
            for j in range(3):
               self.buttons[i].append(QPushButton(self))
               self.buttons[i][j].resize(100, 100)
               self.buttons[i][j].move(100 * (i + 1), 100 * (j + 1))
               self.buttons[i][j].setText('')
               self.buttons[i][j].clicked.connect(self.clickGame)
               self.buttons[i][j].setStyleSheet("background: rgb(255, 255, 255);")
               self.buttons[i][j].setFont(QFont('Arial', 16))
        self.label = QLabel(self)
        self.label.resize(40, 100)
        self.label.move(10, 10)
        self.count = 0

    def clickEvent(self):
        self.player = self.sender().text()
        for i in range(3):
            for j in range(3):
               self.buttons[i][j].setDisabled(False)
 
 
    def clickGame(self):
        self.sender().setStyleSheet("color: rgb(255, 0, 4);\n" if self.player == 'X' else "color: rgb(8, 0, 255);")
        self.sender().setText(self.player)
        self.sender().setDisabled(True)
        self.isWin()
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
        self.count+=1
    def isWin(self):
        ans = []
        for i in range(3):
            temp = self.buttons[i][0].text() + self.buttons[i][1].text() + self.buttons[i][2].text()
            ans.append(temp)
        for j in range(3):
            temp = self.buttons[0][j].text() + self.buttons[1][j].text() + self.buttons[2][j].text()
            ans.append(temp)
        temp = self.buttons[0][0].text() + self.buttons[1][1].text() + self.buttons[2][2].text()
        ans.append(temp)
        temp = self.buttons[0][2].text() + self.buttons[1][1].text() + self.buttons[2][0].text()
        ans.append(temp)
        if 'XXX' in ans:
            self.disableAllBlocks()
 
            self.show_info_messagebox('Крестик')
        elif 'OOO' in ans:
            self.disableAllBlocks()
 
            self.show_info_messagebox('Нолик')
        elif self.count == 8:
            self.disableAllBlocks()
 
            self.show_info_messagebox('Никто')
        print(self.count)
    def show_info_messagebox(self, win):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
    
        # setting message for Message Box
        msg.setText("Перезапустить ли игру?")
        
        # setting Message box window title
        msg.setWindowTitle(f"Победитель: {win}")
        
        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
             
        # start the app
        retval = msg.exec_()
        if retval == 1024:
            self.restart()
        else:
            sys.exit()
    def disableAllBlocks(self):
        for i in range(3):
            for j in range(3):
               self.buttons[i][j].setDisabled(True)
    def restart(self):
        self.player = 'X'
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                self.buttons[i][j].setText('')
                self.buttons[i][j].setStyleSheet("background: rgb(255, 255, 255);")
                self.buttons[i][j].setDisabled(False)
        self.count = 0
app = QApplication(sys.argv)
ex = main()
ex.show()
sys.exit(app.exec())