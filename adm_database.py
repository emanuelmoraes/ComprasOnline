#!/usr/bin/python

#
# File HELP
# python adm_database.py <options>
# Option 1 = Create tables on data base
# Option 2 = Delete all tables
# Option 3 = Erase all rows from all tables
# Option 4 = Populate the data base
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
    cursor.execute("insert into Usuario values ()")
    cursor.execute("insert into CarrinhoCompra values ()")
    cursor.execute("insert into CarrinhoUsuario values ()")
    cursor.execute("insert into Supermecado values ()")
    cursor.execute("insert into Produto values ()")

connect.commit()

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

if __name__ == "__main__":
   main(sys.argv[1:])