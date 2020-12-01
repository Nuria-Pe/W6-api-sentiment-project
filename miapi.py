from flask import Flask, request
import markdown.extensions.fenced_code
import random
import tools.getdata as get
import json
import tools.postdata as post


app = Flask (__name__)


@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string
    


@app.route("/frases/<personaje>")
def frasepersonaje(personaje):
    frases = get.mensajepersonaje(personaje)
    return json.dumps(frases)


@app.route("/nuevafrase", methods=["POST"])
def insertmensaje():
    tiempo = request.form.get("date")
    personaje = request.form.get("speaker")
    frase = request.form.get("speech")
    post.insertmensaje(tiempo, personaje, frase)
    return "Mensaje introducido correctamente en la base de datos"

"""
Almaceno y llamo a la función post insertamensaje
"""











































app.run(debug=True)