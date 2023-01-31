from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

"""
Use the bellow code to run flask app programmatically
"""
if __name__ == '__main__':
    app.run()