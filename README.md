# Heart Disease Prediction Project

A machine learning web application that predicts the likelihood of heart disease based on patient health metrics.

## Features

- Predict heart disease using a trained ML model
- Web interface built with Flask
- MySQL database integration
- Jenkins CI/CD pipeline
- RESTful API endpoints

## Project Structure

```
HeartDiseaseProject/
├── app.py                 # Flask application
├── train_model.py         # Model training script
├── model.pkl              # Trained ML model
├── heart.csv              # Dataset
├── requirements.txt       # Python dependencies
├── Jenkinsfile            # CI/CD pipeline configuration
├── database/
│   └── heartdb.sql        # Database schema
├── templates/
│   ├── index.html         # Home page
│   └── result.html        # Prediction result page
├── static/
│   ├── css/
│   │   └── style.css      # Styling
│   └── images/
│       └── heart.png      # Heart logo
└── screenshots/           # Project screenshots
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   ```bash
   python train_model.py
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the web interface at `http://localhost:5000`

## Database Setup

Import the database schema:
```bash
mysql -u root -p < database/heartdb.sql
```

## Usage

1. Navigate to the home page
2. Enter patient health metrics
3. Submit the form to get a prediction
4. View the result

## Technologies Used

- **Backend**: Flask, Python
- **ML**: scikit-learn
- **Database**: MySQL
- **CI/CD**: Jenkins
