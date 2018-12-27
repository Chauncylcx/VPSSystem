# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase
import updateobject
import adduser
import db
import change
import datetime,time
import user_manage as usermanage
import freevps
import renewalvps
#EXCEL
import xlrd
import xlwt

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow,loginfo):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1393, 764)
        MainWindow.setFixedSize(1393, 764)
        self.loginfo = loginfo      #登录账号
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.datatable = QtWidgets.QTableWidget(self.centralwidget)
        self.datatable.setGeometry(QtCore.QRect(5, 80, 1382, 631))
        self.datatable.setObjectName("datatable")           #设置表格名称
        self.datatable.setColumnCount(13)                   #定义列数
        self.ColCount = 13
        self.datatable.verticalHeader().setVisible(False)   #隐藏垂直表头
        self.datatable.setAlternatingRowColors(True)        #设置条纹
        self.datatable.setEditTriggers(QAbstractItemView.NoEditTriggers)    #关闭双击修改
        self.datatable.setColumnWidth(0,80)                 #设置列宽度，时间列长度较宽
        self.datatable.setColumnWidth(1,120)
        self.datatable.setColumnWidth(2,120)
        self.datatable.setColumnWidth(10,130)
        self.datatable.setColumnWidth(12,130)

        #从数据库获取数据，刷新表格
        self.tabledata()
        
        #加载控件
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1393, 81))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(420, 20, 54, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(620, 18, 54, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.datacenter = QtWidgets.QComboBox(self.groupBox)
        self.datacenter.setGeometry(QtCore.QRect(620, 38, 69, 22))
        self.datacenter.setObjectName("datacenter")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.datacenter.addItem("")
        self.expire = QtWidgets.QComboBox(self.groupBox)
        self.expire.setGeometry(QtCore.QRect(420, 40, 69, 22))
        self.expire.setObjectName("expire")
        self.expire.addItem("")
        self.expire.addItem("")
        self.expire.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(710, 18, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(710, 38, 110, 22))
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_2.setGeometry(QtCore.QRect(820, 38, 110, 22))
        self.dateEdit_2.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.delte = QtWidgets.QComboBox(self.groupBox)
        self.delte.setGeometry(QtCore.QRect(520, 40, 69, 22))
        self.delte.setObjectName("delte")
        self.delte.addItem("")
        self.delte.addItem("")
        self.delte.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(520, 20, 54, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.select = QtWidgets.QPushButton(self.groupBox)
        self.select.setGeometry(QtCore.QRect(960, 40, 75, 21))
        self.select.setObjectName("select")
        self.export = QtWidgets.QPushButton(self.groupBox)
        self.export.setGeometry(QtCore.QRect(1050, 40, 75, 21))
        self.export.setObjectName("export")
        self.iplabel = QtWidgets.QLabel(self.groupBox)
        self.iplabel.setGeometry(QtCore.QRect(100, 20, 54, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.iplabel.setFont(font)
        self.iplabel.setObjectName("iplabel")
        self.ipEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ipEdit.setGeometry(QtCore.QRect(90, 40, 81, 21))
        self.ipEdit.setObjectName("ipEdit")
        self.label_phone = QtWidgets.QLabel(self.groupBox)
        self.label_phone.setGeometry(QtCore.QRect(210, 20, 54, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.phoneEdit = QtWidgets.QLineEdit(self.groupBox)
        self.phoneEdit.setGeometry(QtCore.QRect(200, 40, 81, 21))
        self.phoneEdit.setObjectName("phoneEdit")
        self.title_vname = QtWidgets.QLabel(self.groupBox)
        self.title_vname.setGeometry(QtCore.QRect(330, 20, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_vname.setFont(font)
        self.title_vname.setObjectName("title_vname")
        self.vnameEdit = QtWidgets.QComboBox(self.groupBox)
        self.vnameEdit.setEditable(True)
        self.vnameEdit.setGeometry(QtCore.QRect(310, 40, 81, 21))
        self.vnameEdit.setObjectName("vnameEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1476, 23))
        self.menubar.setObjectName("menubar")
        self.menuData_Select = QtWidgets.QMenu(self.menubar)
        self.menuData_Select.setObjectName("menuData_Select")
        self.menuUserMessage = QtWidgets.QMenu(self.menubar)
        self.menuUserMessage.setObjectName("menuUserMessage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInsert = QtWidgets.QAction(MainWindow)
        self.actionInsert.setStatusTip("")
        self.actionInsert.setObjectName("actionInsert")
        self.actionAdd_User = QtWidgets.QAction(MainWindow)
        self.actionAdd_User.setObjectName("actionAdd_User")
        self.actionUserMea = QtWidgets.QAction(MainWindow)
        self.actionUserMea.setObjectName("actionUserMea")
        self.actionFree = QtWidgets.QAction(MainWindow)
        self.actionFree.setObjectName("actionFree")
        self.actionrenewal = QtWidgets.QAction(MainWindow)
        self.actionrenewal.setObjectName("actionrenewal")
        self.actiondelteete = QtWidgets.QAction(MainWindow)
        self.actiondelteete.setObjectName("actiondelteete")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menuData_Select.addAction(self.actionInsert)
        self.menuData_Select.addAction(self.action)
        self.menuData_Select.addAction(self.actionFree)
        self.menuData_Select.addAction(self.actionrenewal)
        self.menuUserMessage.addAction(self.actionAdd_User)
        self.menuUserMessage.addAction(self.actionUserMea)
        self.menubar.addAction(self.menuData_Select.menuAction())
        self.menubar.addAction(self.menuUserMessage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #菜单栏点击事件
        #更新记录
        self.action.triggered.connect(self.jump_to_updateobject)
        #新添加一条记录
        self.actionInsert.triggered.connect(self.jump_to_adduser)
        #修改密码
        self.actionAdd_User.triggered.connect(self.jump_to_change)
        #用户管理
        self.actionUserMea.triggered.connect(self.jump_to_usermanage)
        #到期提醒
        self.actionFree.triggered.connect(self.jump_to_freevps)
        #到期提醒
        self.actionrenewal.triggered.connect(self.jump_to_renewal)
        #初始化自动补齐姓名
        self.init_combobox()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VPS管理系统"))
        self.datatable.setSortingEnabled(True)  #排序

        __sortingEnabled = self.datatable.isSortingEnabled()
        
        #设置名称
        #请修改数据中心，
        self.datatable.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "是否到期"))
        self.label_3.setText(_translate("MainWindow", "数据中心"))
        self.datacenter.setItemText(0, _translate("MainWindow", "全部"))
        self.datacenter.setItemText(1, _translate("MainWindow", "香港"))
        self.datacenter.setItemText(2, _translate("MainWindow", "台湾"))
        self.datacenter.setItemText(3, _translate("MainWindow", "新加坡"))
        self.datacenter.setItemText(4, _translate("MainWindow", "美国"))
        self.expire.setItemText(0, _translate("MainWindow", "全部"))
        self.expire.setItemText(1, _translate("MainWindow", "未到期"))
        self.expire.setItemText(2, _translate("MainWindow", "已到期"))
        self.label_4.setText(_translate("MainWindow", "开始时间段"))
        self.delte.setItemText(0, _translate("MainWindow", "全部"))
        self.delte.setItemText(1, _translate("MainWindow", "未删除"))
        self.delte.setItemText(2, _translate("MainWindow", "已删除"))
        self.label_6.setText(_translate("MainWindow", "是否删除"))
        self.select.setText(_translate("MainWindow", "查询"))
        self.export.setText(_translate("MainWindow", "导出Excel"))
        self.menuData_Select.setTitle(_translate("MainWindow", "数据管理"))
        self.menuUserMessage.setTitle(_translate("MainWindow", "系统设置"))
        self.actionInsert.setText(_translate("MainWindow", "新建项目"))
        self.actionAdd_User.setText(_translate("MainWindow", "修改密码"))
        self.actionUserMea.setText(_translate("MainWindow",'用户管理'))
        self.actionFree.setText(_translate("MainWindow",'到期提醒'))
        self.actionrenewal.setText(_translate("MainWindow",'续期管理'))
        self.actiondelteete.setText(_translate("MainWindow", "删除用户"))
        self.action.setText(_translate("MainWindow", "更新项目"))
        self.iplabel.setText(_translate("MainWindow", "IP地址"))
        self.label_phone.setText(_translate("MainWindow", "联系方式"))
        self.title_vname.setText(_translate("MainWindow", "联系人"))
        
        self.now_date_year = int(datetime.datetime.now().strftime("%Y"))
        self.next_date_year = int(datetime.datetime.now().strftime("%Y")) - 1
        self.now_date_month = int(datetime.datetime.now().strftime("%m"))
        self.now_date_day = int(datetime.datetime.now().strftime("%d"))
        #设置时间控件显示当前时间
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(self.now_date_year, self.now_date_month, self.now_date_day)))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.next_date_year, self.now_date_month, self.now_date_day)))

        #查询按钮点击事件，查询数据
        self.select.clicked.connect(self.selectdata)
        #导出按钮点击事件，查询数据
        self.export.clicked.connect(self.expexcel)

    def tabledata(self):
        #默认一年
        starttime = datetime.datetime.now().strftime("%Y-%m-%d")
        endtime = (datetime.datetime.now()+datetime.timedelta(days=-365)).strftime("%Y-%m-%d")
        vpsinfo = [endtime,starttime]
        #连接数据库查询
        a = db.getdata()
        sqldata = a.formvps(vpsinfo)
        #如果没有数据
        if sqldata == 1:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","查询出错", QMessageBox.Yes | QMessageBox.No)
            sqldata = []
        #设置行数为查询出来的行数
        rows = len(sqldata)
        self.datatable.setRowCount(rows)
        self.rowCount = rows
        #设置行头
        self.datatable.setHorizontalHeaderLabels(['ID','开始时间','到期时间','主IP','数据中心','价格','付款方式','联系人','联系方式','备注','创建时间','维护人员','删除时间'])
        #循环定义表格的内容
        inum = 0
        for i in sqldata:
            jnum = 0
            for j in i:
                item = QtWidgets.QTableWidgetItem()
                if type(j) == int:
                    j = str(j)
                newItem = QTableWidgetItem(j)   #设置内容
                if i[12] != '' and i[12] != None:
                    newItem.setBackground(QtGui.QColor('red'))  #如果过期，则显示为红色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter) #居中显示
                self.datatable.setItem(inum, jnum, newItem) #设置j行i列的内容为Value
                jnum += 1
            inum += 1

    def jump_to_adduser(self):  
        form1 = QtWidgets.QDialog()
        ui = adduser.Ui_Dialog()
        ui.setupUi(form1,self.loginfo)
        form1.show()
        form1.exec_()
        #更新后刷新数据
        self.selectdata()

    def jump_to_updateobject(self):     #跳转更新页面
        form1 = QtWidgets.QDialog()
        ui = updateobject.Ui_Dialog()
        ui.setupUi(form1,self.loginfo)
        form1.show()
        form1.exec_()
        #更新后刷新数据
        self.selectdata()


    def jump_to_change(self):       #跳转更改密码页面
        form1 = QtWidgets.QDialog()
        ui = change.Ui_Dialog()
        ui.setupUi(form1,self.loginfo)
        form1.show()
        form1.exec_()

    def jump_to_usermanage(self):       #跳转用户管理页面
        form1 = QtWidgets.QDialog()
        ui = usermanage.UserManage()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()

    def jump_to_freevps(self):       #跳转到期提醒页面
        form1 = QtWidgets.QDialog()
        ui = freevps.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()

    def jump_to_renewal(self):       #跳转续期管理页面
        form1 = QtWidgets.QDialog()
        ui = renewalvps.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        #更新后刷新数据
        self.selectdata()

    def init_combobox(self):
        # 增加选项元素
        items_list = []
        a = db.getdata()
        result = a.alluser()
        if result != 1:
            for i in result:
                items_list.append(i[0])
        for i in range(len(items_list)):
            self.vnameEdit.addItem(items_list[i])
        self.vnameEdit.setCurrentIndex(-1)

        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.vnameEdit.setCompleter(self.completer)


    def selectdata(self):
        dateEdit = self.dateEdit.text()   #获取开始时间文本框内容
        dateEdit_2 = self.dateEdit_2.text()   #获取到期时间文本框内容
        datacenter = self.datacenter.currentText()   #获取数据中心文本框内容
        dname = self.vnameEdit.currentText()   #获取联系人文本框内容
        delte = self.delte.currentText()   #获取是否删除文本框内容      
        expire = self.expire.currentText()   #获取是否过期文本框内容
        ipedit = self.ipEdit.text()           #获取IP地址
        phoneEdit = self.phoneEdit.text()      #获取联系方式
        vpsinfo = [dateEdit,dateEdit_2,datacenter,dname,delte,expire,ipedit,phoneEdit]
        a = db.getdata()
        sqldata = a.formvps(vpsinfo)
        if sqldata == 1:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","查询出错", QMessageBox.Yes | QMessageBox.No)
            sqldata = []
        rows = len(sqldata)
        self.datatable.setRowCount(rows)
        self.rowCount = rows
        #设置行头
        self.datatable.setHorizontalHeaderLabels(['ID','开始时间','到期时间','主IP','数据中心','价格','付款方式','联系人','联系方式','备注','创建时间','维护人员','删除时间']) 
        #同tabledata函数类似
        inum = 0
        for i in sqldata:
            jnum = 0
            for j in i:
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                if type(j) == int:
                    j = str(j)
                newItem = QTableWidgetItem(j)
                if i[12] != '' and i[12] != None:
                    newItem.setBackground(QtGui.QColor('red'))  #如果过期，则显示为红色
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter) #居中显示
                self.datatable.setItem(inum, jnum, newItem) #设置j行i列的内容为Value
                jnum += 1
            inum += 1

    def expexcel(self):
        workbook = xlwt.Workbook(encoding='utf-8') #创建工作簿
        sheet = workbook.add_sheet("sheet1") #创建工作页
        row0 = [u'ID',u'开始时间',u'到期时间',u'主IP',u'数据中心',u'价格',u'付款方式',u'联系人',u'联系方式',u'备注',u'创建时间',u'维护人员',u'删除时间']
        for i in range(0,len(row0)):
            sheet.write(0,i,row0[i])
        data = []
        for i in range(0,self.rowCount):
            rocont = []
            for j in range(0,self.ColCount):
                a = self.datatable.item(i,j)
                if a == None:
                    a = ""
                else:
                    a = a.text()
                rocont.append(a)
            data.append(rocont)
        #生成Excel
        num = 1
        for d in data:
            sheet.write(num,0,d[0])
            sheet.write(num,1,d[1])
            sheet.write(num,2,d[2])
            sheet.write(num,3,d[3])
            sheet.write(num,4,d[4])
            sheet.write(num,5,d[5])
            sheet.write(num,6,d[6])
            sheet.write(num,7,d[7])
            sheet.write(num,8,d[8])
            sheet.write(num,9,d[9])
            sheet.write(num,10,d[10])
            sheet.write(num,11,d[11])
            sheet.write(num,12,d[12])
            num += 1
        now_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if (QMessageBox.question(self, "提示信息",
                ("确认在本目录下导出为Excel吗?"),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        workbook.save('VPS信息_{}.xls'.format(now_time))