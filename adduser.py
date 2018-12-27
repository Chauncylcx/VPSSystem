# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import db
import newinfo

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog,loginfo):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 402)
        #限制最大窗口size
        Dialog.setFixedSize(464, 402)
        self.loginfo = loginfo
        self.form = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 40, 54, 12))
        self.label.setObjectName("label")
        self.userEdit = QtWidgets.QLineEdit(Dialog)
        self.userEdit.setGeometry(QtCore.QRect(180, 30, 151, 31))
        self.userEdit.setObjectName("userEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.phoneEdit = QtWidgets.QLineEdit(Dialog)
        self.phoneEdit.setGeometry(QtCore.QRect(180, 80, 151, 31))
        self.phoneEdit.setObjectName("phoneEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 140, 31, 16))
        self.label_3.setObjectName("label_3")
        self.aliasEdit = QtWidgets.QLineEdit(Dialog)
        self.aliasEdit.setGeometry(QtCore.QRect(180, 130, 151, 31))
        self.aliasEdit.setObjectName("aliasEdit")
        self.mailEdit = QtWidgets.QLineEdit(Dialog)
        self.mailEdit.setGeometry(QtCore.QRect(180, 180, 151, 31))
        self.mailEdit.setObjectName("mailEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 190, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(120, 240, 31, 16))
        self.label_5.setObjectName("label_5")
        self.remarkEdit = QtWidgets.QLineEdit(Dialog)
        self.remarkEdit.setGeometry(QtCore.QRect(180, 230, 151, 31))
        self.remarkEdit.setObjectName("remarkEdit")
        self.adduser = QtWidgets.QPushButton(Dialog)
        self.adduser.setGeometry(QtCore.QRect(100, 310, 75, 31))
        self.adduser.setObjectName("adduser")
        self.empty = QtWidgets.QPushButton(Dialog)
        self.empty.setGeometry(QtCore.QRect(190, 310, 75, 31))
        self.empty.setObjectName("empty")
        self.already = QtWidgets.QPushButton(Dialog)
        self.already.setGeometry(QtCore.QRect(280, 310, 75, 31))
        self.already.setObjectName("already")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #清空按钮
        self.empty.clicked.connect(self.emptyd)

        #添加按钮
        self.adduser.clicked.connect(self.useradd)

        #已有用户按钮
        self.already.clicked.connect(self.jump_to_newobject)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加用户"))
        self.label.setText(_translate("Dialog", "用户姓名："))
        self.label_2.setText(_translate("Dialog", "联系方式："))
        self.label_3.setText(_translate("Dialog", "别名："))
        self.label_4.setText(_translate("Dialog", "邮箱地址："))
        self.label_5.setText(_translate("Dialog", "备注："))
        self.adduser.setText(_translate("Dialog", "添加"))
        self.empty.setText(_translate("Dialog", "清空"))
        self.already.setText(_translate("Dialog", "已有用户"))

    def emptyd(self):
        self.userEdit.setText('')
        self.phoneEdit.setText('')
        self.aliasEdit.setText('')
        self.mailEdit.setText('')
        self.remarkEdit.setText('')

    def jump_to_newobject(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = newinfo.Ui_Dialog()
        ui.setupUi(form1,self.loginfo)
        form1.show()
        form1.exec_()
       

    def useradd(self):
        username = self.userEdit.text()
        phone = self.phoneEdit.text()
        alias = self.aliasEdit.text()
        email = self.mailEdit.text()
        remark = self.remarkEdit.text()
        if username == '' or phone == '' or email == '':
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","名称、联系方式、邮箱 不能为空", QMessageBox.Yes | QMessageBox.No)
        elif len(username) > 10 or len(phone) > 15 or len(alias) > 20 or len(email) > 30 or len(remark) > 50:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","不符合长度，请重新填写", QMessageBox.Yes | QMessageBox.No)
        else:
            p = [username,phone,alias,email,remark]
            a = db.postdata()
            result = a.newuser(p)
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","用户添加失败！", QMessageBox.Yes | QMessageBox.No)
            else:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","用户添加成功！", QMessageBox.Yes | QMessageBox.No)
                self.jump_to_newobject()
               

