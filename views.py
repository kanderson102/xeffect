from app import app
from flask import render_template, request, jsonify
from models import User
from forms import LoginForm, SignupForm


@app.route('/', methods=['GET', 'POST'])
def index():
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


@app.route('/login')
def login():
    form = LoginForm
    return render_template('login.html', form=form)


@app.route('/signup')
def signup():
    form = SignupForm
    return render_template('signup.html', form=form)
