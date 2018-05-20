from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'bf1f507a883457ccf1081f6506f74ab5'

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
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
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

if __name__ == "__main__":
    app.run(debug=True)
