from flask import Flask

app = Flask(pythontest)

@app.route("/")
def home():
    return "Hello, world"
    
if pythontest == "pythontest":
    app.run(debug=True)