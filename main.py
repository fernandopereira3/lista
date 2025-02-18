from flask import Flask, render_template, request, jsonify
from models.forms import PesquisaForm
import pandas as pd
import  os
from pymongo import MongoClient
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__, instance_relative_config=True)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/cpppac'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize MongoDB client outside the request context
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["cpppac"]
    collection = db["sentenciados"]
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")

class PesquisaForm(FlaskForm):
    matricula = StringField('Matrícula')
    nome = StringField('Nome')
    pesquisar = SubmitField('PESQUISAR')

@app.route('/lista', methods=['GET', 'POST'])
def pesquisa_matricula():
  form = PesquisaForm()
  return render_template('pesquisa.html', form=form)
  #if request.method == 'POST':
  #  matricula = request.form['matricula']
  #  nome = request.form['nome']
  #  if matricula:
  #    cursor = list(collection.find({'matricula': matricula}))
  #  elif nome:
  #    cursor = list(collection.find({'nome': nome}))
  #  else:
  #    cursor = collection.find()
  #  for sentenciado in cursor:
  #    return sentenciado, 400
     #return render_template('pesquisa.html', form=form, sentenciados=sentenciado)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)
