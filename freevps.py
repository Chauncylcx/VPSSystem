from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import db
import datetime,time
#EMAIL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(810, 445)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(3, 60, 803, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)   #隐藏垂直表头
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)    #关闭双击修改

        self.tableWidget.setColumnCount(8)
        self.commitp = QtWidgets.QPushButton(Dialog)
        self.commitp.setGeometry(QtCore.QRect(260, 30, 71, 23))
        self.commitp.setObjectName("commitp")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 54, 12))
        self.label_2.setObjectName("label_2")
        self.ynexper = QtWidgets.QComboBox(Dialog)
        self.ynexper.setGeometry(QtCore.QRect(160, 30, 69, 22))
        self.ynexper.setObjectName("ynexper")
        self.ynexper.addItem("")
        self.ynexper.addItem("")
        self.expir = QtWidgets.QComboBox(Dialog)
        self.expir.setGeometry(QtCore.QRect(60, 30, 69, 22))
        self.expir.setObjectName("expir")
        self.expir.addItem("")
        self.expir.addItem("")
        self.expir.addItem("")
        self.expir.addItem("")
        self.emailp = QtWidgets.QPushButton(Dialog)
        self.emailp.setGeometry(QtCore.QRect(360, 30, 71, 23))
        self.emailp.setObjectName("emailp")

        enddate = (datetime.datetime.now()+datetime.timedelta(days=5)).strftime("%Y-%m-%d")
        #加载数据
        self.loaddata(enddate,1)

        #查询按钮
        self.commitp.clicked.connect(self.selectdata)

        #发送邮件按钮
        self.emailp.clicked.connect(self.mailcontent)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "到期提醒"))
        self.commitp.setText(_translate("Dialog", "查询"))
        self.label.setText(_translate("Dialog", "最近到期"))
        self.label_2.setText(_translate("Dialog", "是否到期"))
        self.ynexper.setItemText(0, _translate("Dialog", "未到期"))
        self.ynexper.setItemText(1, _translate("Dialog", "已到期"))
        self.expir.setItemText(0, _translate("Dialog", "5"))
        self.expir.setItemText(1, _translate("Dialog", "10"))
        self.expir.setItemText(2, _translate("Dialog", "15"))
        self.expir.setItemText(3, _translate("Dialog", "30"))
        self.emailp.setText(_translate("Dialog", "发送邮件"))

    def loaddata(self,enddate,v):
        #默认一年
        startdate = datetime.datetime.now().strftime("%Y-%m-%d")
        #连接数据库查询
        a = db.getdata()
        self.content = a.freevps(startdate,enddate,v)
        if self.content == 1:
            self.content = [(1,2,3,4,5,6,7,8),(11,12,13,14,15,16,17,18),(21,22,23,24,25,26,27,28)]
        self.tableWidget.setHorizontalHeaderLabels(['ID','开始时间','到期时间','主IP','联系人','联系方式','邮箱地址','备注'])
        rows = len(self.content)
        self.tableWidget.setRowCount(rows)
        #循环定义表格的内容
        inum = 0
        for i in self.content:
            jnum = 0
            for j in i:
                item = QtWidgets.QTableWidgetItem()
                if type(j) == int:
                    j = str(j)
                if jnum == 0:
                    checkBox = QTableWidgetItem(j)
                    checkBox.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget.setItem(inum, jnum, checkBox) #设置j行i列的内容为Value
                else:
                    newItem = QTableWidgetItem(j)   #设置内容
                    newItem.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter) #居中显示
                    self.tableWidget.setItem(inum, jnum, newItem) #设置j行i列的内容为Value
                jnum += 1
            inum += 1

    def selectdata(self):
        freeday = self.expir.currentText()
        ynexp = self.ynexper.currentText()
        enddate = (datetime.datetime.now()+datetime.timedelta(days=int(freeday))).strftime("%Y-%m-%d")
        version = 1
        if ynexp == '已到期':
            version = 2    
        self.loaddata(enddate,version)   


        
    def mailcontent(self):
        #先得到勾选的值
        ondata = []
        inum = 0
        for i in self.content:
            jnum = 0
            for j in i:
                if jnum == 0:
                    ifon = self.tableWidget.item(inum,jnum).checkState()
                    if ifon == 2:
                        tmpon = [self.tableWidget.item(inum,jnum).text(),self.tableWidget.item(inum,jnum+4).text(),self.tableWidget.item(inum,jnum+5).text(),self.tableWidget.item(inum,jnum+6).text(),self.tableWidget.item(inum,jnum+3).text()]
                        ondata.append(tmpon)
                jnum += 1
            inum += 1
        if ondata == []:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","请勾选要发送邮件的列表", QMessageBox.Yes | QMessageBox.No)

        #如果有多个IP地址，就合在一起
        truecon = {}
        #记录联系方式，作为字典头
        listp = []
        index = 1
        for i in ondata:
            if index == 1:
                truecon[i[2]] = i
            a = truecon.get(i[2],'1')
            #若为1，则代表不存在,就初始化
            if a == '1':
                truecon[i[2]] = i
                listp.append(i[2])
            else:
                #如果已经存在且不是第一个，就把IP追加上去
                if index != 1:
                    truecon[i[2]].append(i[4])
                else:
                    listp.append(i[2])
            index += 1

        if (QMessageBox.question(self, "提示信息",
                ("确认对已勾选的用户发送提醒邮件吗?"),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return

        #开始发送邮件
        ipaddr = ''
        for i in truecon.values():
            for j in range(0,len(i)):
                emailaddr = i[3]
                if j > 3:
                    ipaddr = ipaddr + " " + i[j]
            result = self.sendemail(ipaddr,emailaddr)
            #发送失败则提醒发送失败
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","用户 {} 提醒邮件发送失败，请检查网络或账户状态".format(i[1]), QMessageBox.Yes | QMessageBox.No)
            else:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","用户 {} 提醒邮件发送成功！".format(i[1]), QMessageBox.Yes | QMessageBox.No)
            ipaddr = ''



    def sendemail(self,ipaddr,emailaddr):
        #第三方SMTP服务
        #服务器地址
        mail_host = 'mail.xxx.net'
        #邮箱地址和密码
        mail_user = 'xxxt@xxx.net'
        mail_pass = 'xxxx'
        #发件人
        sender = 'xxx@xxx.net'
        #接收邮件人
        receivers = [emailaddr]
        #正文内容
        html = """
        <html>
            <head>
            </head>
            <body>
            <p>您的VPS即将过期，请尽快联系我续费</p>
            <p>IP地址： %(ipaddr)s</p>
            </body>
        </html>
        """      

        #创建一个实例
        message = MIMEMultipart()
        message['From'] = 'PyQt5 Test<xxx@xxx.net>'
        message['To'] = '{}'.format(emailaddr)
        subject = 'VPS即将过期提醒'
        message['Subject'] = Header(subject, 'utf-8')
        
        #邮件正文内容
        html = html % dict(ipaddr=ipaddr)
        message.attach(MIMEText(html,'html','utf-8'))
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            return 0
        except:
            return 1
