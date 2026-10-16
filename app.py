from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/om')
def prosjekter():
    return render_template("om.html")
   

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

@app.route("/spill")
def fag():
    spillliste = ["Noita", "STS2", "Pokérouge", "Hades", "Dead Cells"]
    return render_template("spill.html", spill=spillliste)

@app.route('/registrering', methods=["GET", "POST"])
def registrering():
    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        alder = request.form["alder"]
        kommentar = request.form["kommentar"]
        return render_template(
            "resultat.html",
            navn=navn,
            epost=epost,
            alder=alder,
            kommentar=kommentar
            
        )
    
    return render_template("registrering.html")


@app.route('/velgSpill', methods=["GET", "POST"])
def velgSpill():
    spillvalg = ["Terraria", "Hollow Knight: Silksong", "Deltarune", "Noita", "Slay THhe Spire 2"]
    return render_template("velgSpill.html", spillvalg=spillvalg)

if __name__ == '__main__':
    app.run(debug=True)