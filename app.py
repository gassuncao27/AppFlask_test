from flask import Flask, render_template, request

app = Flask(__name__)
# set FLASK_APP = app.py
# set FLASK_ENV=development

frutas =[]
registros = []

@app.route('/', methods=["GET", "POST"]) # rota principal
def principal():
    # frutas = ["Tenda", "Mrv", "Ecorodovias", "Csn", "Cury"]    
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas) # ao inves desse retorno vamos retornar uma pagina html

@app.route('/sobre', methods=['GET', 'POST'])
def sobre():
    # notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno":7.0, "Sicrano":8.5, "Rodrigo":9.5}
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            registros.append({"aluno": request.form.get("aluno"), 'nota': request.form.get("nota")})
    
    return render_template("sobre.html", registros=registros)


if __name__ == "__main__":
    app.run(debug=True)
