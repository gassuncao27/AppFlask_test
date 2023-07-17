from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True
# app.run()

# set FLASK_APP = app.py
# set FLASK_ENV=development

frutas =[]

@app.route('/', methods=["GET", "POST"]) # rota principal
def principal():
    # frutas = ["Tenda", "Mrv", "Ecorodovias", "Csn", "Cury"]    
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas) # ao inves desse retorno vamos retornar uma pagina html

@app.route('/sobre')
def sobre():
    notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno":7.0, "Sicrano":8.5, "Rodrigo":9.5}
    return render_template("sobre.html", notas=notas)