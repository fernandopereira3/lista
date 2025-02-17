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
    print(f"Could not connect to MongoDB: {e}")
    # Handle the error appropriately, e.g., display an error page
    exit(1)  # Or some other error handling


@app.route('/lista', methods=['GET', 'POST'])

def normalizar_matricula(matricula):
    return re.sub(r'[\.\-]', '', matricula).strip() 

def pesquisa_visi():
    if request.method == 'POST':
        matricula_normalizada = re.compile(f".*{txt_d_pesquisa}.*", re.IGNORECASE)
        consulta_exata = {'matricula': matricula_normalizada}

        #{ "<field>": { "$regex": "pattern", "$options": "<options>" } } REGEX DO MONGODB
        
        if not resultado:
        resultado = list(sentenciados.find({'matricula': {'$regex': matricula_normalizada}}))  
        return resultado



        query = {
            'detento': {
                'matricula':"  matr,
                '$lte': data_fim
            }
        }

        try:
            resultado = list(sentenciados.find(query))

            # Convert ObjectId to string using list comprehension
            results = [{**result, '_id': str(result['_id'])} for result in results]

            return render_template('pesquisa.html', results=results) # Pass results to template

        except pymongo.errors.PyMongoError as e:
            print(f"Database error: {e}")
            return render_template('pesquisa.html', error="A database error occurred.")

    return render_template('pesquisa.html') # Render the page initially or if not a POST request


if __name__ == '__main__':
    app.run(debug=True, port=80)

