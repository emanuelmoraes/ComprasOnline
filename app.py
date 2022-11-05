from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
db.init_app(app)

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=True)
	senha = db.Column(db.String, nullable=False)
	cep = db.Column(db.String, nullable=True)

	def __repr__(self) -> str:
		return '<Name %r>' % self.name

@app.route("/")
def hello():
    return render_template('hello.html', name="Emanuel")
    
@app.route("/usuario")
def usuario():
    lista = Usuario.query.order_by('id')
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