from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hi welcome to the homepage</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    # return "Hi Admin"
    # return redirect(url_for("index"))
    return redirect(url_for("user", name="admin!!"))

if __name__ == "__main__":
    app.run(debug=True)