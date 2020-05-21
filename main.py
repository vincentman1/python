from flask import Flask

app = Flask(main.py)

@app.route("/")
def home():
    return "Hello, world"

if main.py == "main.py":
    app.run(debug=True)