from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PatientData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(5))
    story = db.Column(db.String(2000))
    complaint = db.Column(db.String(300))
    symptoms = db.Column(db.String(200))
    duration = db.Column(db.String(200))
    severity = db.Column(db.String(200))
    asymptom = db.Column(db.String(200))
    afactors = db.Column(db.String(300))
    rfactors = db.Column(db.String(300))


@app.route("/")
@app.route("/home")		
def home():
    return render_template('home.html', active='home')


@app.route("/evaluate")		
def evaluate():
    return render_template('evaluate.html', title='Evaluation', active='evaluate')


@app.route("/report")		
def report():
    return render_template('report.html', title='Report', active='report')

@app.route("/database")		
def database():
    Patientlist = PatientData.query.all()
    return render_template('database.html', title='Database', active='database',Patientlist=Patientlist)

@app.route("/statistics")			
def statistics():
    return render_template('statistics.html', title='Statistics', active='statistics')


@app.route("/howitworks")	
def howitworks():
    return render_template('howitworks.html', title='How it works', active='howitworks')


@app.route("/credits")		
def credits():
    return render_template('creditspage.html', title='Credits', active='credits')

@app.route("/add", methods=["POST"])
def add():
    story = request.form.get("story")
    gender  = request.form.get("gender")
    name  = request.form.get("fullname")
    new_data = PatientData(story=story, name=name, gender=gender)
    db.session.add(new_data)
    db.session.commit()
    return redirect(url_for("database"))

@app.route("/nlp", methods=["POST"])
def nlp():
    return redirect(url_for("reports"))
    story = request.form.get("story")
    gender  = request.form.get("gender")
    name  = request.form.get("fullname")
    # need to integrate InstaMD function from classification.ipynb here
    # This route is called from "evaluate.html" and renders "report.html" with results

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)		
