from app import app
from flask import render_template, request, jsonify
from models import User
from views import LoginForm


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
    return render_template('index.html', form=form)
