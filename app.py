from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_pyfile('config.py')
Bootstrap(app)
db = SQLAlchemy(app)

from views import *

if __name__ == "__main__":
    app.run(debug=True)
