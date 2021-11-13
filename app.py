from flask import Flask, url_for, request, jsonify
import joblib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.json:
        req = request.get_json()
        if 'input' in req.keys():
            classifier = joblib.load("/Users/reffet/Desktop/Deployment_Project/data/model.joblib")
            prediction = classifier.predict(req["input"])
            prediction = str(prediction[0])
            return jsonify({"predict": prediction}), 200
    return jsonify({"msg": "This isn't the right data input format, please verify your input"}), 200
    
if __name__ == "__main__":
    app.run(debug=True)
