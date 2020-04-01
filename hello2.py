from flask import Flask
app=Flask(__name__)

#如果访问/，返回Index Page
@app.route('/')
def index():
    return 'Index Page'

#如果访问/hello,返回Hello,World!
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    #显示用户名
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #显示提交整型的用户id的结果，注意int是将字符串转换成整型
    return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #显示/path/之后的路径名
    return 'Subpath {}'.format(subpath)
