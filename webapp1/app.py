from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def monkey():
    return  '''
    <html>
    <head>
        <title>Favorite Game</title>
    </head>
    <body>
    <a href="/whatsup?page=2">Next</a>
        <form action="/processLogin" method="get">
            Enter your name: <input type="text" name="username">
            Enter your fav game: <input type="password" name="favgame">
            <input type="submit">
        </form>
    </body>
</html> 
    
    ''' 

@app.route('/processLogin')
def login():
    user = request.args.get('username')
    # user against db
    is_valid_user = False
    if is_valid_user:
        message = "You're good <a href=/>Back</a>"
    else:
        message = "Wrong user <a href=/>Back</a>"
    return message


@app.route('/submitgame')
def submitgame(blahblah):
    #value = request.args.get('tid')
    the_name_that_came_in = request.args.get('username')
    return 'You sent me ' + str(the_name_that_came_in).upper()

@app.route('/calc/<somenum>')
def calc(somenum=1):
    return str(int(somenum) * 10)

@app.route('/process')
def duh():
    return 'Duh!!'

@app.route('/whatsup')
def bro():
    request.args.get('uid')
    return 'Bro!!!??'