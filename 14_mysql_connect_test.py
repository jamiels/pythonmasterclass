import mysql.connector as mc

print(mc.__version__)


connection = mc.connect(user='root', password='jamiel',
                              host='127.0.0.1', database='sys',
                              auth_plugin='mysql_native_password')





