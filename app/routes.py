from app.models import User
from app.forms import RegisterForm, LoginForm, BlogUpdateForm
from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required, logout_user, login_user


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html", title="SomaSoma")

@app.route('/courses')
def courses():
    return render_template("courses.html", title='Courses')

@app.route('/blog')
def blog():
    return render_template("blog.html", title='Blog')

@app.route('/events')
def events():
    return render_template("events.html", title='Events')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username Or Email')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Welcome')
        return redirect(url_for('dashboard'))
    return render_template("login.html", title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have been registered now get out')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", title='Dashboard')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/blogupdate', methods=['GET', 'POST'])
@login_required
def update_blog():
    form = BlogUpdateForm()
    return render_template('blog-update.html', title='Update Blog', form=form)