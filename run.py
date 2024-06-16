from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html",)

@app.route("/login.html", methods=["POST", "GET"])
def login():
    return render_template("login.html",)

@app.route("/result", methods=["POST"])
def result():
    list_result = []
    list_result.append(request.form.get("User_name"))
    list_result.append(request.form.get("Login"))
    return list_result

if __name__ == "__main__":
    app.run(debug=True)
