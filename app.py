from flask import Flask, request, jsonify, Response, make_response
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
    db_ocorrencias = client['ocorrencia']
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


def aceitar_host_externo(resp):
    return make_response(resp, {"Access-Control-Allow-Origin": "*"})


@app.route('/v1/ocorrencia', methods=["GET", "POST", "DELETE"])
def ocorrencias():
    if request.method == 'GET':
        return aceitar_host_externo(jsonify(code=200, data=list(db_ocorrencias)))

    elif request.method in ("PUT", "POST"):
        try:
            lat = float(request.args["lat"])
            longt = float(request.args["longt"])
            date = int(request.args["date"])
            tipo = data.Tipo(int(request.args["tipo"]))
            descricao = request.args["descricao"]
            like = int(request.args["like"])
            ocorrencia = data.Ocorrencia(
                lat, longt, date, tipo, descricao, like)
            return aceitar_host_externo(jsonify(code=200))
        except Exception as e:
            if isinstance(e, KeyError):
                return aceitar_host_externo(jsonify(code=400, error="Argumentos faltando"))
            if isinstance(e, ValueError):
                return aceitar_host_externo(jsonify(code=400, error="Argumentos inválidos"))
            return aceitar_host_externo(jsonify(code=400, error="Erro desconhecido"))

    elif request.method == 'DELETE':
        return "buraco"


@app.route('/v1/usuario', methods=["GET", "POST", "DELETE"])
def user():
    if request.method == 'GET':
        return aceitar_host_externo(jsonify(code=200, data=list(usuario)))
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
        return aceitar_host_externo(jsonify(code=200))
