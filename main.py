import json
from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)


def Open(x):
    with open(x, 'r') as reader:
        doc = json.loads(reader.read())
    reader.close()
    return doc


def jsmake():
    response = jsonify({"response": "a á, e é" })
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


@app.route('/')
def launch():
    return redirect('/Alearys')


@app.route('/Alearys')
def front():
    links = Open("fiche.json")
    return render_template('frontPage.html', links=links)


@app.route('/Alearys/fiche', methods=['POST'])
def fichefront():
    idFiche = int(request.form["ficheId"])
    fiche = Open("fiche.json")
    return render_template("show.html", fiche=fiche, id=idFiche)

@app.route('/Alearys/fiche/add')
def ficheAdd():
    return render_template("add.html")


@app.route("/Alearys/fiche/add/link", methods=['GET'])
def gotocreate():
    return redirect('/Alearys/fiche/add')


@app.route("/Alearys/fiche/add/new", methods=['POST'])
def newfiche():
    newFiche = {
        "id": 0,
        "ficheName": request.form['nom'],
        "ficheHead": [request.form['nom'], request.form['race'], request.form['taille'], request.form['poid'], request.form['age']],
        "ficheBody": format(request.form['texter'])
    }
    fiche = Open("fiche.json")
    newFiche['id'] = len(fiche)
    fiche.append(newFiche)
    fiche = json.dumps(fiche, indent=2)
    with open("fiche.json", 'w') as writer:
        writer.write(fiche)
    writer.close()
    return redirect("/Alearys")