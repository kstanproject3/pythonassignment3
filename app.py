import os
import datetime
from flask import Flask, flash, request, redirect, render_template, session, url_for
from flask_bcrypt import Bcrypt
from utils.utils import num_there, special_there, Liste
from bson.json_util import dumps
from flask_cors import CORS
from config.db import users, collection

app = Flask(__name__, template_folder='./public')
CORS(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
flask_bcrypt = Bcrypt(app)


@app.route('/login', methods=['GET'])
def login_get():
    try:
        return render_template('login.html')
    except ValueError as e:
        return dumps({'error': str(e)})


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if not username:
        flash('Please insert Username !')
        return redirect('/login')
    elif not password:
        flash('Please insert Password !')
        return redirect('/login')
    else:
        user = list(users.find({"username": username}))
        if len(user) > 0:
            pswd = user[0]['password']
            pw_hash = flask_bcrypt.check_password_hash(pswd, password)
            if pw_hash:
                session['username'] = username
                return redirect('/')
            else:
                flash('Check your credentials please !', 'error')
                return redirect('/login')
        else:
            flash('Check your credentials please !', 'error')
            return redirect('/login')


@app.route('/register', methods=['GET'])
def register_get():
    try:
        return render_template('signup.html')
    except ValueError as e:
        return dumps({'error': str(e)})


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    conf_password = request.form['password_confirmation']
    if password != conf_password:
        flash("It's not the same password")
        return redirect('/login')
    else:
        if 6 < len(password) < 20 and num_there(password) and special_there(password):
            user = list(users.find({"username": username}))
            if len(user) > 0:
                flash("Username already exists", "error")
                return redirect('/login')
            else:
                dico = {"username": username,
                        "name": name,
                        "password": flask_bcrypt.generate_password_hash(password).decode('utf-8')}
                users.insert_one(dico)
                flash("Registration done ! You can now log in !", "correct")
                return redirect('/login')
        else:
            flash("Password should contains at least one number and one special character !")
            return redirect('/login')


@app.route('/', methods=['GET'])
def get_collection():
    if 'username' in session:
        try:
            x = list(collection.find().limit(9))
            for i in range(len(x)):
                x[i].update({"image": Liste[i]})
            return render_template('index.html', data=x)
        except ValueError as e:
            return dumps({'error': str(e)})
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run()
