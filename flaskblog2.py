from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFrom, LoginFrom

app = Flask(__name__)
app.config['SECRET_KEY'] = '0e588ce36cb1382dcdebfabf7dc5345c'

posts = [
    {
        'author': 'Joey',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'data_posted': 'April 20, 2022'
    },
    {
        'author': 'Ross',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'data_posted': 'April 21, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account create for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check the email and password!', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__== '__main__':
    app.run(debug=True)