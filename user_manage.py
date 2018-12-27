import os
import sys
from PyQt5.QtCore import (QFile, QVariant, Qt)
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QMenu,
        QMessageBox, QTableView, QVBoxLayout)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime,time
import db
#EXCEL
import xlwt

MAC = True
try:
    from PyQt5.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

ID, CREATE_DATE, USERNAME, PHONE, ALIAS, EMAIL, REMARK = range(7)

class UserManage(QDialog):
    def setupUi(self,Dialog,parent=None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(843, 473)
        Dialog.setFixedSize(843, 473)
        self.form = Dialog

        #filename = os.path.join(os.path.dirname(__file__), "VPSDB.db")
        filename = "VPSDB.db"

        #如果已经打开过一次，就不再重新连接
        if QSqlDatabase.contains("qt_sql_default_connection"):
            pass
        else:
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName(filename)

        #绑定数据库TB_VPS_LESSES_USER表
        self.model = QSqlTableModel(self)
        self.model.setTable("TB_VPS_LESSES_USERS")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, "ID")
        self.model.setHeaderData(CREATE_DATE, Qt.Horizontal,"创建时间")
        self.model.setHeaderData(USERNAME, Qt.Horizontal,"用户姓名")
        self.model.setHeaderData(PHONE, Qt.Horizontal,"联系方式")
        self.model.setHeaderData(ALIAS, Qt.Horizontal,"别名")
        self.model.setHeaderData(EMAIL, Qt.Horizontal,"邮箱地址")
        self.model.setHeaderData(REMARK, Qt.Horizontal,"备注")
        self.model.select()

        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionMode(QTableView.SingleSelection)
        self.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.tableView.setColumnHidden(ID, True)
        self.tableView.resizeColumnsToContents()        
        self.tableView.setGeometry(QtCore.QRect(150, 10, 681, 421))
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnWidth(1,140) 	#设置列宽度
        self.tableView.setColumnWidth(2,80) 	#设置列宽度
        self.tableView.setColumnWidth(3,120) 	#设置列宽度
        self.tableView.setColumnWidth(4,56) 	#设置列宽度
        self.tableView.setColumnWidth(5,160) 	#设置列宽度
        self.tableView.setColumnWidth(6,108) 	#设置列宽度

        self.flush = QtWidgets.QPushButton(Dialog)
        self.flush.setGeometry(QtCore.QRect(420, 440, 61, 23))
        self.flush.setObjectName("flush")
        self.exporte = QtWidgets.QPushButton(Dialog)
        self.exporte.setGeometry(QtCore.QRect(630, 440, 61, 23))
        self.exporte.setObjectName("exporte")
        self.adduser = QtWidgets.QPushButton(Dialog)
        self.adduser.setGeometry(QtCore.QRect(490, 440, 61, 23))
        self.adduser.setObjectName("adduser")
        self.deluser = QtWidgets.QPushButton(Dialog)
        self.deluser.setGeometry(QtCore.QRect(560, 440, 61, 23))
        self.deluser.setObjectName("deluser")
        self.sortdata = QtWidgets.QPushButton(Dialog)
        self.sortdata.setGeometry(QtCore.QRect(700, 440, 61, 23))
        self.sortdata.setObjectName("sortdata")
        self.closel = QtWidgets.QPushButton(Dialog)
        self.closel.setGeometry(QtCore.QRect(770, 440, 61, 23))
        self.closel.setObjectName("closel")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 131, 421))
        self.groupBox.setObjectName("groupBox")
        self.phoneEdit = QtWidgets.QLineEdit(self.groupBox)
        self.phoneEdit.setGeometry(QtCore.QRect(20, 120, 91, 31))
        self.phoneEdit.setObjectName("phoneEdit")
        self.userEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userEdit.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.userEdit.setObjectName("userEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 30, 54, 12))
        self.label.setObjectName("label")
        self.mailEdit = QtWidgets.QLineEdit(self.groupBox)
        self.mailEdit.setGeometry(QtCore.QRect(20, 190, 91, 31))
        self.mailEdit.setObjectName("mailEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 54, 12))
        self.label_3.setObjectName("label_3")
        self.commEdit = QtWidgets.QPushButton(self.groupBox)
        self.commEdit.setGeometry(QtCore.QRect(20, 340, 91, 31))
        self.commEdit.setObjectName("commEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 54, 12))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 260, 91, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


        menu = QMenu(self)
        sortByCREATE_DATEAction = menu.addAction("根据创建时间")
        sortByDescriptionAction = menu.addAction("根据用户名称")
        sortByIDAction = menu.addAction("根据用户ID")
        self.sortdata.setMenu(menu)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.flush.clicked.connect(self.refresh)
        self.adduser.clicked.connect(self.addRecord)
        self.deluser.clicked.connect(self.deleteRecord)
        self.exporte.clicked.connect(self.exportExcel)
        sortByCREATE_DATEAction.triggered.connect(lambda:self.sort(CREATE_DATE))
        sortByDescriptionAction.triggered.connect(lambda:self.sort(USERNAME))
        sortByIDAction.triggered.connect(lambda:self.sort(ID))
        self.closel.clicked.connect(self.hidew)    #隐藏窗口
        self.commEdit.clicked.connect(self.queryRecord)
        self.model.beforeUpdate.connect(self.changeitem)    #更新之后
     

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "用户管理"))
        self.exporte.setText(_translate("Dialog", "导出Excel"))
        self.flush.setText(_translate("Dialog", "刷新数据"))
        self.adduser.setText(_translate("Dialog", "添加用户"))
        self.deluser.setText(_translate("Dialog", "删除用户"))
        self.sortdata.setText(_translate("Dialog", "排序"))
        self.closel.setText(_translate("Dialog", "Close"))
        self.groupBox.setTitle(_translate("Dialog", "筛选"))
        self.label_2.setText(_translate("Dialog", "联系方式:"))
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_3.setText(_translate("Dialog", "邮箱地址"))
        self.commEdit.setText(_translate("Dialog", "查询"))
        self.label_4.setText(_translate("Dialog", "创建时间"))
        self.comboBox.setItemText(0, _translate("Dialog", "全部"))
        self.comboBox.setItemText(1, _translate("Dialog", "最近一周"))
        self.comboBox.setItemText(2, _translate("Dialog", "最近一月"))
        self.comboBox.setItemText(3, _translate("Dialog", "最近半年"))
        self.comboBox.setItemText(4, _translate("Dialog", "最近一年"))

    def refresh(self):
        #刷新界面
        self.model.select()

    def hidew(self):
        #隐藏界面
        self.form.hide()

    def addRecord(self):
        row = self.model.rowCount()
        if int(row) == 0:
            QMessageBox.question(self, "提示信息",'请在添加数据中先增加一个用户', QMessageBox.Yes | QMessageBox.No)
        else:
            self.model.insertRow(row)
            index = self.model.index(row, CREATE_DATE)
            self.tableView.setCurrentIndex(index)
            self.tableView.edit(index)


    def deleteRecord(self):
        index = self.tableView.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        #credate = record.value(CREATE_DATE)
        desc = record.value(USERNAME)
        if (QMessageBox.question(self, "提示信息",
                ("确认删除用户 {0} 吗?"
                .format(desc)),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()
        self.model.select()


    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()

    #当更新联系方式后
    def changeitem(self):
        index = self.tableView.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        did = record.value(ID)
        dname = record.value(USERNAME)
        dphone = record.value(PHONE)
        post = db.postdata()
        result = post.updatevpsuserinfo([did,dname,dphone])
        if result == 1:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","更新VPS数据表的用户信息出错", QMessageBox.Yes | QMessageBox.No)

    def queryRecord(self):
        usern = self.userEdit.text()
        phone = self.phoneEdit.text()
        email = self.mailEdit.text()
        cdate = self.comboBox.currentText()
        if usern != '':
            self.model.setFilter(("USERNAME like '%%%s%%'" % (usern)))
        elif phone != '':
            self.model.setFilter(("PHONE like '%%%s%%'" % (phone)))
        elif email != '':
            self.model.setFilter(("EMAIL like '%%%s%%'" % (email)))
        else:
            self.model.setFilter("")
        if cdate == '最近一周':
            ltime = (datetime.datetime.now() + datetime.timedelta(days=-7)).strftime('%Y-%m-%d')
            self.model.setFilter(("DATE(CREATE_DATE) > DATE('%s')" % (ltime)))
        elif cdate == '最近一月':
            ltime = (datetime.datetime.now() + datetime.timedelta(days=-31)).strftime('%Y-%m-%d')
            self.model.setFilter(("DATE(CREATE_DATE) > DATE('%s')" % (ltime)))
        elif cdate == '最近半年':
            ltime = (datetime.datetime.now() + datetime.timedelta(days=-183)).strftime('%Y-%m-%d')
            self.model.setFilter(("DATE(CREATE_DATE) > DATE('%s')" % (ltime)))                 
        elif cdate == '最近一年':
            ltime = (datetime.datetime.now() + datetime.timedelta(days=-365)).strftime('%Y-%m-%d')
            self.model.setFilter(("DATE(CREATE_DATE) > DATE('%s')" % (ltime)))
        else:
            ltime = datetime.datetime.now().strftime('%Y-%m-%d')
        self.model.select()

    def exportExcel(self):
        #从数据查询数据
        getinfo = db.getdata()
        result = getinfo.sealluser()
        if result == 1:
            reply = QtWidgets.QMessageBox.warning(self,"提示信息","查询数据时出现异常", QMessageBox.Yes | QMessageBox.No)
        else:
            workbook = xlwt.Workbook(encoding='utf-8') #创建工作簿
            sheet = workbook.add_sheet("sheet1") #创建工作页
            row0 = [u'ID',u'创建时间',u'姓名',u'联系方式',u'别名',u'邮箱地址',u'备注']
            for i in range(0,len(row0)):
                sheet.write(0,i,row0[i])
            #生成Excel
            num = 1
            for d in result:
                sheet.write(num,0,d[0])
                sheet.write(num,1,d[1])
                sheet.write(num,2,d[2])
                sheet.write(num,3,d[3])
                sheet.write(num,4,d[4])
                sheet.write(num,5,d[5])
                sheet.write(num,6,d[6])
                num += 1
            now_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            if (QMessageBox.question(self, "提示信息",
                    ("确认在本目录下导出VPS联系人信息为Excel吗?"),
                    QMessageBox.Yes|QMessageBox.No) ==
                    QMessageBox.No):
                return
            workbook.save('VPS联系人信息_{}.xls'.format(now_time))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    window = UserManage()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec_())                      