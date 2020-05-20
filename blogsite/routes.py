from flask import Flask, render_template, url_for, flash, redirect, request
# from blogsite.form import RegistrationForm, LoginForm
from blogsite import app
from blogsite.mode import sniff

posts = [
    {
        'author': 'Temp Reading 1:',
        'title': 'WiFi SSID: HaulerAds',
        'date': '12.8 Degrees C'
    },
    {
        'author': 'Temp Reading 2:',
        'title': 'WiFi SSID: BarNote WiFi',
        'date': '13.5 Degrees C'
    }
]


@app.route("/")
@app.route("/home")
def home():
      return render_template('home.html', posts=posts)


@app.route("/temp", methods=['POST'])
def temp():
    if request.method == 'POST':
        return render_template('temp.html', title='Temperature Readings')
    return render_template('home.html')


@app.route("/wifi", methods=['POST'])
def wifi():
    if request.method == 'POST':
        wifi_data = sniff.wifi_scans.view_all()
        print (wifi_data)
        return render_template('wifi.html', title='WiFi Scans', wifi_data=wifi_data)
    return render_template('home.html')


@app.route("/voltage", methods=['POST'])
def voltage():
    if request.method == 'POST':
        return render_template('voltage.html', title='Voltage Readings')
    return render_template('home.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check username/password', 'danger')
    return render_template('login.html', title='Login', form=form)

