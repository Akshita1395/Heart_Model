from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('final_model.pkl', 'rb') as f:
    package = pickle.load(f)

model = package['model']
scaler = package['scaler']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['age']),
            int(request.form['anaemia']),
            int(request.form['creatinine_phosphokinase']),
            int(request.form['diabetes']),
            int(request.form['ejection_fraction']),
            int(request.form['high_blood_pressure']),
            float(request.form['platelets']),
            float(request.form['serum_creatinine']),
            int(request.form['serum_sodium']),
            int(request.form['sex']),
            int(request.form['smoking']),
            int(request.form['time'])
        ]

        input_data = scaler.transform([features])
        prediction = model.predict(input_data)[0]

        result = "High Risk of Death " if prediction == 1 else "Low Risk of Death "

        return render_template('index.html', prediction_text=f"Prediction: {result}")

    except Exception:
        return render_template('index.html', prediction_text=" Invalid input. Please check all fields.")

if __name__ == '__main__':
    app.run(debug=True)
