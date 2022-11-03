class Usuario:
	def __init__(self):
		self.id = 0
		self.nome = ""
		self.email = ""
		self.senha = ""
		self.cep = ""

	def __init__(self, _id, _nome, _email, _senha, _cep):
		self.id = _id
		self.nome = _nome
		self.email = _email
		self.senha = _senha
		self.cep = _cep

	def crate_sql(self):
		s = 'insert into Usuario values (%s, "%s", "%s", "%s", "%s")' % (self.id, self.nome, self.email, self.senha, self.cep)
		return s

	def descompat_sel(self, sql):
		# insert into Usuario values (1, "emanuel", "emanueljsmorae@gmail.com", "12345", "89052-000")
		s = sql.split(" ")
		return s

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
