from flask import Flask, render_template,request,url_for
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

def ler():
    cur = mysql.connection.cursor()
    cur.execute("USE db_Teste;")
    resultValue = cur.execute("SELECT * FROM db_Tabela")
    if resultValue > 0:
        userDetails = cur.fetchall()
    else:
        userDetails = ''
    return userDetails