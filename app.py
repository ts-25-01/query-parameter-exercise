from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Heute ist der Moody Monday"

@app.route("/about")
def about():
    return "This is about the Moody Monday Coffe Need!"

@app.route("/info")
def info():
    return "Das sind die wichtigen Informationen über unseren Moody Monday!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hallo, {name}"

@app.route("/greet")
def main_greet():
    return "Das ist die Willkommensseite"

@app.route("/square/<int:number>")
def square_function(number):
    result = number * number
    return f"Das Quadrat von {number} ist {result}"

@app.route("/files/<path:file_path>")
def show_file(file_path):
    return f"Datei: {file_path}"


if __name__ == "__main__":
    app.run(debug=True)
