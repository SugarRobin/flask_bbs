from flask_script import Manager
from bbs import create_app
from flask_migrate import MigrateCommand,Migrate
from  apps.cms import models as  cms_models
from exts import db

CMSUser = cms_models.CMSUser

app = create_app()
manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)



@manager.option('-u','--username',dest="username")
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_cms_user(username,password,email):
    user = CMSUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print("成功添加用户")


if __name__ == '__main__':
    manager.run()
