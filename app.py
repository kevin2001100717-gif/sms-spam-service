from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SMS Spam Classification Service</h1>
    <p>This service predicts whether an SMS message is spam or ham.</p>
    <p>Test example: <a href="/predict">Click here to test prediction</a></p>
    """

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        data = request.get_json()
        text = data.get("text", "")
    else:
        text = "Congratulations, you won a free prize!"

    spam_words = ["free", "win", "winner", "prize", "cash", "urgent", "click", "claim"]

    if any(word in text.lower() for word in spam_words):
        prediction = "spam"
    else:
        prediction = "ham"

    return jsonify({
        "input": text,
        "prediction": prediction
    })
