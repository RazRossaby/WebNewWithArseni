from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)


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






if __name__ == '__main__':
    app.run()
