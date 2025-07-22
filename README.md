Heart Failure Risk Prediction
This project is a Flask-based web application that predicts the risk of heart failure based on user-provided medical data. The application uses a pre-trained machine learning model and a scaler, both loaded from a pickled file (final_model.pkl), to make predictions.
Features

Input patient data through a web form.
Predicts heart failure risk (High Risk or Low Risk) using a machine learning model.
Displays prediction results on the web interface.
Handles invalid inputs gracefully with error messages.

Prerequisites
Before running the application, ensure you have the following installed:

Python 3.8 or higher
Visual Studio Code (VS Code)
Git
A web browser

Required Python Packages
Install the required Python packages using pip:
pip install flask numpy scikit-learn

Project Structure
heart-failure-prediction/
│
├── app.py               # Flask application script
├── index.html           # HTML template for the web interface
├── final_model.pkl      # Pickled file containing the trained model and scaler
└── README.md            # This file

Installation

Clone the Repository:
git clone https://github.com/your-username/heart-failure-prediction.git
cd heart-failure-prediction


Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

If you don't have a requirements.txt, install the required packages directly:
pip install flask numpy scikit-learn


Ensure final_model.pkl is Available:

The application requires a final_model.pkl file containing the trained model and scaler. Ensure this file is present in the project root directory.
If you need to generate this file, train a machine learning model (e.g., using scikit-learn) and save it with the structure {'model': your_model, 'scaler': your_scaler} using pickle.



Running the Application in Visual Studio Code

Open the Project in VS Code:

Launch VS Code.
Select File > Open Folder and choose the heart-failure-prediction directory.


Set Up the Python Interpreter:

Ensure the correct Python interpreter is selected (the one with Flask installed).
Press Ctrl+Shift+P (or Cmd+Shift+P on Mac) to open the Command Palette.
Type Python: Select Interpreter and choose the Python version from your virtual environment or global installation.


Run the Application:

Open the app.py file in VS Code.
Click the Run button (or press F5) to start the Flask development server. Alternatively, open the terminal in VS Code (Terminal > New Terminal) and run:python app.py


The application will start, and you should see output indicating the server is running (e.g., Running on http://127.0.0.1:5000).


Access the Application:

Open a web browser and navigate to http://127.0.0.1:5000.
Fill out the form with the required medical data and click "Predict Risk" to see the prediction.



Usage

Input Fields:

Age: Patient's age (e.g., 65.0).
Anaemia: 0 (No) or 1 (Yes).
Creatinine Phosphokinase: Integer value (e.g., 582).
Diabetes: 0 (No) or 1 (Yes).
Ejection Fraction: Integer value (e.g., 20).
High Blood Pressure: 0 (No) or 1 (Yes).
Platelets: Float value (e.g., 265000.0).
Serum Creatinine: Float value (e.g., 1.9).
Serum Sodium: Integer value (e.g., 130).
Sex: 0 (Female) or 1 (Male).
Smoking: 0 (No) or 1 (Yes).
Follow-up Time: Integer value representing days (e.g., 4).


Prediction:

After submitting the form, the application will display either "High Risk of Death" or "Low Risk of Death" based on the model's prediction.
If invalid inputs are provided, an error message will appear.



Notes

The application runs in debug mode (debug=True) for development purposes. Disable this in production for security.
Ensure the final_model.pkl file is compatible with the Python and scikit-learn versions used.
The web interface is minimal and can be enhanced with CSS for better styling.

Troubleshooting

Module Not Found Error: Ensure all required packages are installed in the active Python environment.
Port Conflict: If port 5000 is in use, specify a different port in app.py (e.g., app.run(debug=True, port=5001)).
Invalid Input Error: Verify that all form inputs are numeric and within valid ranges.

Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.
License
This project is licensed under the MIT License.
