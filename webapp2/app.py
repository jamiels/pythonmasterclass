from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
        <head><title>Form Website</title></head>
    <body>
        <form action="/submitgame">
        <p>How old are you?</p><br />
        <input type="text" name="Number">
        <input type="submit">
        </form>
    </body>
    </html>
    '''
@app.route('/submitgame')
def submitgame():
    int_num = request.args.get('Number')
    new_ans = int(int_num)**2
    return str(new_ans)

    
