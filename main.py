from flask import Flask, render_template, request
import pandas as pd
import pymongo

app = Flask(__name__)

@app.route('/lista', methods=['GET', 'POST'])
def pesquisa_visi():
    if request.method == 'POST':
       pass

if __name__ == '__main__':
    app.run(debug=True)
