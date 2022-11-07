from app import db

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=True)
	senha = db.Column(db.String, nullable=False)
	cep = db.Column(db.String, nullable=True)

	def __repr__(self) -> str:
		return '<Name %r>' % self.name
class CarrinhoCompra(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	usuario_id = db.Column(db.Integer)

	def __repr__(self) -> str:
		return '<Name %r>' % self.name

class CarrinhoUsuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	produto_id = db.Column(db.Integer)
	usuario_id = db.Column(db.Integer)
	carrinho_id = db.Column(db.Integer)

	def __repr__(self) -> str:
		return '<Name %r>' % self.name

class Supermecado(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	site = db.Column(db.String, nullable=True)

	def __repr__(self) -> str:
		return '<Name %r>' % self.name

class Produto(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	marca = db.Column(db.String, nullable=False)
	valor = db.Column(db.String, nullable=False)
	unidade = db.Column(db.String, nullable=False)
	supermecado_id = db.Column(db.Integer)

	def __repr__(self) -> str:
		return '<Name %r>' % self.name