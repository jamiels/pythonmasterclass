from flask import Flask
from flask import request
import mysql.connector as mc
app = Flask(__name__)

@app.route('/products')
def products():
    result_set = run_query('select * from products')
    response = ''
    for n in result_set:
        response = response + "<option>" +n[1] + "</option>"
        print('id:',n[0],'description:',n[1])

    return "<select>" + response + "</select>"

@app.route('/orders')
def show_orders():
    result_set = run_query('select * from orders')
    return str(result_set)

def run_query(sql):
    connection = get_connection()
    result_set = connection.cmd_query(sql)
    result_set_and_meta = connection.get_rows()
    result_set = result_set_and_meta[0]
    connection.close()
    return result_set

def get_connection():
    return mc.connect(user='root', password='jamiel',
                              host='127.0.0.1', database='myfirstdb',
                              auth_plugin='mysql_native_password')





# def get_products():
#     connection = mc.connect(user='root', password='jamiel',
#                               host='127.0.0.1', database='candystore',
#                               auth_plugin='mysql_native_password')
#     result = connection.cmd_query("select * from products")
#     rows = connection.get_rows()
#     connection.close()
#     return rows[0]