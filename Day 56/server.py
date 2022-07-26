from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("phantom/index.html")

@app.route('/guess/<name>')
def guess(name):
    response1 = requests.get(f"https://api.agify.io?name={name}")
    response1.raise_for_status()
    age = response1.json()

    response2 = requests.get(f"https://api.genderize.io?name={name}")
    response2.raise_for_status()
    gender = response2.json()
    return f"<h2>Hi {name.title()}</h1><p><h2>Your age is probably {age['age']} and your gender is probably {gender['gender']}</h2></p>"

@app.route('/cv')
def cv():
    return render_template("cv.html")

@app.route('/id')
def id():
    current_year = datetime.date.today().year
    return render_template("id/index.html", year=current_year)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)