from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "SMS Spam Classification Service is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "").lower()

    spam_words = ["free", "win", "winner", "prize", "cash", "urgent", "click", "claim"]

    if any(word in text for word in spam_words):
        prediction = "spam"
    else:
        prediction = "ham"

    return jsonify({
        "input": data.get("text", ""),
        "prediction": prediction
    })
