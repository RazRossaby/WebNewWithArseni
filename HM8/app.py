from flask import Flask
from flask import render_template
import datetime
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key = '12345'


@app.route('/')
def HomePage():  # put application's code here
    return render_template('CV.html')



@app.route('/ContactUs')
def ContactForms():  # put application's code here
    return render_template('forms.html')



@app.route('/Hobbies')
def Hobbies():  # put application's code here
    now = datetime.datetime.now()
    return render_template('assignment8.html', firsthobbie='playSoccer', secondhobbie='watch_soccer' , hour=now.hour , teams={'Hapoel Beer Sheva-ISRAEL', 'Manchester United-ENGLAND','Real Madrid-SPAIN'})

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():

    if (request.method == 'GET'):
        if ('name' in request.args):
            input_name = request.args['name']
            found = True
            if (found==True):
                session['name'] = input_name
            if (input_name == ''):
                return render_template('assignment9.html',
                                       users={'user1': {'name': 'Raz', 'email': 'Razrossbi@gmail.com'},'user2': {'name': 'Bar', 'email': 'Bar@walla.com'},
                                              'user3': {'name': 'Mor', 'email': 'Mor@gmail.com'},'user4': {'name': 'Aviva','email': 'Aviva@gmail.com'},
                                              'user5': {'name': 'Ron', 'email': 'Ron@gmail.com'}})
            else:
                return render_template('assignment9.html', name=input_name,
                                       users={'user1': {'name': 'Raz', 'email': 'Razrossbi@gmail.com'},'user2': {'name': 'Bar', 'email': 'Bar@walla.com'},
                                              'user3': {'name': 'Mor', 'email': 'Mor@gmail.com'},'user4': {'name': 'Aviva', 'email': 'Aviva@gmail.com'},
                                              'user5': {'name': 'Ron', 'email': 'Ron@gmail.com'}})

        else:
            return render_template('assignment9.html')
    if (request.method) == 'POST':
        username = request.form['username']
        found = True
        if (found == True):
            session['username'] = username
            return render_template('CV.html', name=username)
        else:
            return render_template('assignment9.html')

    return render_template('assignment9.html')

@app.route('/log_out')
def log_out():  # put application's code here
    session['username'] = ''
    return render_template('CV.html')






















if __name__ == '__main__':
    app.run()
