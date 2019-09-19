from exts import db
from datetime import datetime
from ..cms.models import CMSUser




#文章分类表
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    index = db.Column(db.Integer)


#中间表 tag_article
article_tag_table = db.Table(
    'article_tag',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)

)


#文章标签表
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))



#推荐文章
class Tui(db.Model):
    __tablename__ = 'tui'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))



#文章表
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    title = db.Column(db.String(100))        #标题
    excerpt = db.Column(db.session(200))     #摘要
    category_id = db.Column(db.Integer,db.ForeignKey('category.id')) #文章与分类是一对多的关系
    category = db.relationship("Category",backref='categorys')   #分类表可以通过查询文章

    tags = db.relationship("Tag",secondary=article_tag_table,backref='tags') #标签与文章是多对多的关系

    #user 是通过取出用户表中用户字段
    user_id = db.Column(db.Integer,db.ForeignKey('cms_user.id'))
    user = db.relationship('CMSUser',backref='cmsusers')
    views = db.Column(db.Integer)

    #tui  推荐位与文章表是一对多的关系
    tui_id = db.Column(db.Integer,db.ForeignKey('tui.id'))
    tui = db.relationship("Tui",backref='tuis')

    created_time = db.Column(db.DateTime,default=datetime.now)
    modified_time = db.Column(db.DateTime,default=datetime.now)

#Banner
class Banner(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    text_info = db.Column(db.String(50))   #标题
    img_name = db.Column(db.String(50))    #轮播图
    img_link = db.Column(db.String(100))   #图片链接
    is_active = db.Column(db.Boolean,default=True)   #是否开启

#frendly_link   有情链接
class Link(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    name = db.Column(db.String(50))    #链接名称
    linkurl = db.Column(db.String(100)) #网址




