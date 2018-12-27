# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QIcon
import socket
import regiest
import index
import db
import hashlib  #MD5
import smtplib
import datetime,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
net = True
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    net = False



class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(505, 350)
        #限制最大窗口size
        Form.setFixedSize(505, 350)
        self.form = Form
        #加载视图控件
        self.header = QtWidgets.QLabel(Form)
        self.header.setGeometry(QtCore.QRect(170, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(160, 110, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.useredit = QtWidgets.QLineEdit(Form)
        self.useredit.setGeometry(QtCore.QRect(230, 100, 113, 31))
        self.useredit.setObjectName("useredit")
        self.passwdedit = QtWidgets.QLineEdit(Form)
        self.passwdedit.setGeometry(QtCore.QRect(230, 160, 113, 31))
        self.passwdedit.setObjectName("passwdedit")
        self.passwdedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(160, 170, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(160, 250, 81, 31))
        self.login.setObjectName("login")
        self.register = QtWidgets.QPushButton(Form)
        self.register.setGeometry(QtCore.QRect(270, 250, 81, 31))
        self.register.setObjectName("register")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        #设置控件名称
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录窗口"))
        self.header.setText(_translate("Form", "请输入用户名和密码"))
        self.username.setText(_translate("Form", "用户名"))
        self.password.setText(_translate("Form", "密  码"))
        self.login.setText(_translate("Form", "登录"))
        self.register.setText(_translate("Form", "注册"))
        #按钮点击事件
        self.login.clicked.connect(self.testuser)
        self.register.clicked.connect(self.jump_to_windows)

    def testuser(self):
        userna = self.useredit.text()   #获取文本框内容
        password = self.passwdedit.text()   #获取文本框内容
        if userna == '':
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","账号不能为空", QMessageBox.Yes | QMessageBox.No)
            self.useredit.setText('')       #设置文本框内容为空
            self.passwdedit.setText('')
        elif password == '':
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","密码不能为空", QMessageBox.Yes | QMessageBox.No)
            self.useredit.setText('')
            self.passwdedit.setText('')
        else:
            #MD5加密密码
            self.b = db.getdata()
            result = self.b.formuser(userna,password)
            if result == 1:
                reply = QtWidgets.QMessageBox.warning(self,"提示信息","您输入的账号或密码不正确", QMessageBox.Yes | QMessageBox.No)
                self.useredit.setText('')
                self.passwdedit.setText('')
            else:
                try:
                    #addrip = self.get_out_ip(self.get_real_url())   #获取外网IP地址
                    #mail = self.sendemail(self.useredit.text(),addrip)    #登录通知
                    mail = 0                                        #如果要开启登录邮件通知，请注释这行，开启上一行
                    if mail == 1:                                   #若无法发送邮件，则不能登录
                        reply = QtWidgets.QMessageBox.warning(self,"提示信息","登录失败，请检查网络", QMessageBox.Yes | QMessageBox.No)
                        self.form.hide()
                    else:
                        self.form.hide()                        #隐藏当前窗口
                        self.form1 = QtWidgets.QMainWindow()    #跳转主窗口
                        self.ui = index.Ui_MainWindow()
                        self.ui.setupUi(self.form1,self.useredit.text())
                        self.form1.show()
                except:
                    if net == False:
                        reply = QtWidgets.QMessageBox.warning(self,"提示信息","请安装requests 和 BeautifulSoup4插件", QMessageBox.Yes | QMessageBox.No)
                    reply = QtWidgets.QMessageBox.warning(self,"提示信息","登录失败，请确认网络是否正常", QMessageBox.Yes | QMessageBox.No)


    def jump_to_windows(self):        #跳转注册窗口
        a = db.getdata()
        result = a.countuser()
        #只允许注册一位用户，之后便不可以再注册，除非删除掉用户
        if result == 1:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","只允许注册一位用户！", QMessageBox.Yes | QMessageBox.No)
        else:
            self.form.hide()            #如果没有self.form.show()这一句，关闭注册界面后就会关闭程序
            form1 = QtWidgets.QDialog()
            ui = regiest.Ui_Dialog()
            ui.setupUi(form1)
            form1.show()
            form1.exec_()
            self.form.show()

    # 获取外网IP
    def get_out_ip(self,url):
        r = requests.get(url)
        r.encoding='gb2312'
        txt = r.text
        addr = (txt[txt.find("<center>") + 8: txt.find("</center>")].split('：'))[2]
        ip = txt[txt.find('[') + 1: txt.find("]")]
        return ip,addr

    # 获取外网IP
    def get_real_url(self,url=r'http://www.ip138.com/'):
        r = requests.get(url)
        txt = r.text
        soup = BeautifulSoup(txt,"html.parser").iframe
        return soup["src"]


    def sendemail(self,loginuser,addrip):
        #获取HOSTNAME和IPADDR
        hostname = socket.gethostname()
        ipList = socket.gethostbyname_ex(hostname)
        ipList = ipList[2]
        #第三方SMTP服务
        #服务器地址
        mail_host = 'mail.xxx.net'
        #邮箱
        mail_user = 'xxx@xxx.net'
        #密码
        mail_pass = 'xxxx'
        #发送人
        sender = 'xxx@xxx.net'
        #接收邮件人
        receivers = ['xxx@sina.com']
        #正文内容
        html = """
        <html>
            <head>
            </head>
            <body>
            <p>登录时间： %(logintime)s</p>
            <p>用户： %(loginuser)s</p>
            <p>计算机名: %(loginhost)s</p>
            <p>IP地址： %(loginip)s</p>
            <p>来自: %(address)s</p>
            </body>
        </html>
        """      

        #创建一个实例
        message = MIMEMultipart()
        message['From'] = 'PyQt5 Test<xxx@xxx.net>'
        message['To'] = 'xxx@sina.com'
        subject = 'VPS管理系统登录提醒'
        message['Subject'] = Header(subject, 'utf-8')
        
        #邮件正文内容
        logintime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        loginip = addrip[0]
        loginaddr = addrip[1]
        html = html % dict(logintime = logintime,loginuser = loginuser,loginhost = hostname,loginip = loginip, address = loginaddr)
        message.attach(MIMEText(html,'html','utf-8'))
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            return 0
        except smtplib.SMTPException:
            return 1
    def closeEvent(self,event):
        sys.exit(app.exec_())

def firstlogin():
    #判断数据库表是否存在
    a = db.getdata()
    result = a.firstlogin()
    #不存在则自动创建表
    if result == 1:
        b = db.loaddata()
        b.formnew()

if __name__ == "__main__":
    #第一次登录时加载TABLE
    firstlogin()
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    window = Ui_Form()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec_())