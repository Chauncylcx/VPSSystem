# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import db
import datetime,time

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog,loginfo):
        Dialog.setObjectName("Dialog")
        Dialog.resize(572, 440)
        self.commit = QtWidgets.QPushButton(Dialog)
        self.commit.setGeometry(QtCore.QRect(150, 360, 131, 41))
        self.commit.setObjectName("commit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(320, 170, 54, 12))
        self.label_3.setObjectName("label_3")
        self.startTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.startTimeEdit.setGeometry(QtCore.QRect(130, 40, 121, 31))
        self.startTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 11, 23), QtCore.QTime(0, 0, 0)))
        self.startTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm") 
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.price = QtWidgets.QLineEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(370, 220, 121, 31))
        self.price.setText("")
        self.price.setObjectName("price")
        self.ipaddr = QtWidgets.QLineEdit(Dialog)
        self.ipaddr.setGeometry(QtCore.QRect(370, 160, 121, 31))
        self.ipaddr.setText("")
        self.ipaddr.setObjectName("ipaddr")
        self.username = QtWidgets.QComboBox(Dialog)
        self.username.setEditable(True)
        self.username.setGeometry(QtCore.QRect(130, 100, 121, 31))
        self.username.setObjectName("username")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(320, 290, 51, 16))
        self.label_10.setObjectName("label_10")
        self.starttimetitle = QtWidgets.QLabel(Dialog)
        self.starttimetitle.setGeometry(QtCore.QRect(60, 50, 54, 12))
        self.starttimetitle.setObjectName("starttimetitle")
        self.paymode = QtWidgets.QComboBox(Dialog)
        self.paymode.setGeometry(QtCore.QRect(130, 280, 121, 31))
        self.paymode.setObjectName("paymode")
        self.paymode.addItem("")
        self.paymode.addItem("")
        self.paymode.addItem("")
        self.paymode.addItem("")
        self.endTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.endTimeEdit.setGeometry(QtCore.QRect(370, 40, 121, 31))
        self.endTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm") 
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.endtimetitel = QtWidgets.QLabel(Dialog)
        self.endtimetitel.setGeometry(QtCore.QRect(300, 50, 54, 12))
        self.endtimetitel.setObjectName("endtimetitel")
        self.datacenter = QtWidgets.QComboBox(Dialog)
        self.datacenter.setGeometry(QtCore.QRect(130, 220, 121, 31))
        self.datacenter.setObjectName("datacenter")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 110, 51, 16))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 290, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(320, 230, 31, 16))
        self.label_6.setObjectName("label_6")
        self.note = QtWidgets.QLineEdit(Dialog)
        self.note.setGeometry(QtCore.QRect(370, 280, 121, 31))
        self.note.setText("")
        self.note.setObjectName("note")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 230, 54, 12))
        self.label_5.setObjectName("label_5")
        self.commit_2 = QtWidgets.QPushButton(Dialog)
        self.commit_2.setGeometry(QtCore.QRect(310, 360, 131, 41))
        self.commit_2.setObjectName("commit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(330, 110, 31, 16))
        self.label_4.setObjectName("label_4")
        self.oid = QtWidgets.QLineEdit(Dialog)
        self.oid.setGeometry(QtCore.QRect(370, 100, 121, 31))
        self.oid.setText("")
        self.oid.setObjectName("oid")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(60, 170, 51, 16))
        self.label_11.setObjectName("label_11")
        self.phone = QtWidgets.QLineEdit(Dialog)
        self.phone.setGeometry(QtCore.QRect(130, 160, 121, 31))
        self.phone.setText("")
        self.phone.setObjectName("phone")

        self.now_date_year = int(datetime.datetime.now().strftime("%Y"))
        self.next_date_year = int(datetime.datetime.now().strftime("%Y")) + 1
        self.now_date_month = int(datetime.datetime.now().strftime("%m"))
        self.now_date_day = int(datetime.datetime.now().strftime("%d"))

        self.now_time_h = int(datetime.datetime.now().strftime("%H"))
        self.now_time_m = int(datetime.datetime.now().strftime("%M"))
        self.now_time_s = int(datetime.datetime.now().strftime("%S"))
        #定义当前时间控件
        self.startTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.now_date_year, self.now_date_month, self.now_date_day), QtCore.QTime(self.now_time_h, self.now_time_m, self.now_time_s)))
        self.endTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.next_date_year, self.now_date_month, self.now_date_day), QtCore.QTime(self.now_time_h, self.now_time_m, self.now_time_s)))

        #初始化自动补齐姓名
        self.init_combobox()

        #增加选中事件
        self.username.activated.connect(self.on_combobox_Activate)

        #提交按钮
        self.commit.clicked.connect(self.commitdata)

        #重置按钮
        self.commit_2.clicked.connect(self.empty)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "新建项目"))
        self.commit.setText(_translate("Dialog", "提交"))
        self.label_3.setText(_translate("Dialog", "主IP"))
        self.label_10.setText(_translate("Dialog", "备注"))
        self.starttimetitle.setText(_translate("Dialog", "开始时间"))
        self.paymode.setItemText(0, _translate("Dialog", "支付宝"))
        self.paymode.setItemText(1, _translate("Dialog", "微信"))
        self.paymode.setItemText(2, _translate("Dialog", "银行卡"))
        self.paymode.setItemText(3, _translate("Dialog", "信用卡"))
        self.endtimetitel.setText(_translate("Dialog", "到期时间"))
        self.datacenter.setItemText(0, _translate("Dialog", "香港"))
        self.datacenter.setItemText(1, _translate("Dialog", "台湾"))
        self.datacenter.setItemText(2, _translate("Dialog", "新加坡"))
        self.datacenter.setItemText(3, _translate("Dialog", "美国纽约"))
        self.datacenter.setItemText(4, _translate("Dialog", "美国华盛顿"))
        self.label_8.setText(_translate("Dialog", "用户姓名"))
        self.label_7.setText(_translate("Dialog", "付款方式"))
        self.label_6.setText(_translate("Dialog", "价格"))
        self.label_5.setText(_translate("Dialog", "数据中心"))
        self.commit_2.setText(_translate("Dialog", "重置"))
        self.label_4.setText(_translate("Dialog", "ID"))
        self.label_11.setText(_translate("Dialog", "联系方式"))

    def init_combobox(self):
        # 增加选项元素
        items_list = []
        a = db.getdata()
        result = a.alluser()
        if result != 1:
            for i in result:
                items_list.append(i[0])
        for i in range(len(items_list)):
            self.username.addItem(items_list[i])
        self.username.setCurrentIndex(-1)

        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.username.setCompleter(self.completer)

    def on_combobox_Activate(self):
        name = self.username.currentText()
        phone = ''
        a = db.getdata()
        result = a.userphone(name)
        if result != 1:
            for i in result:
                phone = i[0]
        self.phone.setText(phone)

    def empty(self):
        self.oid.setText('')
        self.ipaddr.setText('')
        self.price.setText('')
        self.note.setText('')
        self.startTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.now_date_year, self.now_date_month, self.now_date_day), QtCore.QTime(self.now_time_h, self.now_time_m, self.now_time_s)))
        self.endTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.next_date_year, self.now_date_month, self.now_date_day), QtCore.QTime(self.now_time_h, self.now_time_m, self.now_time_s)))


    def commitdata(self):
        starttime = self.startTimeEdit.text()
        endtime = self.endTimeEdit.text()
        uname = self.username.currentText()
        uphone = self.phone.text()
        uid = self.oid.text()
        uip = self.ipaddr.text()
        uprice = self.price.text()
        udatacenter = self.datacenter.currentText()
        upaymode = self.paymode.currentText()
        unote = self.note.text()
        if uname == '' or uid == '' or uphone == '' or uip == '' or uprice == '':
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","必填项不能为空！", QMessageBox.Yes | QMessageBox.No)
        else:
            geta = db.getdata()
            usersid = geta.usersid([uname,uphone])
            if usersid != 1:
                usersid = usersid[0][0]
            else:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","联系人和联系方式不匹配", QMessageBox.Yes | QMessageBox.No)
                return
            uprice = uprice + '.00'
            p = [usersid,uid,uip,uprice,unote,uname,uphone,starttime,endtime,udatacenter,upaymode]
            a = db.postdata()
            result = a.insertvps(p)
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","数据提交失败！", QMessageBox.Yes | QMessageBox.No)
            else:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","数据提交成功！", QMessageBox.Yes | QMessageBox.No)
                self.empty()



