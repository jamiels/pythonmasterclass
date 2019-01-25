# Author: Deep Datta deepdattax@gmail.com

from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    motd = 'Have a great one!'
    return render_template('index.html',xyz=motd)

@app.route('/submitgame',methods=['POST'])
def submitgame():
    int_num = request.form['Number']
    new_ans = int(int_num)**2
    return str(new_ans)

    
