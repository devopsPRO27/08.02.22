import os
import random

from flask import Flask
from flask import redirect, url_for, render_template, request

app = Flask(__name__)

global users
users = {}


@app.route('/')
def home_page():
    return f'guy is the best'


@app.route('/king')
def king_page():
    return 'tomer is a king'


@app.route('/quotes')
def quotes_page():
    lis = ['old keys dont open new doors', 'be a warrior not a worrier', 'no pain ni gain ', 'pizza is life ',
           'with great power comes great responsibilty']
    i = random.randint(0, 4)
    return f'<h1 style="color:aqua;"> the quote of the day is :{lis[i]}</h1>'


@app.route('/htmlexm')
def htmlexm():
    return '<body><h1>hodi is king </h1><p> this is paragraph <br> cake is life</p> \
    <h1 style="color:aqua;"> this text is blue</h1><button> hothaifa </button><form><p>first name\
     <input id="11" name="firstnametxt" type="password" required=true></p><p>Email <input id="12" name="emailtxt" \
     type="email" required=true ></p><button>ok</button></form></body>'


@app.route('/hello/<name>')
def hello_name(name):
    return f'hello {name}'


# targil - create URL which gets 2 numbers and print their sum
# 'sum/3/4' --> will display: 3 + 4 = 7
@app.route('/calc/<int:x>/<int:y>')
def calc(x, y):
    return f'{x} + {y} = {x + y} '


@app.route('/calc2/<int:x>')
def calc2(x):
    return f'{x % 10} + {x // 10} = {x // 10 + x % 10} '


@app.route('/pizza')
def pizza():
    return redirect('https://www.w3schools.com/python/')


@app.route('/admin')
def admin_page():
    return f'welcome SIR   ADMIN'


@app.route('/user/<username>')
def hello_user(username):
    return f"hiiii user {username}"


@app.route('/login/<name>')
def login(name):
    if name == "oriel":
        return redirect(url_for("admin_page"))
    else:
        return redirect(url_for('hello_user', username=name))


# flast folder structrue:
# -- flask_program.py
# -- trmplates\  pages.html
# -- static\     style.css
# -- static\     myjs.js
# -- static\     images

@app.route('/flask')
def my_flask():
    return render_template('hello.html', x=13, y=18)


@app.route('/d')
@app.route('/dict')
def dic_temp():
    grades = {'py': 99, 'ch': 64, 'math': 100, 'sport': 12}
    # for x,v in grades.items():
    #    print(x,v)
    return render_template('python.html', d=grades)


@app.route('/form')  # get
def form2():
    return render_template('a.html')


@app.route('/form_acc', methods=['POST'])
def form():
    global user_name
    user_name = request.form['name']
    if request.form['psw'] == "123456":
        return f'your name is =>{user_name}'
    else:
        return f'lekh lekh ata lo lidor'


@app.route('/form_acc1', methods=['POST'])
def form22():
    user_name = request.form['name']
    password=request.form['psw']
    users[user_name]=password

@app.route('/showAll')
def showAllUsers():
    return render_template('python.html', d=users)




app.run()
