from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()

    return render_template("index.html", posts=all_posts)


# id needs to be an integer not a string
@app.route('/post/<int:id>')
def post(id):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_posts = response.json()
    returned_post = None

    for blog_post in all_posts:
        if blog_post['id'] == id:
            returned_post = blog_post

    return render_template("post.html", returned_post=returned_post)


if __name__ == "__main__":
    app.run(debug=True)
