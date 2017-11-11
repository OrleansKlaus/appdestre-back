from flask import Flask, request
app = Flask(__name__)

'''
@app.route('/<nome>/<float:idade>')
def hello(nome, idade):
    return f"Ta achando que eu sou besta?? {nome} {idade}"

@app.route('/<nome>/<int:idade>', methods= ["GET", "PUT", "DELETE"])
def outro(nome, idade):
    if request.method == 'GET':
        pass
    elif request.method in ("PUT", "POST"):
        pass
    elif request.method == 'DELETE':
        pass
    return f"seja bem vindo {nome} {idade} {request.method}"
'''
@app.route('/v1/buraco_rua', methods= ["GET", "PUT", "DELETE"])
def buraco():
    if request.method == 'GET':
        pass
    elif request.method in ("PUT", "POST"):
        pass
    elif request.method == 'DELETE':
        pass
    

@app.route('/v1/buraco_rua/deletar')
def deletar_buraco():
    return "Buraco criado"

@app.route('/v1/calcada_quebrada/criar')
def criar_calcada():
    return "Calcada quebrada adicionada"

@app.route('/v1/calcada_quebrada/deletar')
def deletar_calcada():
    return "Calcada quebrada removida"