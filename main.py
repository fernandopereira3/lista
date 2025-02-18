from flask import Flask, render_template, request, jsonify
import pandas as pd
import pymongo
import re
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/cpppac'

# Initialize MongoDB client outside the request context
try:
    client = pymongo.MongoClient(app.config['MONGO_URI'])
    db = client["cpppac"]
    collection = db["sentenciados"]
except pymongo.errors.ConnectionFailure as e:
    print(f"Nao foi possivel conectar ao banco: {e}")
    exit(1)


@app.route('/lista', methods=['GET', 'POST'])

#def normalizar_matricula():
#    matricula = request.form.get('pesquisa_preso')
#    debug = app.logger.info(matricula)
#    return debug


def pesquisa_matricula():
  return render_template('pesquisa.html')  # Render the page initially or if not a POST request


if __name__ == '__main__':
    app.run(debug=True, port=80)
