from flask import Flask, render_template

app = Flask(__name__)

# set FLASK_APP = app.py
# set FLASK_ENV=development

@app.route('/') # rota principal
def principal():
    frutas = ["TENDA", "MRV", "ECORODOVIAS", "CSN", "CURY"]    

    return render_template("index.html", frutas=frutas) # ao inves desse retorno vamos retornar uma pagina html

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")