from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="Cloud API is running")

@app.get("/api/greet/<name>")
def greet(name):
 return jsonify(message=f"Hello, {name}!")

@app.route("/api/message", methods=["GET", "POST"])
def create_message():
    return jsonify(message="POST request received")

if __name__ == "__main__":
    app.run(debug=True)