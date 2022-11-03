from flask import Flask, render_template, jsonify
from entidades import *

app = Flask(__name__)

emanuel = Usuario(1, "Emanuel", "emanueljsmoraes@gmail.com", "", "89052-000")
edinho = Usuario(2, "Edson", "edtjb@gmail.com", "", "89052-000")
lista = [emanuel, edinho]

@app.route("/")
def hello():
    return render_template('hello.html', name="Emanuel")
    
@app.route("/usuario")
def usuario():
    return render_template('usuario.html', users=lista)

@app.route("/cadusuario")
def cadusuario():
    return render_template('cadusuario.html')
    
@app.route("/carrinhocompra")
def carrinhocompra():
    return "<H1>Carrinho de Compra</H1>"

@app.route("/supermecado")
def supermecado():
    return "<H1>Supermecado</H1>"

@app.route("/produto")
def produto():
    return "<H1>Produto</H1>"


app.run("localhost", 50, debug=True)