from flask import Flask, url_for, request, jsonify, render_template
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        req = request.get_json()
        # Check mandatory keys
        if 'input' in req.keys():
            # load model
            classifier = joblib.load("models/model.joblib")
            prediction = classifier.predict(req["input"])
            #prediction = str(prediction[0])
            return jsonify([str(pred) for pred in prediction]), 200
    return jsonify({"msg": "This isn't the right data input format, please verify your input"})
    
if __name__ == "__main__":
    app.run(debug=True)
