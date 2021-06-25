from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.datastructures import RequestCacheControl
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET','POST'])
def login():
    message = '';
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
        else:
            message = 'Your authentication information is incorrect. Please try again!'
        if len(username) == 0:
            message = 'A Username is required!'
        elif len(password) == 0:
            message = 'A Password is required!'
        print(message)

    return render_template("login.html",user = current_user,message=message)

@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up/', methods=['GET','POST'])
def sing_up():
    message = '';
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        username = request.form.get('username')
        password = request.form.get('password')
        passwordconfirm = request.form.get('passwordconfirm')
        email = request.form.get('email')
       
        if len(firstname) < 1:
            message = 'A First Name is required!'
        elif len(username) < 1:
            message = 'A Username is required!'
        elif len(password) < 1:
            message = 'A Password is required!'
        elif password != passwordconfirm:
            message = '''The Password don't match'''
        else:
            new_user = User(firstname=firstname,username=username,password=generate_password_hash(password, method='sha256'),email=email)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html",user = current_user,message=message)