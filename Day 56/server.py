from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("phantom/index.html")


@app.route('/cv')
def cv():
    return render_template("cv.html")

@app.route('/id')
def id():
    return render_template("id/index.html")


if __name__ == "__main__":
    app.run(debug=True)