from flask import Flask, render_template, request
import pickle
import mysql.connector

app = Flask(__name__)

# ==========================
# Load Trained Model
# ==========================
model = pickle.load(open("model.pkl", "rb"))

# ==========================
# MySQL Connection
# ==========================
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="student",   # Change if your MySQL password is different
        database="heartdb"
    )

    cursor = db.cursor()
    print("Database Connected Successfully")

except Exception as e:
    print("Database Connection Error:", e)

# ==========================
# Home Page
# ==========================
@app.route('/')
def home():
    return render_template('index.html')


# ==========================
# Prediction Route
# ==========================
@app.route('/predict', methods=['POST'])
def predict():

    try:

        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])

        # Create input list
        data = [[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]]

        # Predict
        prediction = model.predict(data)[0]

        print("Prediction =", prediction)

        # IMPORTANT:
        # For your dataset:
        # 0 = Heart Disease
        # 1 = No Heart Disease

        if prediction == 0:
            status = "High Risk"
            result = "Heart Disease Detected"
        else:
            status = "Low Risk"
            result = "No Heart Disease"

        # ==========================
        # Save to Database
        # ==========================

        sql = """
        INSERT INTO predictions
        (
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal,
            result
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s
        )
        """

        values = (
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal,
            result
        )

        cursor.execute(sql, values)
        db.commit()

        return render_template(
            'result.html',
            prediction=result,
            status=status
        )

    except Exception as e:
        return f"Error: {str(e)}"


# ==========================
# Run Flask App
# ==========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)