from flask import Flask, request
from cloudant.client import Cloudant
from os import environ
from sys import exit
import data


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


@app.route('/v1/buraco_rua', methods=["GET", "PUT", "DELETE"])
def buraco():
    if request.method == 'GET':
        return "test"
    elif request.method in ("PUT", "POST"):
        return "test"
    elif request.method == 'DELETE':
        pass


@app.route('/v1/buraco_rua/deletar')
def deletar_buraco():
    stub = data.Ocorrencia(112.21321, 213.2313, 32131231,
                           data.Tipo.BURACO.value)
    print(stub.__dict__)
    docs = ocorrencia.create_document(
        {"lat": 2131.2311, "long": 2313.2222, "date": 321321321321, "tipo": 1})
    print("LOL")
    print(docs.exists())
    return "Buraco criado"


@app.route('/v1/calcada_quebrada/criar')
def criar_calcada():
    return "Calcada quebrada adicionada"


@app.route('/v1/calcada_quebrada/deletar')
def deletar_calcada():
    return "Calcada quebrada removida"
