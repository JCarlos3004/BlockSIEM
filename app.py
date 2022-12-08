from flask import Flask,render_template, request


app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/layout')
def layout():
    return render_template("layout.html")

@app.route('/tables.html')
def tables():
    return render_template("tables.html")

@app.route('/transacciones.html')
def transacciones():
    return render_template("transacciones.html")

if __name__ == '__main__':
    app.run(debug=True)