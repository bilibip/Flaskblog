from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app, bcrypt, db
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': "Daniel RIVIERE",
        'title': "My second flask app",
        'content': "First post content"
    },
    {
        'author': "Test User",
        'title': "Second post message",
        'content': "Second post content"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You can login now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'test':
            flash('You have been logged in!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Login unsucessful! Please check your Email and password', 'danger')
            return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)
