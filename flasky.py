import os

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
x = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
# manager
maneger = Manager(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    maneger.run()
