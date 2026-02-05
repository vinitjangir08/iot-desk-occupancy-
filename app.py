from flask import Flask, render_template, jsonify

app = Flask(__name__)

# This will be fake/mock status
desk_status = "Empty"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/status")
def status():
    # we will toggle status every request for demo
    global desk_status
    desk_status = "Occupied" if desk_status == "Empty" else "Empty"
    return jsonify({"desk": desk_status})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
