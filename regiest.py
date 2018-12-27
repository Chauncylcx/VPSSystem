# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import db

class Ui_Dialog(QWidget):
	#加载控件
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 355)
        Dialog.setFixedSize(419, 355)
        self.form = Dialog
        self.idedit = QtWidgets.QLineEdit(Dialog)
        self.idedit.setGeometry(QtCore.QRect(180, 40, 121, 31))
        self.idedit.setObjectName("idedit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 50, 54, 12))
        self.label.setObjectName("label")
        self.passwdedit = QtWidgets.QLineEdit(Dialog)
        self.passwdedit.setGeometry(QtCore.QRect(180, 100, 121, 31))
        self.passwdedit.setText("")
        self.passwdedit.setObjectName("passwdedit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 170, 54, 12))
        self.label_3.setObjectName("label_3")
        self.nameedit = QtWidgets.QLineEdit(Dialog)
        self.nameedit.setGeometry(QtCore.QRect(180, 160, 121, 31))
        self.nameedit.setText("")
        self.nameedit.setObjectName("nameedit")
        self.mailedit = QtWidgets.QLineEdit(Dialog)
        self.mailedit.setGeometry(QtCore.QRect(180, 220, 121, 31))
        self.mailedit.setText("")
        self.mailedit.setObjectName("mailedit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 230, 54, 12))
        self.label_4.setObjectName("label_4")
        self.reg = QtWidgets.QPushButton(Dialog)
        self.reg.setGeometry(QtCore.QRect(120, 280, 91, 31))
        self.reg.setObjectName("reg")
        self.empty = QtWidgets.QPushButton(Dialog)
        self.empty.setGeometry(QtCore.QRect(220, 280, 91, 31))
        self.empty.setObjectName("empty")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "注册用户"))
        self.label.setText(_translate("Dialog", "登录ID"))
        self.label_2.setText(_translate("Dialog", "登录密码"))
        self.label_3.setText(_translate("Dialog", "姓   名"))
        self.label_4.setText(_translate("Dialog", "邮   箱"))
        self.reg.setText(_translate("Dialog", "注册"))
        self.empty.setText(_translate("Dialog", "清空"))
		#按钮点击事件
        self.reg.clicked.connect(self.loginp)
        self.empty.clicked.connect(self.bempty)
	
    def bempty(self):
		#清空时的动作
        self.idedit.setText('')
        self.passwdedit.setText('')
        self.nameedit.setText('')
        self.mailedit.setText('')

    def loginp(self):
        uid = self.idedit.text()   #获取文本框内容
        upasswd = self.passwdedit.text()   #获取文本框内容  
        uname = self.nameedit.text()   #获取文本框内容
        uemail = self.mailedit.text()   #获取文本框内容
        if uid == '' or upasswd == '' or uname == '' or uemail == '':
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","文本框不能为空", QMessageBox.Yes | QMessageBox.No)
        elif len(uid) > 10 or len(upasswd) > 15 or len(uname) > 5 or len(uemail) >50:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","字符长度超过文本框定义的长度", QMessageBox.Yes | QMessageBox.No)
        else:
            #若返回的值是0，则代表注册成功，反之及注册失败
            userinfo = [uid,upasswd,uname,uemail]
            a = db.postdata()
            result = a.insertuser(userinfo)
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","注册失败，请确认数据库以及表都存在", QMessageBox.Yes | QMessageBox.No)
            elif result == 0:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","注册成功！", QMessageBox.Yes | QMessageBox.No)
                self.form.hide()    #隐藏窗口




