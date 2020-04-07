from flask import Flask
app = Flask(__name__)

#如果访问/,返回Index Page
@app.route('/')
def index():
    return 'Index Page'
#如果访问/hello，返回Hello world！
@app.route('/hello')
def hello():
    return 'Hello.World!'
