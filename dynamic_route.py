from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def print_person(name):
    return f"hello {name}"

@app.route('/<int:id>')
def print_id(id):
    return f"Id - {id}"

if __name__ == '__main__':
    app.run()