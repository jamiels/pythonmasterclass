# Author: Deep Datta deepdattax@gmail.com

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

import mysql.connector as mc
app = Flask(__name__)

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html',products=products)

@app.route('/submitOrder',methods=['POST'])
def submit_order():
    quantity = request.form['quantity']
    product = request.form['product']
    insert_order(quantity,product)
    return redirect('/') #Order received!'

@app.route('/orders')
def display_orders():
    connection = get_connection()
    result = connection.cmd_query("select * from orders")
    rows = connection.get_rows()
    connection.close()
    return str(rows[0])


def insert_order(qty,product_id):
    connection = get_connection()
    sql = 'INSERT INTO ORDERS(quantity,product_id) values('+qty+','+product_id+')'
    print(sql)
    connection.cmd_query(sql)
    connection.commit()
    connection.close()

def get_products():
    connection = get_connection()
    result = connection.cmd_query("select * from products")
    rows = connection.get_rows()
    connection.close()
    return rows[0]

def get_connection():
    return mc.connect(user='root', password='jamiel',
                              host='127.0.0.1', database='candystore',
                              auth_plugin='mysql_native_password')


