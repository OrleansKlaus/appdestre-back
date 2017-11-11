from flask import Flask, request, jsonify, Response
from cloudant.client import Cloudant
from os import environ
from sys import exit
import data
import bcrypt as bc


app = Flask(__name__)

try:
    usuario = environ.get("CLOUDANT_USERNAME")
    passwd = environ.get("CLOUDANT_PASSWORD")
    url = environ.get("CLOUDANT_URL")
    client = Cloudant(usuario, passwd, url=url, connect=True)
    ocorrencia = client['ocorrencia']
    usuario = client['usuario']
except Exception as e:
    if isinstance(e, KeyError):
        ocorrencia = client.create_database('ocorrencia')
        usuario = client.create_database('usuarios')
    else:
        print("Não foi possivel conectar a database")
        print(e)
        exit(1)


'''
desnivel - falta de acessibilidade
mato na calçada
poste na calçada
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


@app.route('/v1/buraco', methods=["GET", "POST", "DELETE"])
def buraco():
    if request.method == 'GET':
        return "test"

    elif request.method in ("PUT", "POST"):
        try:
            lat = float(request.args["lat"])
            longt = float(request.args["longt"])
            date = int(request.args["date"])
            tipo = data.Tipo(int(request.args["tipo"]))
            ocorrencia = data.Ocorrencia(lat, longt, date, tipo)
            return jsonify(banana=lat)
        except Exception as e:
            if isinstance(e, KeyError):
                return jsonify(code=400, error="Argumentos faltando")
            if isinstance(e, ValueError):
                return jsonify(code=400, error="Argumentos inválidos")
            return jsonify(code=400, error="Erro desconhecido")

    elif request.method == 'DELETE':
        return "buraco"


@app.route('/v1/usuario', methods=["GET", "POST", "DELETE"])
def user():
    if request.method == 'GET':
        return "test"
    elif request.method == 'POST':
        nome_usuario = request.args["nome_usuario"]
        nome = request.args["nome"]
        senha = request.args["senha"]
        salt = bc.gensalt()

        user = data.Usuario(
            nome_usuario, nome, bc.hashpw(senha.encode(), salt).decode(),
            salt.decode())
        print(user.__dict__)
        usuario.create_document(
            user.__dict__
        )
        return jsonify(code=200)
