##  Heart Failure Risk Prediction

This is a Flask-based web application that predicts the **risk of heart failure** based on medical inputs. It uses a machine learning model and a scaler, both loaded from a single `final_model.pkl` file.

---

###  Features

* Web-based form to input patient data
* Predicts **High Risk** or **Low Risk** of heart failure
* Displays results on-screen instantly
* Handles invalid input gracefully

---

###  Prerequisites

* Python 3.8+
* Visual Studio Code
* Git
* Web browser

---

###  Required Python Packages

Install dependencies:

```bash
pip install flask numpy scikit-learn
```

Or use a `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

###  Project Structure

```
heart-failure-prediction/
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend form
├── final_model.pkl      # Trained model + scaler
└── README.md            # Project guide
```

---

###  Installation & Running (VS Code)

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/heart-failure-prediction.git
cd heart-failure-prediction
```

#### 2. (Optional) Create Virtual Environment

```bash
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If no `requirements.txt`:

```bash
pip install flask numpy scikit-learn
```

#### 4. Ensure Model Exists

Make sure `final_model.pkl` is in the root directory. It should contain:

```python
{'model': your_trained_model, 'scaler': your_fitted_scaler}
```

---

### ▶ Running the App

#### From VS Code:

1. Open folder in VS Code
2. Select Python interpreter (use the virtual environment if created)
3. Open `app.py` and hit `Run` (or press `F5`)

#### Or via terminal:

```bash
python app.py
```

App will run on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

###  Usage

#### Input Fields:

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
| Follow-up Time (days)    | 4        |

#### Output:

* **Prediction:** “High Risk of Death ” or “Low Risk of Death ”
* **Error handling:** If invalid input, user-friendly error is shown

---

###  Troubleshooting

| Issue                 | Fix                                                 |
| --------------------- | --------------------------------------------------- |
| `ModuleNotFoundError` | Run: `pip install flask numpy scikit-learn`         |
| Port already in use   | Use another: `app.run(debug=True, port=5001)`       |
| Model error / crash   | Make sure `final_model.pkl` is valid and compatible |

---

###  Customization

* Improve UI with custom CSS or Tailwind
* Add charts or animations (Chart.js / D3.js)
* Export predictions as PDF or email summary

---

###  Contributing

Pull requests are welcome. Fork the repo, make changes on a new branch, and submit a PR.

---

###  License

This project is licensed under the [MIT License](LICENSE).

