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
        <form action="/submitgame" method="get">
            Enter your name: <input type="text" name="username">
            Enter your fav game: <input type="text" name="favgame">
            <input type="submit">
        </form>
    </body>
</html> 
    
    ''' 

@app.route('/submitgame')
def submitgame():
    
    the_name_that_came_in = request.args.get('username')
    return 'You sent me ' + str(the_name_that_came_in).upper()

@app.route('/calc/<somenum>')
def calc(somenum=1):
    return str(int(somenum) * 10)

@app.route('/duh')
def duh():
    return 'Duh!!'