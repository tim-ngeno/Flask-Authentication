from flask import render_template, redirect, url_for, flash, request, session
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, EmailForm,LoginForm, UpdateAccountInfo
from flaskblog.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_password, colors=form.colors.data)

        db.session.add(user)
        db.session.commit()
        flash(f"Account created, re-enter your email to log in ", 'success')
        return redirect(url_for('email'))
    return render_template('register.html', title='Register', form=form)

@app.route('/email', methods=['GET', 'POST'])
def email():
    form = EmailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            session['attempt_user_email'] = user.email
            session['attempt_user_color'] = user.colors
            return redirect(url_for('login'))
        else:
            flash(f"E-mail not associated with any account, kindly check e-mail or register", 'danger')
    return render_template('email.html', title='Email Confirmation', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    attempt_user_email=session.get('attempt_user_email', None)
    if attempt_user_email is None:
        return redirect(url_for('email'))
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    form.email.data = attempt_user_email
    if form.validate_on_submit():
        user = User.query.filter_by(email=attempt_user_email).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash(f"Login Failed!", 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountInfo()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f"Account Updated!", 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username 
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))