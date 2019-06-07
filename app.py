from flask import Flask, render_template,request,url_for
from flask_mysqldb import MySQL
from bancoDoApp import lerBanco, criarBanco,bancoCargo
import yaml, Pessoa



app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))

app.config["MYSQL_HOST"] = db['mysql_host']
app.config["MYSQL_USER"] = db['mysql_user']
app.config["MYSQL_PASSWORD"] = db['mysql_password']
app.config["MYSQL_DB"] = db['mysql_db']


mysql = MySQL(app)


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastro",methods = ["GET","POST"])
def cadastro():
    if(request.method == "POST"):
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        cargo = request.form.get("cargo")
        Pessoa.Funcionario(nome,telefone,cpf,email,cargo,0)
        criarBanco.criar(nome,telefone,cpf,email,cargo);
        return render_template("index.html")
    return render_template("cadastro.html")
    

@app.route("/lista_cadastrados")
def lista_cadastrados():
    teste = lerBanco.ler()
    if(teste == ""):
        return render_template("listarFunc.html", userDetails=[])
    return render_template("listarFunc.html", userDetails= teste)

@app.route("/delete_Cargo/<matricula>", methods = ['POST'])
def delete_cargo(matricula):
    if(request.method == "POST"):
        print(matricula)
        # mat 
        #matricula = request.form.get("matricula")
        cur = mysql.connection.cursor()
        cur.execute("USE db_Teste;")
        cur.execute("""DELETE FROM db_Tabela WHERE matricula = %s;""",(str(matricula)));
        mysql.connection.commit()
        #bancoCargo.mudar(cargo,id)
        cur.close()
    return render_template("index.html")
    
@app.route("/atualizar_Cargo/<matricula>", methods = ["GET",'POST'])
def atualizar_cargo(matricula):
    cur = mysql.connection.cursor()
    cur.execute("USE db_Teste;")
    print(request.method)
    if(request.method == "POST"):
        cur.execute("""UPDATE db_Tabela SET cargo = %s WHERE matricula = %s;""",(str(matricula)));
        mysql.connection.commit()
        #bancoCargo.mudar(cargo,id)
        cur.close()

    func = cur.execute("""SELECT cargo FROM db_Tabela WHERE matricula = %s;""",(matricula))
    
    
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)