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
    cursor.execute("CREATE TABLE `usuario` (\
	`id` INTEGER PRIMARY KEY AUTOINCREMENT,\
	`nome` VARCHAR(50) NOT NULL,\
	`email` VARCHAR(30) NOT NULL,\
	`senha` VARCHAR(20) NOT NULL,\
	`cep` VARCHAR(10))")
    cursor.execute("CREATE TABLE `carrinho_compra` (\
	`id` INTEGER PRIMARY KEY AUTOINCREMENT,\
	`nome` VARCHAR(50),\
	`usuario_id` INT(20))")
    cursor.execute("CREATE TABLE `carrinho_usuario` (\
	`id` INTEGER PRIMARY KEY AUTOINCREMENT,\
	`produto_id` INT(20) NOT NULL,\
	`usuario_id` INT(20) NOT NULL,\
	`carrinho_id` INT(20) NOT NULL)")
    cursor.execute("CREATE TABLE `supermecado` (\
	`id` INTEGER PRIMARY KEY AUTOINCREMENT,\
	`nome` VARCHAR(50) NOT NULL,\
	`site` VARCHAR(50))")
    cursor.execute("CREATE TABLE `produto` (\
	`id` INTEGER PRIMARY KEY AUTOINCREMENT,\
	`nome` VARCHAR(50) NOT NULL,\
	`marca` VARCHAR(50),\
    'valor' VARCHAR(10),\
    'unidade' VARCHAR(10),\
    'supermecado_id' INTEGER\
    )")

def apagar_tabelas():
    cursor.execute("drop table usuario")
    cursor.execute("drop table carrinho_compra")
    cursor.execute("drop table carrinho_usuario")
    cursor.execute("drop table supermecado")
    cursor.execute("drop table produto")

def limpar_tabelas():
    cursor.execute("delete from usuario")
    cursor.execute("delete from carrinho_compra")
    cursor.execute("delete from carrinho_usuario")
    cursor.execute("delete from supermecado")
    cursor.execute("delete from produto")

def popular_tabelas():
    cursor.execute("insert into usuario values (1, 'emanuel', 'emanueljsmoraes@gmail.com', '123456', '89052-000')")
    cursor.execute("insert into usuario values (2, 'edson', 'etjbr@gmail.com', '123456', '89052-000')")
    cursor.execute("insert into carrinho_compra values (1, 'primeiro', 1)")
    cursor.execute("insert into carrinho_compra values (2, 'semana', 1)")
    cursor.execute("insert into carrinho_compra values (3, 'mensal', 2)")
    cursor.execute("insert into carrinho_compra values (4, 'churrasco', 2)")
    #cursor.execute("insert into CarrinhoUsuario values ()")
    cursor.execute("insert into supermecado values (1, 'Villareal', 'villareal.com.br')")
    cursor.execute("insert into supermecado values (2, 'Carrefour', 'carrefour.com.br')")
    cursor.execute("insert into produto values (1, 'leite', 'parmalat', '10,00', 'caixa', 1)")
    cursor.execute("insert into produto values (2, 'pão', 'carrefour', '1,00', 'un', 1)")
    cursor.execute("insert into produto values (3, 'café', 'união', '5,50', 'pacote', 1)")
    cursor.execute("insert into produto values (4, 'torrada', 'blabla', '6,50', 'pacote', 1)")
    cursor.execute("insert into produto values (5, 'leite', 'parmalat', '12,00', 'caixa', 2)")
    cursor.execute("insert into produto values (6, 'pão', 'carrefour', '2,00', 'un', 2)")
    cursor.execute("insert into produto values (7, 'café', 'união', '4,50', 'pacote', 2)")
    cursor.execute("insert into produto values (8, 'torrada', 'blabla', '3,50', 'pacote', 2)")

def pega_usuario_tabela(id):
    s = "select * from Usuario where id = %s" % id
    cursor.execute(s)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


def main(argv):
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))

    for item in sys.argv:
        if (str(item) == "1"):
            criar_tabelas()
        if (str(item) == "2"):
            apagar_tabelas()
        if (str(item) == "3"):
            limpar_tabelas()
        if (str(item) == "4"):
            popular_tabelas()
        if (str(item) == "5"):
            pega_usuario_tabela("1")
    
    connect.commit()

if __name__ == "__main__":
   main(sys.argv[1:])