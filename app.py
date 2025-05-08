from flask import Flask, render_template, request
from password_strength import check_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = check_strength(password)
    return render_template("index.html", password=password, result=result)


if __name__ == "__main__":
    app.run(debug=True)
