# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import db
import datetime,time

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog,loginfo):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 351)
        Dialog.setFixedSize(401, 351)
        self.loginfo = loginfo
        self.form = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 40, 91, 16))
        self.label.setObjectName("label")
        self.oldpasswd = QtWidgets.QLineEdit(Dialog)
        self.oldpasswd.setGeometry(QtCore.QRect(140, 70, 113, 31))
        self.oldpasswd.setObjectName("oldpasswd")
        self.newpasswd = QtWidgets.QLineEdit(Dialog)
        self.newpasswd.setGeometry(QtCore.QRect(142, 170, 111, 31))
        self.newpasswd.setText("")
        self.newpasswd.setObjectName("newpasswd")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 140, 81, 20))
        self.label_2.setObjectName("label_2")
        self.commit = QtWidgets.QPushButton(Dialog)
        self.commit.setGeometry(QtCore.QRect(110, 260, 181, 61))
        self.commit.setObjectName("commit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
		
		#按钮点击事件
        self.commit.clicked.connect(self.changepasswd)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "更改密码"))
        self.label.setText(_translate("Dialog", "输入之前的密码："))
        self.label_2.setText(_translate("Dialog", "输入新的密码："))
        self.commit.setText(_translate("Dialog", "确认"))

    def changepasswd(self):
        old = self.oldpasswd.text()   #获取旧密码文本框内容  
        new = self.newpasswd.text()   #获取新密码文本框内容
        if old == '' or len(old) > 12:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","输入的旧密码为空或长度不对", QMessageBox.Yes | QMessageBox.No)
        elif new == '' or len(new) > 12:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","输入的新密码为空或长度不对", QMessageBox.Yes | QMessageBox.No)
        else:
            #MD5加密密码
            userna = self.loginfo
            password = old
            self.b = db.getdata()
            result = self.b.formuser(userna,password)
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","您输入的旧密码不正确", QMessageBox.Yes | QMessageBox.No)
            else:
                password = new
                a = db.postdata()
                result = a.updatepasswd(userna,password)
                if result == 1:
                    reply = QtWidgets.QMessageBox.warning(self,"提示信息","更改密码时出错，请重试", QMessageBox.Yes | QMessageBox.No)
                else:
                    reply = QtWidgets.QMessageBox.warning(self,"提示信息","密码更改成功！", QMessageBox.Yes | QMessageBox.No) 
                    self.form.hide()    #隐藏窗口