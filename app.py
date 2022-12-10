from flask import Flask,render_template, request
import pandas as pd
import hashlib

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login")

@app.route('/layout')
def layout():
    return render_template("layout.html")

@app.route('/tables')
def tables():
    return render_template("tables.html")

@app.route('/transacciones')
def transacciones():
    logs = pd.read_csv('logs.csv', sep=";")
    logs_1 = {'n':logs["n"].to_list(),
              'id':logs["ID"].to_list(),
              'timestamp':logs["timestamp"].to_list(),
              'descripcion':logs["agent.type"].to_list(),
              'hash': [ hashlib.sha256(str(i).encode()).hexdigest()[:20]+"..." for i in range(len(logs["n"]))],
              'clasificacion':logs["Clasificacion"].to_list(),
              'bloques':logs["Bloque"].to_list()}
    return render_template("transacciones.html", data=logs_1)

@app.route('/blockchain', methods=['POST','GET'])
def blockchain():
    if request.method=='POST':
        bloque = request.form.get("block")
    logs = pd.read_csv('logs.csv', sep=";")
    logs_1 = {'n':logs["n"].to_list(),
              'id':logs["ID"].to_list(),
              'timestamp':logs["timestamp"].to_list(),
              'descripcion':logs["agent.type"].to_list(),
              'hash': [ hashlib.sha256(str(i).encode()).hexdigest()[:20]+"..." for i in range(len(logs["n"]))],
              'hash_c':  [ hashlib.sha256(str(i).encode()).hexdigest() for i in range(len(logs["n"]))],
              'clasificacion':logs["Clasificacion"].to_list(),
              'bloques':logs["Bloque"].to_list()}

    return render_template("blockchain.html", data=logs_1)

@app.route('/perfil')
def perfil():
    return render_template("perfil.html")

if __name__ == '__main__':
    app.run(debug=True)