from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import joblib

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

# Load ML Model
model = joblib.load('model.pkl')


# Database Table
class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    dob = db.Column(db.String(50))

    email = db.Column(db.String(100))

    glucose = db.Column(db.Float)

    haemoglobin = db.Column(db.Float)

    cholesterol = db.Column(db.Float)

    remarks = db.Column(db.String(100))


# Home Route
@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']

        glucose = float(request.form['glucose'])
        haemoglobin = float(request.form['haemoglobin'])
        cholesterol = float(request.form['cholesterol'])

        # ML Prediction
        result = model.predict([
            [glucose, haemoglobin, cholesterol]
        ])

        prediction = result[0]

        # Save Record
        new_patient = Patient(
            name=name,
            dob=dob,
            email=email,
            glucose=glucose,
            haemoglobin=haemoglobin,
            cholesterol=cholesterol,
            remarks=prediction
        )

        db.session.add(new_patient)
        db.session.commit()

        return redirect('/')

    patients = Patient.query.all()

    return render_template(
        'index.html',
        patients=patients
    )


# Delete Route
@app.route('/delete/<int:id>')
def delete(id):

    patient = Patient.query.get(id)

    db.session.delete(patient)

    db.session.commit()

    return redirect('/')


# Update Route
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    patient = Patient.query.get(id)

    if request.method == 'POST':

        patient.name = request.form['name']
        patient.dob = request.form['dob']
        patient.email = request.form['email']

        patient.glucose = float(request.form['glucose'])
        patient.haemoglobin = float(request.form['haemoglobin'])
        patient.cholesterol = float(request.form['cholesterol'])

        # Generate New Prediction
        result = model.predict([
            [
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol
            ]
        ])

        patient.remarks = result[0]

        db.session.commit()

        return redirect('/')

    return render_template(
        'update.html',
        patient=patient
    )


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)