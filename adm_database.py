#!/usr/bin/python

#
# File HELP
# python adm_database.py <options>
# Option 1 = Create tables on data base
# Option 2 = Delete all tables
# Option 3 = Erase all rows from all tables
# Option 4 = Populate the data base
# Option 5 = Get data´s from data base
#
import sqlite3
import sys, getopt

connect = sqlite3.connect("example.db")

cursor = connect.cursor()

def criar_tabelas():
    cursor.execute("create table Usuario(id, nome, email, senha, cep)")
    cursor.execute("create table CarrinhoCompra(id, nome, usuario_id)")
    cursor.execute("create table CarrinhoUsuario(id, produto_id, user_id, carrinho_id)")
    cursor.execute("create table Supermecado(id, nome, site)")
    cursor.execute("create table Produto(id, nome, marca, valor, unidade, supermecado_id)")

def apagar_tabelas():
    cursor.execute("drop table Usuario")
    cursor.execute("drop table CarrinhoCompra")
    cursor.execute("drop table CarrinhoUsuario")
    cursor.execute("drop table Supermecado")
    cursor.execute("drop table Produto")

def limpar_tabelas():
    cursor.execute("delete from Usuario")
    cursor.execute("delete from CarrinhoCompra")
    cursor.execute("delete from CarrinhoUsuario")
    cursor.execute("delete from Supermecado")
    cursor.execute("delete from Produto")

def popular_tabelas():
    cursor.execute("insert into Usuario values (1, 'emanuel', 'emanueljsmoraes@gmail.com', '123456', '89052-000')")
    cursor.execute("insert into Usuario values (2, 'edson', 'etjbr@gmail.com', '123456', '89052-000')")
    cursor.execute("insert into CarrinhoCompra values (1, 'primeiro', 1)")
    cursor.execute("insert into CarrinhoCompra values (2, 'semana', 1)")
    cursor.execute("insert into CarrinhoCompra values (3, 'mensal', 2)")
    cursor.execute("insert into CarrinhoCompra values (4, 'churrasco', 2)")
    #cursor.execute("insert into CarrinhoUsuario values ()")
    cursor.execute("insert into Supermecado values (1, 'Villareal', 'villareal.com.br')")
    cursor.execute("insert into Supermecado values (2, 'Carrefour', 'carrefour.com.br')")
    cursor.execute("insert into Produto values (1, 'leite', 'parmalat', '10,00', 'caixa', 1)")
    cursor.execute("insert into Produto values (2, 'pão', 'carrefour', '1,00', 'un', 1)")
    cursor.execute("insert into Produto values (3, 'café', 'união', '5,50', 'pacote', 1)")
    cursor.execute("insert into Produto values (4, 'torrada', 'blabla', '6,50', 'pacote', 1)")
    cursor.execute("insert into Produto values (5, 'leite', 'parmalat', '12,00', 'caixa', 2)")
    cursor.execute("insert into Produto values (6, 'pão', 'carrefour', '2,00', 'un', 2)")
    cursor.execute("insert into Produto values (7, 'café', 'união', '4,50', 'pacote', 2)")
    cursor.execute("insert into Produto values (8, 'torrada', 'blabla', '3,50', 'pacote', 2)")

def pega_usuario_tabela(id):
    s = "select * from Usuario where id = %s" % id
    cursor.execute(s)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


def main(argv):
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))

    if (str(sys.argv[1]) == "1"):
        criar_tabelas()
    if (str(sys.argv[1]) == "2"):
        apagar_tabelas()
    if (str(sys.argv[1]) == "3"):
        limpar_tabelas()
    if (str(sys.argv[1]) == "4"):
        popular_tabelas()
    if (str(sys.argv[1]) == "5"):
        pega_usuario_tabela("1")
    
    connect.commit()

if __name__ == "__main__":
   main(sys.argv[1:])