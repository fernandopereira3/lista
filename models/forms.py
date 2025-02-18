from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PesquisaForm(FlaskForm):
    matricula = StringField('matrícula', validators=[DataRequired()])
    nome = StringField('nome', validators=[])
    pesquisa = SubmitField('Pesquisar')