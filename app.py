from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_privacy_score(data):
    risk_factors = {
        "phone": 10, "address": 10, "dob": 10, "social_media": 10
    }
    score = sum(risk_factors[key] for key in risk_factors if data.get(key))
    return score

@app.route("/", methods=["GET", "POST"])
def index():
    risk_score = None
    user_data = {}

    if request.method == "POST":
        user_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "address": request.form.get("address"),
            "dob": request.form.get("dob"),
            "social_media": request.form.get("social_media"),
        }
        risk_score = calculate_privacy_score(user_data)

    return render_template("index.html", risk_score=risk_score, user_data=user_data)

if __name__ == "__main__":
    app.run(debug=True)
