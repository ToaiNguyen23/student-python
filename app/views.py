from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import Student

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    students =  Student.query.all()
    print(students)
    return render_template("home.html", user = current_user,students = students)

@views.route('/addstudent', methods=['GET','POST'])
@login_required
def addstudent():
    message='';
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        numberphone = request.form.get('numberphone')
        gmailaddress = request.form.get('gmailaddress')

        if len(name) == 0:
            message = 'A Name is required!'
        elif len(address) == 0:
            message = 'A Address is required!'
        elif len(numberphone) == 0:
            message = 'A Numberphone is required!'
        else:
            new_student = Student(name=name,address=address,numberphone=numberphone,gmailaddress=gmailaddress)
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('views.home'))

    return render_template("addstudent.html", user = current_user,message=message)
@views.route('/delete/<int:id>')
@login_required
def delete(id):
    print(id)
    student_delete = Student.query.get_or_404(id)

    try:
        db.session.delete(student_delete)
        db.session.commit()
        return redirect(url_for('views.home'))
    except:
        return "Delete error"

@views.route('/update/<int:id>', methods=['GET','POST'])
@login_required
def update(id):
    print(id)
    student_update = Student.query.get_or_404(id)

    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        numberphone = request.form.get('numberphone')
        gmailaddress = request.form.get('gmailaddress')

        student_update.name = name
        student_update.address = address
        student_update.numberphone = numberphone
        student_update.gmailaddress = gmailaddress
        db.session.add(student_update)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template("updatestudent.html", user = current_user,student = student_update)
