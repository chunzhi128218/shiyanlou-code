from flask import Flask,session,redirect,url_for,escape,request
app = Flask(__name__)

#设置密钥，保证会话安全
app.secret_key = '_5#y23"F4Qsdfsd}'
#随机产生密钥
#python3 -c 'import os; print(os.urandom(16))'


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' %escape(session['username'])
    return 'You are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username></p>
            <p><input type=submit value=Login></p>
        </form>
    '''
@app.route('/logout')
def logout():
    #如果用户名存在，则从会话中移除该用户名
    session.pop('username',None)
    return redirect(url_for('index'))
