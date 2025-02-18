from flask import Flask, render_template, request, jsonify
from models.forms import PesquisaForm
import pandas as pd
import pymongo
import os
import re
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__, instance_relative_config=True)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/cpppac'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize MongoDB client outside the request context
try:
    client = pymongo.MongoClient(app.config['MONGO_URI'])
    db = client["cpppac"]
    collection = db["sentenciados"]
except pymongo.errors.ConnectionFailure as e:
    print(f"Nao foi possivel conectar ao banco:  {e}")
    exit(1)

class PesquisaForm(FlaskForm):
    matricula = StringField('matrícula', validators=[DataRequired(message='Campo obrigatório')])
    nome = StringField('nome')
    pesquisar = SubmitField('pesquisar')

@app.route('/lista', methods=['GET', 'POST'])
def pesquisa_matricula():
  form = PesquisaForm()
  return render_template('pesquisa2.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=80)
