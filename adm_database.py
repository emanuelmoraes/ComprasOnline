import sqlite3

connect = sqlite3.connect("example.db")

cursor = connect.cursor()
# criar as tabelas
cursor.execute("create table Usuario(id, nome, email, senha, cep)")
cursor.execute("create table CarrinhoCompra(id, nome, usuario_id)")
cursor.execute("create table CarrinhoUsuario(id, produto_id, user_id, carrinho_id)")
cursor.execute("create table Supermecado(id, nome, site)")
cursor.execute("create table Produto(id, nome, marca, valor, unidade, supermecado_id)")

connect.commit()