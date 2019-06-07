from flask import Flask, render_template,request,url_for
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)
mysql = MySQL(app)

def criar(nome,telefone,cpf,email,cargo):
    cur = mysql.connection.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS db_Teste;')
    cur.execute('USE db_Teste;')
    cur.execute('CREATE TABLE IF NOT EXISTS db_Tabela(name varchar(30), telefone varchar(30), cpf varchar(30), email varchar(40), cargo varchar(30), matricula int(4) AUTO_INCREMENT, PRIMARY KEY(matricula));')
    cur.execute("INSERT INTO db_Tabela(name,telefone,cpf,email,cargo) VALUES(%s,%s,%s,%s,%s);",(nome,telefone,cpf,email,cargo))
    mysql.connection.commit()
    cur.close()
    
