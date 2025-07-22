# Heart Failure Risk Prediction

This is a Flask-based web application that predicts the risk of heart failure based on patient medical inputs. It uses a machine learning model and a scaler stored in a single `final_model.pkl` file.

---

## Features

- Web interface to enter patient medical data  
- Predicts "High Risk" or "Low Risk" of death  
- Displays real-time prediction result  
- Handles invalid input gracefully

---

## Prerequisites

- Python 3.8 or above  
- Git  
- Visual Studio Code  
- Web browser

---

## Required Python Packages

Install dependencies manually:

```bash
pip install flask numpy scikit-learn
````

Or use:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
heart-failure-prediction/
├── app.py               # Flask application
├── templates/
│   └── index.html       # Web form UI
├── final_model.pkl      # Pickled model + scaler
└── README.md            # Project documentation
```

---

## Installation & Running

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/heart-failure-prediction.git
cd heart-failure-prediction
```

### 2. (Optional) Create Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Ensure Model File Exists

Place `final_model.pkl` in the root directory.
It must contain:

```python
{'model': trained_model, 'scaler': fitted_scaler}
```

---

## Running the App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Usage

### Input Fields:

| Field                    | Example  |
| ------------------------ | -------- |
| Age                      | 65.0     |
| Anaemia                  | 0 or 1   |
| Creatinine Phosphokinase | 582      |
| Diabetes                 | 0 or 1   |
| Ejection Fraction        | 20       |
| High Blood Pressure      | 0 or 1   |
| Platelets                | 265000.0 |
| Serum Creatinine         | 1.9      |
| Serum Sodium             | 130      |
| Sex                      | 0 or 1   |
| Smoking                  | 0 or 1   |
| Follow-up Time           | 4        |

### Output:

* "High Risk of Death" or "Low Risk of Death"
* If input is invalid, a descriptive error message is displayed

---

## Troubleshooting

| Problem              | Fix                                         |
| -------------------- | ------------------------------------------- |
| Missing modules      | Run: `pip install flask numpy scikit-learn` |
| Port 5000 busy       | Change to `app.run(debug=True, port=5001)`  |
| Model crash or error | Check `final_model.pkl` is valid            |

---

## Customization Ideas

* Enhance UI using CSS or design frameworks
* Add charts or animations
* Enable export to PDF or share prediction via email

---

## Contributing

Contributions are welcome! Fork the repository, create a new branch, and submit a pull request.

---

## License

This project is licensed under the MIT License.

