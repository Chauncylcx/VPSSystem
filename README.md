# VPSSystem
使用PyQt5开发的VPS管理系统

# 运行环境
版本：Python3
插件：PyQt5，PyQt5-tools，xlwt，requests，BeautifulSoup4
数据库：SQLITE3 本地

        

# 文件
--登录窗口
Login.py  

--主窗口
Index.py

 --注册窗口
Regiest.py

--数据库操作驱动
db.py	 

 --更改密码窗口
change.py

--添加用户窗口
adduser.py

--到期提醒窗口
freevps.py

--用户管理窗口
user_manage.py

--续期管理窗口
renewalvps.py  

-- 续期记录窗口
renewlog.py

 --新建项目窗口
newinfo.py  

 --Sqlite3数据库文件
VPSDB.db	

# 说明
login.py
首先会判断是否是第一次登录，若是，则会自动生成四个表，一个用户表，一个数据表，一个VPS用户表，一个续费日志表，然后会判断输入的账号密码的格式是否正确，如果正确就到数据库中对比是否存在此用户，不正确就弹窗提示。
只允许创建一位用户，创建之后便不可以再创建了，除非把之前的用户从数据库中删除
如果登录成功，就会发邮件通知，并且会记录计算机名和IP地址(目前已关闭，如果想开启，就在代码中97行处修改)
邮件使用第三方邮箱，可以用QQ邮箱，新浪邮箱等，然后配置账号密码等信息。
增加获取外网IP的功能，若无法上网，则不可登录(邮件提醒默认关闭，请修改)
	
regiest.py
从登录窗口跳到注册窗口，输入账号密码姓名邮箱等，若格式没有问题，就记录到数据库，并且密码是由MD5加密的
	
index.py
主窗口显示数据，可以根据一些条件进行查询，排序等等。可以在菜单栏添加数据，修改数据，修改用户密码等, 添加新功能：模糊查询，导出Excel
如果是已经删除的，会用红底标识
一些特定的下拉列表内容，需要自己手动修改，比如IP范围，数据中心等等。
因为有很多中文字符，所有修改方法就不过多叙述了
	
adduser.py
新建用户界面，新添加一个用户, 新项目之前需要新添加一个用户，然后才能添加新项目
	
newinfo.py
新建项目窗口，新添加一条记录，
时间控件已经设置为默认时间，其他内容填好之后会判断必填项是否为空，长度等是否合格，合格就写入数据库，不合格就弹窗提示
一些特定的下拉列表内容，需要自己手动修改，比如支付方式，数据中心等等。
	
freevps.py
到期提醒窗口
可以选择到期时间，然后勾选之后可以点击发送邮件。注：邮箱信息尚未配置
如果同一个用户有几个VPS同时过期，只会发送一次邮件

user_manage.py
用户管理界面
双击单元格可以修改内容，回车就会更改了
可以筛选用户，添加用户，删除用户，导出用户信息
添加用户时，用户名、联系方式、邮箱地址不能为空
	
updateobject.py
更新项目窗口
首先打开的时候会从数据库中加载ID到选择中，然后每选择一个ID，就会根据ID从数据库中查询数据，然后写到数据显示的文本框中。修改后点击确认，如果ID为空，就会提示不能更新，或者输入的值格式不对或长度不对也会不能更新
ID使用模糊查询方式
一些特定的下拉列表内容，需要自己手动修改，比如支付方式，数据中心等等。
	
change.py
更改密码窗口
如果输入的密码和前密码一致，并且后输入的密码格式没有问题，就可以修改密码

renewalvps.py
续期管理窗口
先根据用户名或联系方式查询到相关用户的VPS，然后勾选之后再选择续期时间跟金额，
手动发送邮件指的是 点击确认续期之后，会修改数据库的数据，然后发邮件提醒用户续费成功，若因为网络等原因导致邮件发送失败，就需要手动发送一遍，勾选之前选择的用户
用户名跟联系方式采用模糊查询
续费记录会跳到其他窗口，可查询续费记录
	
renewlog.py
续费记录窗口
可以通过IP，联系人，联系方式和续费时间来查询续费日志，还可以导出Excel
IP，联系人，联系方式 均采用模糊查询
	
db.py
包含各个部分连接数据库的函数，SQL语句

VPSDB.db
SQLITE3 数据库文件，如果没有这个文件，当建表的时候会自动生成


# 示例图

![Image text](https://github.com/Chauncylcx/VPSSystem/blob/master/picture/login.png)
![Image text](https://github.com/Chauncylcx/VPSSystem/blob/master/picture/index.png)
![Image text](https://github.com/Chauncylcx/VPSSystem/blob/master/picture/remerb.png)
![Image text](https://github.com/Chauncylcx/VPSSystem/blob/master/picture/update.png)
![Image text](https://github.com/Chauncylcx/VPSSystem/blob/master/picture/usermanage.png)
      
