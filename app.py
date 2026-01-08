from flask import Flask, render_template

app = Flask(__name__)

@app.route("/old")
def old_route():
    return render_template("budget.html")

@app.route("/")
def home():
    return render_template("budget2.html")

if __name__ == "__main__":
    app.run(debug=True)