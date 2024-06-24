import os
from count import retrieve_document_id, update_document_id, storeDbase
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html",)

@app.route("/login.html", methods=["POST", "GET"])
def login():
    return render_template("login.html",)

@app.route("/result.html", methods=["POST"])
def result():
    user_data = {}
    user_data["name"] = request.form.get("User_name")
    user_data["email"] = request.form.get("User_email")
    user_data["password"] = request.form.get("User_password")
    id = retrieve_document_id()
    user_data_db = {}
    user_data_db[id] = user_data
    update_document_id(str(int(id) + 1))
    storeDbase(user_data_db)
    return render_template("login.html",)

if __name__ == "__main__":
    app.run(debug=True)
