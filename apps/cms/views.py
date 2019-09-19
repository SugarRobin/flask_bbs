from flask import Blueprint,render_template,url_for,views,session,redirect,request,g
from  .forms import LoginForm
from .models import CMSUser
import config
from .decorators import login_required

bp = Blueprint("cms",__name__,url_prefix="/cms")


@bp.route('/')
def index():
    # print(g.cms_user)
    return render_template('cms/cms_index.html')







class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)
    def post(self):
        form = LoginForm(request.form)
        print(1111111)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remeber = form.remeber.data
            print(email)
            print(password)
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remeber:
                    #如果等于true，那么session的持久化为31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message="用户名或密码错误")
        else:
            message = form.get_errors()
            return self.get(message=message)


bp.add_url_rule('/login/',view_func=LoginView.as_view('login')) #as_view('name') 方便url_for('cms.name')找到这个视图函数

@bp.route('/logout/',endpoint='logout')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

@bp.route('/profile/',endpoint='profile')
@login_required
def profile():
    return render_template('cms/cms_profile.html')



