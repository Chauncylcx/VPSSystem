from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import db
import datetime,time
#EXCEL
import xlwt

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1207, 600)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(3, 60, 1200, 535))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)   #隐藏垂直表头
        self.tableWidget.setSortingEnabled(True)  #排序
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)    #关闭双击修改
        self.tableWidget.setColumnCount(11)
        self.ColCount = 11                                      #用于导出
        self.tableWidget.setColumnWidth(1,120)                 #设置列宽度，时间列长度较宽
        self.tableWidget.setColumnWidth(2,120)                 #设置列宽度，时间列长度较宽
        self.tableWidget.setColumnWidth(3,120)                 #设置列宽度，时间列长度较宽
        self.tableWidget.setColumnWidth(10,120)                 #设置列宽度，时间列长度较宽

        self.commitp = QtWidgets.QPushButton(Dialog)
        self.commitp.setGeometry(QtCore.QRect(670, 30, 71, 23))
        self.commitp.setObjectName("commitp")
        self.expdp = QtWidgets.QPushButton(Dialog)
        self.expdp.setGeometry(QtCore.QRect(760, 30, 71, 23))
        self.expdp.setObjectName("expdp")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(184, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(287, 10, 54, 12))
        self.label_2.setObjectName("label_2")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(260, 30, 85, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.phoneLabel = QtWidgets.QLabel(Dialog)
        self.phoneLabel.setGeometry(QtCore.QRect(380, 10, 54, 12))
        self.phoneLabel.setObjectName("phoneLabel")
        self.phoneEdit = QtWidgets.QLineEdit(Dialog)
        self.phoneEdit.setGeometry(QtCore.QRect(360, 30, 85, 22))
        self.phoneEdit.setObjectName("phoneEdit")
        self.ipaddrEdit = QtWidgets.QLineEdit(Dialog)
        self.ipaddrEdit.setGeometry(QtCore.QRect(160, 30, 85, 22))
        self.ipaddrEdit.setObjectName("ipaddrEdit")
        self.dateLabel = QtWidgets.QLabel(Dialog)
        self.dateLabel.setGeometry(QtCore.QRect(460, 10, 54, 12))
        self.dateLabel.setObjectName("dateLabel")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(460, 30, 85, 22))
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(545, 30, 85, 22))
        self.dateEdit_2.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit_2.setObjectName("dateEdit_2")

        self.now_date_year = int(datetime.datetime.now().strftime("%Y"))
        self.next_date_year = int(datetime.datetime.now().strftime("%Y")) - 1
        self.now_date_month = int(datetime.datetime.now().strftime("%m"))
        self.now_date_day = int(datetime.datetime.now().strftime("%d"))
        #设置时间控件显示当前时间
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(self.now_date_year, self.now_date_month, self.now_date_day)))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.next_date_year, self.now_date_month, self.now_date_day)))

        #加载数据
        self.loaddata()

        #查询按钮
        self.commitp.clicked.connect(self.loaddata)

        #导出按钮
        self.expdp.clicked.connect(self.expexcel)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "续费记录"))
        self.commitp.setText(_translate("Dialog", "查询"))
        self.expdp.setText(_translate("Dialog", "导出Excel"))
        self.label.setText(_translate("Dialog", "IP地址"))
        self.label_2.setText(_translate("Dialog", "联系人"))
        self.phoneLabel.setText(_translate("Dialog", "联系方式"))
        self.dateLabel.setText(_translate("Dialog", "续费时间"))

    def loaddata(self):
        #默认一年
        startdate = self.dateEdit.text()
        enddate = self.dateEdit_2.text()
        vip = self.ipaddrEdit.text()
        vname = self.nameEdit.text()
        vphone = self.phoneEdit.text()
        p = [startdate,enddate,vip,vname,vphone]
        #连接数据库查询
        a = db.getdata()
        self.content = a.formlog(p)
        #self.content = 1
        if self.content == 1:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","查询失败，请检查TB_VPS_RENEW表是否存在", QMessageBox.Yes | QMessageBox.No)
            self.content = [()]
        self.tableWidget.setHorizontalHeaderLabels(['ID','开始时间','旧到期时间','新到期时间','主IP','旧价格','新价格','联系人','联系方式','邮箱地址','续费时间'])
        rows = len(self.content)
        self.rowCount = rows
        self.tableWidget.setRowCount(rows)
        #循环定义表格的内容
        inum = 0
        for i in self.content:
            jnum = 0
            for j in i:
                item = QtWidgets.QTableWidgetItem()
                if type(j) == int:
                    j = str(j)
                newItem = QTableWidgetItem(j)   #设置内容
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter) #居中显示
                self.tableWidget.setItem(inum, jnum, newItem) #设置j行i列的内容为Value
                jnum += 1
            inum += 1

    def expexcel(self):
        workbook = xlwt.Workbook(encoding='utf-8') #创建工作簿
        sheet = workbook.add_sheet("sheet1") #创建工作页
        row0 = [u'ID',u'开始时间',u'旧到期时间',u'新到期时间',u'主IP',u'旧价格',u'新价格',u'联系人',u'联系方式',u'邮箱地址',u'续费时间']
        for i in range(0,len(row0)):
            sheet.write(0,i,row0[i])
        data = []
        for i in range(0,self.rowCount):
            rocont = []
            for j in range(0,self.ColCount):
                a = self.tableWidget.item(i,j)
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
            num += 1
        now_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if (QMessageBox.question(self, "提示信息",
                ("确认在本目录下导出为Excel吗?"),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        workbook.save('VPS续费记录信息_{}.xls'.format(now_time))

