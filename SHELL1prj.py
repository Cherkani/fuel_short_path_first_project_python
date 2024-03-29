# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SHELLprj.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtWidgets import QMessageBox
from interface2 import MainWindow_Ui
from PyQt5.QtGui import QPixmap, QIcon 

class Ui_MainWindow(object):
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainWindow_Ui()
        self.ui.setupUi(self.window)
        self.window.setFixedWidth(824)
        self.window.setFixedHeight(593)
        self.window.show()
        
    def setupUi(self, MainWindow):
        pixmap=QPixmap('C:/Users/ilyass/Desktop/projet/6395463.png')

# Create the QIcon object from the QPixmap
        icon = QIcon(pixmap)

# Set the window icon
        MainWindow.setWindowIcon(icon)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setStyleSheet("#background{\n"
"    \n"
"    background-image: url(:/photos/SHELL.jpg);\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.frame1 = QtWidgets.QFrame(self.background)
        self.frame1.setGeometry(QtCore.QRect(190, 180, 415, 351))
        self.frame1.setStyleSheet("#frame1{\n"
"background-color:#E8b746;\n"
"}")
        self.frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setLineWidth(10)
        self.frame1.setMidLineWidth(10)
        self.frame1.setObjectName("frame1")
        self.frame2 = QtWidgets.QFrame(self.frame1)
        self.frame2.setGeometry(QtCore.QRect(0, 0, 171, 351))
        self.frame2.setStyleSheet("#frame2{\n"
"background-color:#fdd504;\n"
"}")
        self.frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame2.setLineWidth(10)
        self.frame2.setMidLineWidth(10)
        self.frame2.setObjectName("frame2")
        self.label = QtWidgets.QLabel(self.frame2)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 71))
        self.label.setStyleSheet("background-image: url(:/newPrefix/shell-vertical.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("shell-vertical.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 131, 311))
        self.label_2.setStyleSheet("image: url(:/logos/pngwing.com.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.frame2)
        self.line.setGeometry(QtCore.QRect(0, 70, 171, 31))
        self.line.setStyleSheet("color: rgb(230, 0, 0);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(8)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.user = QtWidgets.QLabel(self.frame1)
        self.user.setGeometry(QtCore.QRect(220, 70, 121, 31))
        self.user.setStyleSheet("font: 12pt \"Segoe Print\";\n"
"")
        self.user.setObjectName("user")
        self.code = QtWidgets.QLabel(self.frame1)
        self.code.setGeometry(QtCore.QRect(220, 170, 121, 31))
        self.code.setStyleSheet("font: 12pt \"Segoe Print\";")
        self.code.setObjectName("code")
        self.iconuser = QtWidgets.QLabel(self.frame1)
        self.iconuser.setGeometry(QtCore.QRect(180, 70, 31, 31))
        self.iconuser.setStyleSheet("#iconuser{\n"
"    image: url(:/logos/user.svg);\n"
"}")
        self.iconuser.setText("")
        self.iconuser.setObjectName("iconuser")
        self.iconcode = QtWidgets.QLabel(self.frame1)
        self.iconcode.setGeometry(QtCore.QRect(180, 170, 41, 31))
        self.iconcode.setStyleSheet("#iconcode{\n"
"    image: url(:/logos/lock.svg);\n"
"}")
        self.iconcode.setText("")
        self.iconcode.setObjectName("iconcode")
        self.enter = QtWidgets.QPushButton(self.frame1)
        self.enter.setGeometry(QtCore.QRect(320, 270, 75, 31))
        self.enter.setStyleSheet("#enter{\n"
"    font: 14pt \"Sakkal Majalla\";\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"")
        self.enter.setObjectName("enter")
        self.username = QtWidgets.QLineEdit(self.frame1)
        self.username.setGeometry(QtCore.QRect(190, 110, 181, 25))
        self.username.setStyleSheet("font: 11pt \"Sitka Display\";")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame1)
        self.password.setGeometry(QtCore.QRect(190, 210, 181, 25))
        self.password.setStyleSheet("font: 11pt \"Sitka Display\";")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.enter.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user.setText(_translate("MainWindow", "User-name :"))
        self.code.setText(_translate("MainWindow", "Password :"))
        self.enter.setText(_translate("MainWindow", "Enter"))


    def show_popup(self):
        msg=QMessageBox()
        us=self.username.text()
        pasw=self.password.text()

        if us=="" or pasw=="":
            msg.setWindowTitle("warning")
            msg.setText("*All the fields are obligatory")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("font: 9pt \"Segoe UI Variable Display Semib\";\n""")

            x=msg.exec_()
        elif us == "admin" and pasw == "123456":
            msg.setWindowTitle("success")
            msg.setText("Login successful")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.setStyleSheet("font: 9pt \"Segoe UI Variable Display Semib\";\n""")

            msg.buttonClicked.connect(self.login)
            x=msg.exec_()
            
        
        elif us == "admin" and pasw != "123456":
            msg.setWindowTitle("warning")
            msg.setText("*Incorrect password")
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet("font: 9pt \"Segoe UI Variable Display Semib\";\n""")

            x=msg.exec_()

        elif us != "admin" and pasw == "123456":
            msg.setWindowTitle("warning")
            msg.setText("*Incorrect username")
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet("font: 9pt \"Segoe UI Variable Display Semib\";\n""")

            x=msg.exec_()
        

        else:
            msg.setWindowTitle("warning")
            msg.setText("*Incorrect username and password")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("font: 9pt \"Segoe UI Variable Display Semib\";\n""")

            x=msg.exec_()
    def login(self,i):
        print(i.text())
        
        if i.text()== 'OK':
            MainWindow.close()
            self.openWindow()
            
            
            
            
            
        
            
        
import testshell_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedWidth(824)
    MainWindow.setFixedHeight(583)
    MainWindow.show()
    sys.exit(app.exec_())
