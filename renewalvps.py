from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import db
import renewlog
import datetime,time
import calendar
#EMAIL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1153, 500)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(220, 10, 930, 480))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.verticalHeader().setVisible(False)   #隐藏垂直表头
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)    #关闭双击修改
        self.tableWidget.setColumnWidth(1,110)                 #设置列宽度，时间列长度较宽
        self.tableWidget.setColumnWidth(2,110)                 #设置列宽度，时间列长度较宽

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 201, 190))
        self.groupBox.setObjectName("groupBox")
        self.usernameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.usernameEdit.setGeometry(QtCore.QRect(70, 30, 81, 31))
        self.usernameEdit.setObjectName("usernameEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 54, 12))
        self.label_4.setObjectName("label_4")
        self.phoneEdit = QtWidgets.QLineEdit(self.groupBox)
        self.phoneEdit.setGeometry(QtCore.QRect(70, 80, 81, 31))
        self.phoneEdit.setObjectName("phoneEdit")
        self.SelectButton = QtWidgets.QPushButton(self.groupBox)
        self.SelectButton.setGeometry(QtCore.QRect(70, 130, 81, 31))
        self.SelectButton.setObjectName("SelectButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 220, 201, 270))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label.setObjectName("label")
        self.expir = QtWidgets.QComboBox(self.groupBox_2)
        self.expir.setGeometry(QtCore.QRect(70, 30, 81, 31))
        self.expir.setObjectName("expir")
        self.expir.addItem("")
        self.expir.addItem("")
        self.expir.addItem("")
        self.expir.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.priceEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.priceEdit.setGeometry(QtCore.QRect(70, 80, 81, 31))
        self.priceEdit.setObjectName("priceEdit")
        self.commitp = QtWidgets.QPushButton(self.groupBox_2)
        self.commitp.setGeometry(QtCore.QRect(70, 130, 81, 31))
        self.commitp.setObjectName("commitp")
        self.emailp = QtWidgets.QPushButton(self.groupBox_2)
        self.emailp.setGeometry(QtCore.QRect(100, 180, 91, 31))
        self.emailp.setObjectName("emailp")
        self.renewlog = QtWidgets.QPushButton(self.groupBox_2)
        self.renewlog.setGeometry(QtCore.QRect(5, 180, 88, 31))
        self.renewlog.setObjectName("renewlog")

        #加载数据
        self.loaddata()

        #查询按钮
        self.SelectButton.clicked.connect(self.loaddata)

        #确认续费按钮
        self.commitp.clicked.connect(self.TrueRenew)

        #续费记录按钮
        self.renewlog.clicked.connect(self.jump_to_log)

        #发送邮件按钮
        self.emailp.clicked.connect(self.mailcontent)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "续期管理"))
        self.groupBox.setTitle(_translate("Dialog", "查询"))
        self.label_3.setText(_translate("Dialog", "用 户 名："))
        self.label_4.setText(_translate("Dialog", "联系方式："))
        self.SelectButton.setText(_translate("Dialog", "查询"))
        self.groupBox_2.setTitle(_translate("Dialog", "续期"))
        self.label.setText(_translate("Dialog", "续期时间："))
        self.expir.setItemText(0, _translate("Dialog", "一个月"))
        self.expir.setItemText(1, _translate("Dialog", "一季度"))
        self.expir.setItemText(2, _translate("Dialog", "半年"))
        self.expir.setItemText(3, _translate("Dialog", "一年"))
        self.label_2.setText(_translate("Dialog", "价格增加："))
        self.commitp.setText(_translate("Dialog", "确认续期"))
        self.emailp.setText(_translate("Dialog", "手动发送邮件"))
        self.renewlog.setText(_translate("Dialog", "续费记录"))

    def loaddata(self):
        u = self.usernameEdit.text()
        p = self.phoneEdit.text()
        if u == '' and p == '':
            u = 'xxx'
        #连接数据库查询
        a = db.getdata()
        self.content = a.renewalvps(u,p)
        if self.content == 1:
            self.content = [()]
        self.tableWidget.setHorizontalHeaderLabels(['ID','开始时间','到期时间','主IP','价格','联系人','联系方式','邮箱地址','备注'])
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

    def TrueRenew(self):
        renewtime = self.expir.currentText()
        if renewtime == '一个月':
            addm = 1
        elif renewtime == '一季度':
            addm = 3
        elif renewtime == '半年':
            addm = 6
        elif renewtime == '一年':
            addm = 12
        else:
            addm = 1 

        #若续费金额未填，则为0
        priceadd = self.priceEdit.text()
        if priceadd == '':
            priceadd = "0"
        #先得到勾选的值
        ondata = []
        inum = 0
        for i in self.content:
            jnum = 0
            for j in i:
                if jnum == 0:
                    ifon = self.tableWidget.item(inum,jnum).checkState()
                    if ifon == 2:
                        tmpon = [self.tableWidget.item(inum,jnum).text()]
                        for pf in range(1,8):
                            tmpon.append(self.tableWidget.item(inum,jnum+pf).text())
                        ondata.append(tmpon)
                jnum += 1
            inum += 1
        if ondata == []:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","请勾选要续费的VPS", QMessageBox.Yes | QMessageBox.No)
            return 
        if (QMessageBox.question(self, "提示信息",
                ("确认对已勾选的VPS进行续费吗?"),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return

        #记录续费信息
        newdata = []
        for i in ondata:
            index = 0
            newlist = []
            for j in i:
                #记录添加后的金额
                if index == 4:
                    if priceadd.isdigit():
                        newlist.append(j)
                        newlist.append(str('%.2f'%float(float(j)+float(priceadd))))
                        index += 1
                        continue
                newlist.append(j)
                #记录续费后的时间
                if index == 2:
                    timeStruct = datetime.datetime.strptime("{}".format(j), "%Y-%m-%d %H:%M")
                    a = self.addmonths(timeStruct,addm)
                    lasttime = a.strftime("%Y-%m-%d %H:%M")
                    newlist.append(lasttime)
                #记录当前续费时间
                if index == 7:
                    newlist.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))                
                index += 1
            newdata.append(newlist)

        post = db.postdata()
        mailinfo = [[renewtime,newdata[0][9]]]
        yn = True
        #修改主数据表的到期时间和金额
        for i in newdata:
            #vid = i[0], vname = i[7], endtime = i[3], new_price = i[6]
            p = [i[0],i[7],i[3],i[6]]
            result = post.changetime(p)
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","修改主数据表的到期时间和金额时出错", QMessageBox.Yes | QMessageBox.No)
                yn = False
            else:
                #添加续费记录到数据库
                for j in newdata:
                    result = post.addrenew(j)
                    if result == 1:
                        reply = QtWidgets.QMessageBox.warning(self,"提示信息","添加续费记录时出错", QMessageBox.Yes | QMessageBox.No)
                        yn = False
            mailinfo.append([i[4],i[3]])
        self.loaddata()

        #发送邮件
        if yn:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","续费成功,正在发送提醒邮件...", QMessageBox.Yes | QMessageBox.No)
            result = self.sendemail(mailinfo)
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","续费提醒邮件发送失败，请检查之后手动发送", QMessageBox.Yes | QMessageBox.No)
            else:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","续费提醒邮件发送成功", QMessageBox.Yes | QMessageBox.No)


    def mailcontent(self):
        renewtime = self.expir.currentText() 

        #先得到勾选的值
        ondata = []
        inum = 0
        for i in self.content:
            jnum = 0
            for j in i:
                if jnum == 0:
                    ifon = self.tableWidget.item(inum,jnum).checkState()
                    if ifon == 2:
                        tmpon = [self.tableWidget.item(inum,jnum).text()]
                        for pf in range(1,8):
                            tmpon.append(self.tableWidget.item(inum,jnum+pf).text())
                        ondata.append(tmpon)
                jnum += 1
            inum += 1

        if ondata == []:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","请勾选要发送提醒邮件的VPS", QMessageBox.Yes | QMessageBox.No)
            return

        mailinfo = [[renewtime,ondata[0][7]]]
        for i in ondata:
            mailinfo.append([i[3],i[2]])


        if (QMessageBox.question(self, "提示信息",
                ("确认对已勾选的用户发送提醒邮件吗?"),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return

        #发送邮件
        result = self.sendemail(mailinfo)
        if result == 1:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","续费提醒邮件发送失败，请检查邮箱配置以及网络状态", QMessageBox.Yes | QMessageBox.No)
        else:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","续费提醒邮件发送成功", QMessageBox.Yes | QMessageBox.No)

    def jump_to_log(self):     #跳转更新页面
        form1 = QtWidgets.QDialog()
        ui = renewlog.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()

    #增加月份函数
    def addmonths(self,begindate,months):
        Yearmonth = ((0,31,28,31,30,31,30,31,31,30,31,30,31),(0,31,29,31,30,31,30,31,31,30,31,30,31))
        n = begindate.year*12 + begindate.month - 1
        n = n + months
        ryear = int(n / 12)
        rmonth = n%12 + 1
        rday = begindate.day
        if calendar.isleap(ryear):
            if rday > Yearmonth[1][rmonth]:
                rday = Yearmonth[1][rmonth]
        else:
            if rday > Yearmonth[0][rmonth]:
                rday = Yearmonth[0][rmonth]
        return begindate.replace(year=ryear, month=rmonth, day = rday)

    def sendemail(self,info):
        #第三方SMTP服务
        #服务器地址
        mail_host = 'mail.xxxx.com'
        #邮箱地址和密码
        mail_user = 'xxx@xxx.com'
        mail_pass = 'xxx'
        #发件人
        sender = 'xxx@xxx.com'
        #接收邮件人
        receivers = [info[0][1]]
        #正文内容
        html = """
        <html>
            <head>
            </head>
            <body>
            <p>您的VPS已成功续期%(months)s！</p>
            %(cont)s
            </body>
        </html>
        """      

        #创建一个实例
        message = MIMEMultipart()
        message['From'] = 'PyQt5 Test<xxx@xxx.comt>'
        message['To'] = '{}'.format(info[0][1])
        subject = 'VPS续费成功提醒'
        message['Subject'] = Header(subject, 'utf-8')
        
        #邮件正文内容
        content = ""
        for i in info:
            if i == info[0]:
                pass
            else:
                content = content + "<p>IP地址： {}</p>\n<p>到期时间： {}</p>\n\n".format(i[0],i[1])
        html = html % dict(months=info[0][0],cont=content)
        message.attach(MIMEText(html,'html','utf-8'))
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            return 0
        except:
            return 1