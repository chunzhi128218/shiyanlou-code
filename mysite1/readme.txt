创建项目：django-admin startproject 项目名
运行项目：cd 项目名 && python3 manage.py runserver
访问：http：//127.0.0.1:8000/lib 得到hello，world也页面；
浏览/lib/detail得到book书浏览页面；
浏览/admin得到登入页面

对模块models.py编辑book类
python3 manage.py makemigrations为模型的改变生成迁移文件
ipython3 manage.py migrate 来应用数据库迁移

通过对lib/templates/lib/detail.html页面的修改传值到lib/views.py调用后台数据，
之后在lib/urls.py添加访问url的路径实现对页面的操作

