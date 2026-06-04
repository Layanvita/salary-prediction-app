from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(
    open("C:/Users/HP/Documents/project3/model/salary_model.pkl", "rb")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    percentage = float(
        request.form["percentage"]
    )

    prediction = model.predict(
        np.array([[percentage]])
    )

    return render_template(
        "index.html",
        prediction_text=
        f"Predicted Salary: {prediction[0]:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)