from flask import Flask, render_template

app = Flask(__name__)

@app.route("/old")
def home():
    return render_template("budget.html")

@app.route("/")
def old_budget():
    return render_template("budget2.html")

@app.route("/new")
def new_budget():
    return render_template("budget3.html")

if __name__ == "__main__":
    app.run(debug=True)