from flask import Flask
from flask import redirect
from flask import url_for


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/RedirectHome')
def redirect_func():  # put application's code here
    return redirect('/')


@app.route('/BackToWorld')
def url_for_func():
    return redirect(url_for('HiiWorld_func'))


@app.route('/HiiWorld')
def HiiWorld_func():
    return 'HiiWorld'




if __name__ == '__main__':
    app.run()
