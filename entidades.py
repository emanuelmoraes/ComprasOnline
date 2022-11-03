class Usuario:
	def __init__(self, _id, _nome, _email, _senha, _cep):
		self.id = _id
		self.nome = _nome
		self.email = _email
		self.senha = _senha
		self.cep = _cep

	def crate_sql(self):
		s = 'insert into Usuario values (%s, "%s", "%s", "%s", "%s")' % (self.id, self.nome, self.email, self.senha, self.cep)
		return s

	def insert_data_from_lista(self, lista):
		self.id = lista[0]
		self.nome = lista[1]
		self.email = lista[2]
		self.senha = lista[3]
		self.cep = lista[4]

class CarrinhoCompra:
	def __init__(self):
		self.id = 0
		self.nome = ""
		self.usuario_id = 0

class CarrinhoUsuario:
	def __init__(self):
		self.id = 0
		self.produto_id = 0
		self.user_id = 0
		self.carrinho_id = 0

class Supermecado:
	def __init__(self):
		self.id = 0
		self.nome = ""
		self.site = ""

class Produto:
	def __init__(self):
		self.id = 0
		self.nome = ""
		self.marca = ""
		self.valor = 0.0
		self.unidade = 0
		self.supermecado_id = 0
