# Health Prediction Application

## Overview

This is a Flask-based Health Prediction Application developed using Python, SQLite, Bootstrap, and Machine Learning.

The application allows users to:

* Add patient records
* View patient records
* Update patient details
* Delete patient records
* Predict health risk based on blood test values

The project combines CRUD operations with Machine Learning prediction in a simple healthcare application.

---

## Technologies Used

* Python
* Flask
* SQLite
* SQLAlchemy
* HTML
* Bootstrap
* Scikit-learn
* Pandas
* Joblib

---

## Features

* Add new patient records
* View all patient records
* Update patient information
* Delete patient records
* Health risk prediction using Machine Learning
* Responsive user interface
* Form validation
* SQLite database integration

---

## Machine Learning Model

The application uses a RandomForestClassifier model trained on sample healthcare data.

Input values:

* Glucose
* Haemoglobin
* Cholesterol

Prediction output:

* Low Risk
* Moderate Risk
* High Risk

The trained model is saved as:

```plaintext id="m1"
model.pkl
```

---

## Project Structure

```plaintext id="m2"
Health_Prediction_App/
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── update.html
│
└── instance/
```

---

## How To Run The Project

### Step 1: Clone Repository

```bash id="m3"
git clone https://github.com/HarshaGotmare/Health-Prediction-App.git
```

### Step 2: Open Project Folder

```bash id="m4"
cd Health-Prediction-App
```

### Step 3: Install Required Libraries

```bash id="m5"
pip install -r requirements.txt
```

### Step 4: Run Application

```bash id="m6"
python app.py
```

### Step 5: Open Browser

```plaintext id="m7"
http://127.0.0.1:5000
```

---

## CRUD Operations

### Create

Users can add new patient records.

### Read

All patient records are displayed in the table.

### Update

Existing patient details can be modified.

### Delete

Patient records can be removed from the database.

---

## Validation Implemented

* Required fields validation
* Valid email format
* Numeric value validation
* Prevention of negative values

---

## Challenges Faced

* Integrating Machine Learning prediction with CRUD operations
* Managing data flow between frontend, backend, and database
* Improving frontend responsiveness

---

## Learning Outcomes

This project helped me improve my understanding of:

* Flask backend development
* CRUD operations
* SQLite database integration
* Frontend development using Bootstrap
* Machine Learning model integration

---

## Author

Harsha Gotmare
