import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from forms import NameForm

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'nhDaXvbs1T-HnaU5kgAdJDHtQnuutXhY7xM2cn_fdMo'

db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
# manager
maneger = Manager(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/1/')
def fun1():
    return ''


@app.route('/2/')
def fun2():
    return redirect(url_for('fun1'))


if __name__ == '__main__':
    # app.run()
    maneger.run()
