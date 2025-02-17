from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pesquisa_visi():
    if request.method == 'POST':
        # Read Excel file
        df = pd.read_excel('visitas.xlsx')
        
        # Get search term from form
        search_term = request.form.get('search')
        
        # Filter dataframe
        result = df[df['Nome'].str.contains(search_term, case=False, na=False)]
        
        return render_template('results.html', results=result.to_dict('records'))
    
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
