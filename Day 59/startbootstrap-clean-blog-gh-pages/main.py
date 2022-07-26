import os
import requests
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_PASSWORD"] = "uzwpjqdzgfpzsnxy"
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "euclyd@gmail.com"


@app.route("/")
def main():
    url = "https://api.npoint.io/4cedc647e52fc72c2543"
    response = requests.get(url)
    posts = response.json()
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():

    if request.method == "GET":
        return render_template("contact.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        mail = Mail(app)
        msg = Message('Hello from the other side!', sender='euclyd@gmail.com', recipients=['euclyd@gmail.com'])
        msg.body = f"Flask email test - Name: {name}, email: {email}"
        mail.send(msg)
        return render_template("mail.html", name=name, email=email)


@app.route("/mail", methods=["POST"])
def mail():

    return render_template("mail.html", name=name, email=email)

@app.route("/post/<int:id>")
def post(id):
    url = "https://api.npoint.io/4cedc647e52fc72c2543"
    response = requests.get(url)
    posts = response.json()
    return render_template("post.html", blog_id=id, all_posts=posts)

if __name__ == "__main__":
    app.run(debug=True)


main()
