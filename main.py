from flask import Flask, render_template, request, jsonify
from models.forms import PesquisaForm
import pandas as pd
import  os
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__, instance_relative_config=True)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/cpppac'
app.config['SECRET_KEY'] = os.urandom(32)

# Inicializa o PyMongo corretamente
mongo = PyMongo(app)
db = mongo.db  # Aqui você acessa o banco de dados diretamente


class PesquisaForm(FlaskForm):
    matricula = StringField('Matrícula')
    nome = StringField('Nome')
    pesquisar = SubmitField('PESQUISAR')

@app.route('/lista', methods=['GET', 'POST'])
def pesquisa_matricula():
    form = PesquisaForm()
    sentenciados = db.sentenciados  # Acesse a coleção do MongoDB
    resultados = []  # Inicializa uma lista vazia para os resultados

    if form.validate_on_submit():  # Se o formulário foi enviado corretamente
        matricula = form.matricula.data.strip()
        nome = form.nome.data.strip()
        query = {}

        if matricula:
            query['matricula'] = matricula
        if nome:
            query['nome'] = {"$regex": nome, "$options": "i"}  # Busca por nome ignorando maiúsculas e minúsculas

        resultados = list(sentenciados.find(query))  # Converte o cursor do MongoDB para lista

        # Convertendo ObjectId para string antes de passar para o template
        for resultado in resultados:
            resultado['_id'] = str(resultado['_id'])

    return render_template('pesquisa.html', form=form, sentenciados=resultados)



@app.route('/completa', methods=['GET'])
def completa():
    resultado = db.sentenciados.find()  # Substitua 'sentenciados' pelo nome da coleção real
    lista = list(resultado)
    return jsonify(lista)  # Retorna toda a lista em JSON


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)
