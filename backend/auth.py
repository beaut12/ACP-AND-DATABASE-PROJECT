from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()

        if not user:
            flash('Username does not exist.')
        elif not check_password_hash(user.password, request.form.get('password')):
            flash('Incorrect password.')
        else:
            login_user(user)
            return redirect(url_for('views.dashboard'))

    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        if User.query.filter_by(username=request.form.get('username')).first():
            flash('Username already taken.')
        elif User.query.filter_by(email=request.form.get('email')).first():
            flash('Email already registered.')
        else:
            new_user = User(
                fullname=request.form.get('fullname'),
                email=request.form.get('email'),
                username=request.form.get('username'),
                password=generate_password_hash(request.form.get('password')),
                profile_picture=None
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('views.dashboard'))

    return render_template('signup.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
