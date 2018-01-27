from flask import Flask
from flask_sqlalchemy import SLQAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SLQAlchemy(app)

from views import *

if __name__ == "__main__":
    app.run(debug=True)
