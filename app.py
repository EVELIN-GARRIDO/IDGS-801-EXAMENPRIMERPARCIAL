from flask import Flask, request, render_template

from TuclaseExamen import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def cargarPagina():
    return render_template("formulario.html")

@app.route('/arreglista-aritmetico', methods=["POST"])
def arithmetic():
    problemas = request.form.get("txtProblemas")
    
    if ('"' in problemas):
        problemas = problemas.replace('"', '')

        if ('[' in problemas or ']' in problemas):
            problemas = problemas.replace('[', '')
            problemas = problemas.replace(']', '')

    lista = problemas.split(',')
    respuestaResolver = request.form.get("rbtRespuesta")
    
    if (respuestaResolver == 'True'):
        respuestaResolver == True
        resp = '\n' + TuclaseExamen.arithmetic_arranger(lista, respuestaResolver)

    if (respuestaResolver == 'False'):
        resp = '\n' + TuclaseExamen.arithmetic_arranger(lista)

    return render_template('resultado.html', resp=resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)