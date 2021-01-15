from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")


@app.route("/home.html")
def index():
    return render_template("home.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/projects.html")
def test():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)