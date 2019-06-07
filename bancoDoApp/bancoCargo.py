from flask import Flask, render_template,request,url_for
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
mysql = MySQL(app)

def mudar(cargo,matricula):
    cur = mysql.connection.cursor()
    cur.execute('USE db_Teste;')
    cur.execute("UPDATE db_Tabela SET cargo = %s WHERE matricula = %s;",(cargo, matricula));
    mysql.connection.commit()
    cur.close()