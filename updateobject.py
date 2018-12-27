# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import db
import datetime,time

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog,loginfo):
        Dialog.setObjectName("Dialog")
        Dialog.resize(684, 483)
        Dialog.setFixedSize(684, 483)
        self.form = Dialog
        self.commit = QtWidgets.QPushButton(Dialog)
        self.commit.setGeometry(QtCore.QRect(320, 410, 211, 51))
        self.commit.setObjectName("commit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(140, 20, 531, 371))
        self.groupBox.setObjectName("groupBox")
        self.Contact = QtWidgets.QLineEdit(self.groupBox)
        self.Contact.setGeometry(QtCore.QRect(360, 260, 121, 31))
        self.Contact.setText("")
        self.Contact.setObjectName("Contact")
        self.price = QtWidgets.QLineEdit(self.groupBox)
        self.price.setGeometry(QtCore.QRect(360, 140, 121, 31))
        self.price.setText("")
        self.price.setObjectName("price")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(60, 270, 41, 16))
        self.label_8.setObjectName("label_8")
        self.iprange_2 = QtWidgets.QLabel(self.groupBox)
        self.iprange_2.setGeometry(QtCore.QRect(60, 90, 54, 12))
        self.iprange_2.setObjectName("iprange_2")
        self.oid = QtWidgets.QLineEdit(self.groupBox)
        self.oid.setGeometry(QtCore.QRect(120, 80, 121, 31))
        self.oid.setObjectName("oid")
        self.oid.setText("")
        self.endtimetitel = QtWidgets.QLabel(self.groupBox)
        self.endtimetitel.setGeometry(QtCore.QRect(290, 30, 54, 12))
        self.endtimetitel.setObjectName("endtimetitel")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 54, 12))
        self.label_5.setObjectName("label_5")
        self.note = QtWidgets.QLineEdit(self.groupBox)
        self.note.setGeometry(QtCore.QRect(360, 200, 121, 31))
        self.note.setText("")
        self.note.setObjectName("note")
        self.endTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.endTimeEdit.setGeometry(QtCore.QRect(360, 20, 121, 31))
        self.endTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.datacenter = QtWidgets.QComboBox(self.groupBox)
        self.datacenter.setGeometry(QtCore.QRect(120, 140, 121, 31))
        self.datacenter.setObjectName("datacenter")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.contoer = QtWidgets.QLineEdit(self.groupBox)
        self.contoer.setGeometry(QtCore.QRect(120, 260, 121, 31))
        self.contoer.setText("")
        self.contoer.setObjectName("contoer")
        self.startTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.startTimeEdit.setGeometry(QtCore.QRect(120, 20, 121, 31))
        self.startTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.starttimetitle = QtWidgets.QLabel(self.groupBox)
        self.starttimetitle.setGeometry(QtCore.QRect(50, 30, 54, 12))
        self.starttimetitle.setObjectName("starttimetitle")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(310, 210, 51, 16))
        self.label_10.setObjectName("label_10")
        self.ipaddr = QtWidgets.QLineEdit(self.groupBox)
        self.ipaddr.setGeometry(QtCore.QRect(360, 80, 121, 31))
        self.ipaddr.setText("")
        self.ipaddr.setObjectName("ipaddr")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(310, 90, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(290, 270, 51, 16))
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(310, 150, 31, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(50, 210, 51, 16))
        self.label_7.setObjectName("label_7")
        self.paymode = QtWidgets.QComboBox(self.groupBox)
        self.paymode.setGeometry(QtCore.QRect(120, 200, 121, 31))
        self.paymode.setObjectName("paymode")
        self.paymode.addItem("")
        self.paymode.addItem("")
        self.paymode.addItem("")
        self.paymode.addItem("")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(50, 330, 51, 16))
        self.label_11.setObjectName("label_11")
        self.contoer_2 = QtWidgets.QLineEdit(self.groupBox)
        self.contoer_2.setGeometry(QtCore.QRect(120, 320, 121, 31))
        self.contoer_2.setText("")
        self.contoer_2.setObjectName("contoer_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(290, 330, 51, 16))
        self.label_12.setObjectName("label_12")
        self.paymode_2 = QtWidgets.QComboBox(self.groupBox)
        self.paymode_2.setGeometry(QtCore.QRect(360, 320, 121, 31))
        self.paymode_2.setObjectName("paymode_2")
        self.paymode_2.addItem("")
        self.paymode_2.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 120, 371))
        self.groupBox_2.setObjectName("groupBox_2")
        self.nid = QtWidgets.QComboBox(self.groupBox_2)
        self.nid.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.nid.setObjectName("nid")
        self.manualid = QtWidgets.QLineEdit(self.groupBox_2)
        self.manualid.setGeometry(QtCore.QRect(20, 140, 81, 21))
        self.manualid.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 110, 61, 16))
        self.label.setObjectName("label")
        self.manual = QtWidgets.QPushButton(self.groupBox_2)
        self.manual.setGeometry(QtCore.QRect(20, 190, 75, 23))
        self.manual.setObjectName("pushButton")
		
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.loadid()   #加载ID

        self.nid.currentIndexChanged.connect(self.loaddata)

        self.commit.clicked.connect(self.updata)
		
        self.manual.clicked.connect(self.manualselect)

        #初始化自动补齐姓名
        self.init_combobox()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "更新项目"))
        self.commit.setText(_translate("Dialog", "更新"))
        self.groupBox.setTitle(_translate("Dialog", "更新数据"))
        self.label_8.setText(_translate("Dialog", "联系人"))
        self.endtimetitel.setText(_translate("Dialog", "到期时间"))
        self.label_5.setText(_translate("Dialog", "数据中心"))
        self.datacenter.setItemText(0, _translate("Dialog", "香港"))
        self.datacenter.setItemText(1, _translate("Dialog", "台湾"))
        self.datacenter.setItemText(2, _translate("Dialog", "新加坡"))
        self.datacenter.setItemText(3, _translate("Dialog", "美国纽约"))
        self.datacenter.setItemText(4, _translate("Dialog", "美国华盛顿"))
        self.starttimetitle.setText(_translate("Dialog", "开始时间"))
        self.label_10.setText(_translate("Dialog", "备注"))
        self.label_3.setText(_translate("Dialog", "主IP"))
        self.label_9.setText(_translate("Dialog", "联系方式"))
        self.label_6.setText(_translate("Dialog", "价格"))
        self.label_7.setText(_translate("Dialog", "付款方式"))
        self.paymode.setItemText(0, _translate("Dialog", "支付宝"))
        self.paymode.setItemText(1, _translate("Dialog", "微信"))
        self.paymode.setItemText(2, _translate("Dialog", "银行卡"))
        self.paymode.setItemText(3, _translate("Dialog", "信用卡"))
        self.label_11.setText(_translate("Dialog", "维护人员"))
        self.label_12.setText(_translate("Dialog", "是否删除"))
        self.paymode_2.setItemText(0, _translate("Dialog", "是"))
        self.paymode_2.setItemText(1, _translate("Dialog", "否"))
        self.groupBox_2.setTitle(_translate("Dialog", "选择ID"))
        self.groupBox_2.setTitle(_translate("Dialog", "选择ID"))
        self.label.setText(_translate("Dialog", "手动输入ID"))
        self.manual.setText(_translate("Dialog", "确认"))
        self.iprange_2.setText(_translate("Dialog", "ID"))

    def loadid(self):
        a = db.getdata()
        result = a.seid()
        self.autoid = result
        if result == 1:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","查询ID时出错", QMessageBox.Yes | QMessageBox.No)
            self.form.hide()    #隐藏窗口
        vid = ['']
        for i in result:
            for j in i:
                con = str(j)
                vid.append(con)
        self.nid.addItems(vid)

    def formaft(self,vdate):
        starttime = vdate
        syear = int(starttime[0:4])
        smonth = int(starttime[5:7])
        sday = int(starttime[8:10])
        shour = int(starttime[11:13])
        smi = int(starttime[14:16])
        result = [syear,smonth,sday,shour,smi]
        return result    

    def loaddata(self):
        vid = self.nid.currentText()   #获取ID
        if vid == '':
            pass
        else:
            a = db.getdata()
            result = a.sedata(vid)          
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","查询数据时出错", QMessageBox.Yes | QMessageBox.No)
                self.form.hide()    #隐藏窗口               
            for i in result:
                self.wid = i[0]
                oid = i[2]
                ipaddr = i[3]
                starttime = i[4]
                endtime = i[5]
                price = i[6]
                paymode = i[7]
                vname = i[8]
                phone = i[9]
                note = i[10]
                datacenter = i[11]
                deler = i[13]
                deltime = i[14]
            stime = self.formaft(starttime)
            etime = self.formaft(endtime)

            self.startTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(stime[0], stime[1], stime[2]), QtCore.QTime(stime[3], stime[4])))
            self.endTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(etime[0], etime[1], etime[2]), QtCore.QTime(etime[3], etime[4])))
            #设置IP范围
            self.tmpchange(self.datacenter,datacenter)
            self.tmpchange(self.paymode,paymode)
            self.oid.setText(oid)
            self.ipaddr.setText(ipaddr)
            self.price.setText(price)
            self.contoer.setText(vname)
            self.Contact.setText(phone)
            self.note.setText(note)
            self.contoer_2.setText(deler)
            if deltime == None or deltime == '':
                self.paymode_2.setItemText(0,'否')
                self.paymode_2.setItemText(1,'是')
            else:
                self.paymode_2.setItemText(1,'否')
                self.paymode_2.setItemText(0,'是')                

    def tmpchange(self,con1,con2):  #把选择框中的第一个值改为当前ID的值
        tmp = con1.itemText(0)      #然后判断选择框中的值是否重复
        connum = con1.count()       #最后再把已经替换的值写到最后
        con1.setItemText(0,con2)
        consuzu = []
        for i in range(0,connum):
            consuzu.append(con1.itemText(i))
        if tmp in consuzu:
            pass
        else:
            con1.addItem(tmp)
		
    def manualselect(self):
        newid = self.manualid.text()
        connum = self.nid.count()
        conid = []
        for i in range(0,connum):
            conid.append(self.nid.itemText(i))
        if newid not in conid:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","ID不存在，请重新选择", QMessageBox.Yes | QMessageBox.No)
        else:
            self.nid.setItemText(0,newid)
            self.manualid.setText('')
            self.loaddata()

    def init_combobox(self):
        # 增加选项元素
        items_list = []
        for i in self.autoid:
            items_list.append(i[0])
        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.manualid.setCompleter(self.completer)


    def updata(self):
        starttime = self.startTimeEdit.text()   #获取开始时间文本框内容
        endtime = self.endTimeEdit.text()   #获取到期时间文本框内容    
        oid = self.oid.text()   #获取VPS ID范围文本框内容
        datacenter = self.datacenter.currentText()   #获取数据中心文本框内容
        paymode = self.paymode.currentText()   #获取支付方式文本框内容
        isdelte = self.paymode_2.currentText()   #获取是否删除文本框内容
        ipaddr = self.ipaddr.text()   #获取IP内容
        price = self.price.text()   #获取价格内容
        phone = self.Contact.text()   #获取联系方式内容
        contoer = self.contoer.text()   #获取联系人内容
        note = self.note.text()   #获取备注内容
        deler = self.contoer_2.text()   #获取维护人员内容

        if isdelte == '否':
            isdelte = ''
        elif isdelte == '是':
            if oid != '':
                a = db.getdata()
                result = a.sedata(oid)
                deltime = result[0][13]
                if deltime != '' and deltime != None:
                    isdelte = deltime
                else:
                    isdelte = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
        if oid == '':
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","ID为空，请重新选择", QMessageBox.Yes | QMessageBox.No)
        elif ipaddr == '' or price == '' or contoer == '':
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","必填项不能为空", QMessageBox.Yes | QMessageBox.No)
        elif len(ipaddr) > 20 or len(price) > 8 or len(note) > 50 or len(contoer) > 10 or len(phone) > 15 or len(deler) > 10:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","填入的值长度大于预设长度", QMessageBox.Yes | QMessageBox.No)
        else:
            wid = self.wid  #获取唯一ID值
            info = [wid,oid,ipaddr,starttime,endtime,price,paymode,contoer,phone,note,datacenter,deler,isdelte]
            a = db.postdata()
            result = a.updatevps(info)
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","更新失败，请确认数据库及表是否存在", QMessageBox.Yes | QMessageBox.No)
            else:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","更新成功", QMessageBox.Yes | QMessageBox.No)
                self.form.hide()    #隐藏窗口
                
















