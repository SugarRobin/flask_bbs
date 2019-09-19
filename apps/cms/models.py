from exts import db
from datetime import datetime
from werkzeug.security import  generate_password_hash,check_password_hash    #加密，解密

class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(50),nullable=False,unique=True)
    join_time = db.Column(db.DateTime,default=datetime.now)

    #对外字段password  对内_password

    @property                         #将password属性化
    def password(self):
        return self._password

    @password.setter                 #将密码加密
    def password(self,raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self,raw_password):        #比对密码
        result = check_password_hash(self.password,raw_password)
        return result

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

