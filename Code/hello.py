from flask import Flask,render_template
app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    #默认name为None
    return render_template('hello.html',name=name)
#将name参数传递到模板变量中
@app.route('/')
def get_hello():
    return  render_template('index.html')
