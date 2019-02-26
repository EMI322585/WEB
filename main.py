from flask import Flask, render_template
app = Flask(__name__) #objekts Flask


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():

    return '<h1>About page</h><a href="/">Go back to main page</a>'# ārpusē lielās pēdiņas un iekšā mazās. Nedrīkst jaukt!


if __name__ == '__main__': #pārbauda vai fails tiek izpildīts pa tiešo vai cita faila apakšdaļa
    app.run() #palaiž objektu