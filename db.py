# -*- coding: utf-8 -*-
import sqlite3
import os
import hashlib  #MD5
import datetime,time

class getdata():
	#MD5
	def md5(self,arg):
		#设置要加密的字符
		text = str(arg)
		#创建对象
		h1 = hashlib.md5()
		#声明encode
		h1.update(text.encode())
		return h1.hexdigest()

	#判断用户是否存在
	def formuser(self,user,passwd):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			vpasswd = self.md5(passwd)			
			sql = "select id from TB_VPS_USERS where USERNAME = '{}' and PASSWORD = '{}'".format(user,vpasswd)
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			if res:
				return 0
			else:
				return 1

		conn.close()
		
	#判断用户数量
	def countuser(self):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()		
			sql = "select id from TB_VPS_USERS"
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			if len(res) < 1:
				return 0
			else:
				return 1

		conn.close()		
		
	#查询ID，用于更新
	def seid(self):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select id from TB_VPS_MANAGE order by id desc"
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res

		conn.close()

	#查询用户信息，用于导出
	def sealluser(self):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select * from TB_VPS_LESSES_USERS"
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res
		conn.close()

	#根据ID查询数据，用于更新数据
	def sedata(self,vid):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select * from TB_VPS_MANAGE where ID = '{}'".format(vid)
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res

		conn.close()

	#查询即将到期
	def freevps(self,s,e,v):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select a.ID,a.STARTIME,a.ENDTIME,a.MAINIP,a.VNAME,a.Contact,b.EMAIL,a.NOTE from TB_VPS_MANAGE a, TB_VPS_LESSES_USERS b WHERE a.VNAME = b.USERNAME and a.Contact = b.PHONE AND DATE(ENDTIME) between DATE('{}') and DATE('{}')".format(s,e)
			if v == 2:
				sql = "select a.ID,a.STARTIME,a.ENDTIME,a.MAINIP,a.VNAME,a.Contact,b.EMAIL,a.NOTE from TB_VPS_MANAGE a, TB_VPS_LESSES_USERS b WHERE a.VNAME = b.USERNAME and a.Contact = b.PHONE AND DATE(ENDTIME) < DATE('now')"
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res

		conn.close()

	#查询续费
	def renewalvps(self,u,p):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			if u != '':
				u = "AND a.VNAME = '{}'".format(u)
			if p != '':
				p = "AND a.Contact = '{}'".format(p)
			sql = "select a.ID,a.STARTIME,a.ENDTIME,a.MAINIP,a.PRICE,a.VNAME,a.Contact,b.EMAIL,a.NOTE from TB_VPS_MANAGE a, TB_VPS_LESSES_USERS b WHERE a.VNAME = b.USERNAME and a.Contact = b.PHONE {} {}".format(u,p)
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res

		conn.close()	


	#第一次登录时判断表是否存在所用
	def firstlogin(self):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select id from TB_VPS_MANAGE limit 0,1"
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return 0
		conn.close()

	#查询所有租户
	def alluser(self):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select USERNAME from TB_VPS_LESSES_USERS"
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res
		conn.close()

	#查询租户联系方式
	def userphone(self,p):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select PHONE from TB_VPS_LESSES_USERS where USERNAME = '{}'".format(p)
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res
		conn.close()

	#查询用户ID
	def usersid(self,p):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select ID from TB_VPS_LESSES_USERS where USERNAME = '{}' and PHONE = '{}'".format(p[0],p[1])
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res
		conn.close()

	#查询续费记录
	def formlog(self,p):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			setime = "and DATE(CREATE_DATE) between DATE('{}') and DATE('{}')".format(p[0],p[1])
			if p[2] == '':
				vip = ''
			else:
				vip = "AND MAINIP LIKE '%{}%'".format(p[2])
			if p[3] == '':
				vname = ''
			else:
				vname = "AND VNAME LIKE '%{}%'".format(p[3])
			if p[4] == '':
				vphone = ''
			else:
				vphone = "AND Contact LIKE '%{}%'".format(p[4])		
			sql = "select ID,STARTIME,OLD_ENDTIME,NEW_ENDTIME,MAINIP,OLD_PRICE,NEW_PRICE,VNAME,Contact,EMAIL,CREATE_DATE from TB_VPS_RENEW where 1 = 1 {} {} {} {}".format(setime,vip,vname,vphone)
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res
		conn.close()	

	#查询VPS数据
	def formvps(self,vpsinfo):
		if len(vpsinfo) == 2:
			startdate = vpsinfo[0]
			enddate = vpsinfo[1]
			startime = "and DATE(STARTIME) between DATE('{}') and DATE('{}')".format(startdate,enddate)
			datacenter = ''
			dname = ''
			delte = ''
			expire = ''
			ipaddr = ''
			phone = ''
		else:
			startdate = vpsinfo[0]
			enddate = vpsinfo[1]
			startime = "and DATE(STARTIME) between DATE('{}') and DATE('{}')".format(startdate,enddate)
			if vpsinfo[2] == '全部':
				datacenter = ""
			else:
				datacenter = "and DATACENTER = '{}'".format(vpsinfo[2]) 
			if vpsinfo[3] != '':
				dname = "and VNAME LIKE '%{}%'".format(vpsinfo[3])
			else:
				dname = ""
			#判断是否删除
			if vpsinfo[4] == '未删除':
				delte = "and DELETEDATE = ''"
			elif vpsinfo[4] == '已删除':
				delte = "and DELETEDATE != ''"
			else:
				delte = ""
			#判断是否到期
			if vpsinfo[5] == '未到期':
				expire = "and DATE(ENDTIME) > DATE('now')"
			elif vpsinfo[5] == '已到期':
				expire = "and DATE(ENDTIME) < DATE('now')"
			else:
				expire = ''
			#模糊查询IP
			if vpsinfo[6] != '':
				ipaddr = "and MAINIP LIKE '%{}%'".format(vpsinfo[6])
			else:
				ipaddr = ''
			#模糊查询联系方式
			if vpsinfo[7] != '':
				phone = "and PHONE LIKE '%{}%'".format(vpsinfo[7])
			else:
				phone = ''
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()			
			sql = "select ID,STARTIME,ENDTIME,MAINIP,DATACENTER,PRICE,PAYMODE,VNAME,Contact,NOTE,CREATE_DATE,DELETER,DELETEDATE from TB_VPS_MANAGE where 1 = 1 {} {} {} {} {} {} {} order by CREATE_DATE desc".format(startime,datacenter,dname,delte,expire,ipaddr,phone)
			cursor = c.execute(sql)
			res = cursor.fetchall()
		except sqlite3.OperationalError:
			return 1
		else:
			return res

		conn.close()


class loaddata():
	def formnew(self):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			#新建用户表
			c.execute('''
				CREATE TABLE TB_VPS_USERS
       			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
       			 USERNAME           TEXT    NOT NULL,
       			 PASSWORD            TEXT     NOT NULL,
       			 ALIAS        TEXT,
       			 EMAIL         TEXT);
       			 ''')
			#新建租户表
			c.execute('''
				CREATE TABLE TB_VPS_LESSES_USERS
       			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
       			 CREATE_DATE 		DATETIME DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')) NOT NULL,
       			 USERNAME           TEXT    NOT NULL,
       			 PHONE            TEXT     NOT NULL,
       			 ALIAS        TEXT,
       			 EMAIL         TEXT NOT NULL,
       			 REMARK			TEXT);
       			 ''')
			#新建续费记录表
			c.execute('''
				CREATE TABLE TB_VPS_RENEW
       			(VID INTEGER PRIMARY KEY AUTOINCREMENT,
       			 ID TEXT NOT NULL,
       			 MAINIP		TEXT NOT NULL,
       			 STARTIME 	TEXT,
       			 OLD_ENDTIME    TEXT NOT NULL,
       			 NEW_ENDTIME    TEXT NOT NULL,
       			 OLD_PRICE		TEXT NOT NULL,
       			 NEW_PRICE	TEXT NOT NULL,
       			 VNAME		TEXT NOT NULL,
       			 Contact	TEXT NOT NULL,
       			 EMAIL		TEXT NOT NULL,
       			 CREATE_DATE TEXT NOT NULL,
       			 NOTE TEXT);
       			 ''')
			#新建数据表
			c.execute('''
				CREATE TABLE TB_VPS_MANAGE
       			(VID INTEGER PRIMARY KEY AUTOINCREMENT,
       			 USERID TEXT NOT NULL,
       			 ID TEXT NOT NULL,
       			 MAINIP		TEXT NOT NULL,
       			 STARTIME 	TEXT,
       			 ENDTIME    TEXT NOT NULL,
       			 PRICE		TEXT NOT NULL,
       			 PAYMODE	TEXT NOT NULL,
       			 VNAME		TEXT NOT NULL,
       			 Contact	TEXT,
       			 NOTE 		TEXT,
       			 DATACENTER	TEXT,
       			 CREATE_DATE TEXT NOT NULL,
       			 DELETER	TEXT,
       			 DELETEDATE	TEXT);
       			 ''')			
		except:
			info = '表创建失败'
			print(info)
		finally:
			conn.commit()
			conn.close()


class postdata():
	#MD5
	def md5(self,arg):
		#设置要加密的字符
		text = str(arg)
		#创建对象
		h1 = hashlib.md5()
		#声明encode
		h1.update(text.encode())
		return h1.hexdigest()

	#注册用户
	def insertuser(self,userinfo):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			password = userinfo[1]
			a = getdata()
			passwd = a.md5(password)
			c.execute("INSERT INTO TB_VPS_USERS (USERNAME,PASSWORD,ALIAS,EMAIL) VALUES ('{}','{}','{}','{}')".format(userinfo[0],passwd,userinfo[2],userinfo[3]))
			conn.commit()
			conn.close()		
		except sqlite3.OperationalError:
			conn.close()
			return 1
		else:
			return 0
			
	#插入VPS信息
	def insertvps(self,vpsinfo):
		create_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			c.execute("INSERT INTO TB_VPS_MANAGE (USERID,ID,MAINIP,PRICE,NOTE,VNAME,Contact,STARTIME,ENDTIME,DATACENTER,PAYMODE,CREATE_DATE) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(vpsinfo[0],vpsinfo[1],vpsinfo[2],vpsinfo[3],vpsinfo[4],vpsinfo[5],vpsinfo[6],vpsinfo[7],vpsinfo[8],vpsinfo[9],vpsinfo[10],create_date))
			conn.commit()
			conn.close()		
		except sqlite3.OperationalError:
			conn.close()
			return 1
		else:
			return 0
			
	#更新VPS信息
	def updatevps(self,i):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			sql = "UPDATE TB_VPS_MANAGE SET (ID,MAINIP,STARTIME,ENDTIME,PRICE,PAYMODE,VNAME,Contact,NOTE,DATACENTER,DELETER,DELETEDATE) = ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') where vid = {}".format(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[0])
			c.execute(sql)
			conn.commit()
			conn.close()
		except sqlite3.OperationalError:
			conn.close()
			return 1
		else:
			return 0

	#更新VPS用户信息
	def updatevpsuserinfo(self,i):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			sql = "UPDATE TB_VPS_MANAGE SET (VNAME,Contact) = ('{}','{}') WHERE USERID = '{}'".format(i[1],i[2],i[0])
			c.execute(sql)
			conn.commit()
			conn.close()
		except sqlite3.OperationalError:
			conn.close()
			return 1
		else:
			return 0

	#更新密码
	def updatepasswd(self,u,p):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			passwd = self.md5(p)
			sql = "UPDATE TB_VPS_USERS SET PASSWORD = '{}' WHERE USERNAME = '{}'".format(passwd,u)
			c.execute(sql)
			conn.commit()
			conn.close()
		except sqlite3.OperationalError:
			conn.close()
			return 1
		else:
			return 0

	#添加租户
	def newuser(self,p):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			sql = "INSERT INTO TB_VPS_LESSES_USERS(USERNAME,PHONE,ALIAS,EMAIL,REMARK) VALUES('{}','{}','{}','{}','{}')".format(p[0],p[1],p[2],p[3],p[4])
			c.execute(sql)
			conn.commit()
			conn.close()
		except sqlite3.OperationalError:
			conn.close()
			return 1
		else:
			return 0

	#添加续费记录
	def addrenew(self,p):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			sql = "INSERT INTO TB_VPS_RENEW(ID,STARTIME,OLD_ENDTIME,NEW_ENDTIME,MAINIP,OLD_PRICE,NEW_PRICE,VNAME,Contact,EMAIL,CREATE_DATE) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10])
			c.execute(sql)
			conn.commit()
			conn.close()
		except sqlite3.OperationalError:
			conn.close()
			return 1
		else:
			return 0

	#更改主数据到期时间和金额
	def changetime(self,p):
		try:
			conn = sqlite3.connect('VPSDB.db')
			c = conn.cursor()
			sql = "UPDATE TB_VPS_MANAGE SET (ENDTIME,PRICE) = ('{}','{}') WHERE ID = '{}' AND VNAME = '{}'".format(p[2],p[3],p[0],p[1])
			c.execute(sql)
			conn.commit()
			conn.close()
		except sqlite3.OperationalError:
			conn.close()
			return 1
		else:
			return 0



		
