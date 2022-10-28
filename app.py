from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html', name="Emanuel")
    
@app.route("/edson")
def exemplo():
    return "Bem vindo edson"
    
@app.route("/retorno", methods=['GET'])
def retorno():
    return jsonify({
        "name": "emanuel",
        "descricao": "teste",
        "idade": 10})
    
app.run("localhost", 50)