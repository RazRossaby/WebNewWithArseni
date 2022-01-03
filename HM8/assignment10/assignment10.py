from flask import Blueprint, render_template
import app as app
from flask import Flask
from flask import render_template
import datetime
from flask import request
from flask import session
from flask import flash
from interact_with_DB import *
from flask import redirect


assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         template_folder='templates')





@assignment10.route('/assignment10')
def users():
    query= 'select * from users;'
    users= interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html',users=users)

@assignment10.route('/insert_user', methods=['post'])
def insert():
    name= request.form['name']
    email = request.form['email']
    query="insert into users (Name,Email) values ('%s','%s');" % (name,email)
    interact_db(query=query, query_type='commit')
    flash(f'Account created!', 'success')
    return redirect('/assignment10')

@assignment10.route('/delete_user_name', methods=['post'])
def delete():
    name= request.form['name']
    query="delete from users where Name ='%s';" %name
    interact_db(query=query, query_type='commit')
    flash(f'Account deleted!', 'success')
    return redirect('/assignment10')

@assignment10.route('/delete_user_email', methods=['post'])
def deleteemail():
    email= request.form['email']
    query="delete from users where Email ='%s';" %email
    interact_db(query=query, query_type='commit')
    flash(f'Account deleted!', 'success')
    return redirect('/assignment10')


@assignment10.route('/updatemail', methods=['post'])
def updatemail():
    name= request.form['name']
    newemail= request.form['email']
    query="Update users set Email='%s' where Name='%s';" %(newemail,name)
    interact_db(query=query, query_type='commit')
    flash(f'Account Updated!', 'success')
    return redirect('/assignment10')

@assignment10.route('/updatename', methods=['post'])
def updatename():
    email = request.form['email2']
    newname= request.form['name2']
    query="Update users set Name='%s' where Email='%s';" %(newname,email)
    interact_db(query=query, query_type='commit')
    flash(f'Account Updated!', 'success')
    return redirect('/assignment10')