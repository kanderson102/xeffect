from app import app
from flask import render_template, request, jsonify
from models import User, Settings, Habit, DateEvent
from forms import LoginForm, SignupForm


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', form=form)


@app.route('/signup')
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        pass
    return render_template('signup.html', form=form)


@app.route('/api/v1.0/habits')
def habits():
    pass


@app.route('/api/v1.0/toggle')
def toggle():
    if request.method == 'POST':
        try:
            data = request.get_json()
            count = data['checked']
            # TODO add to database
            response = {"count": count}
        except:
            response = {"status": 'error'}
        return jsonify(response)
    return render_template('index.html')
