from flask import Flask
import random


app = Flask(__name__)

answer = str(random.randint(0,9))
print(answer)

def color_decorator(function):
    def wrapper(*args,**kwargs):
        colors =['red', 'blue', 'green']
        color = random.choice(colors)
        return f"<h1 style='color:{color}'>{function(**kwargs)}</h1>"
    return wrapper

@app.route('/')
def body():
    return "<b>Guess a number between 0 and 9 by adding your guess to the url </b>"


@app.route('/<n>')
@color_decorator
def number(n):
    global answer
    if n > answer:
        return "too high!"
    elif n < answer:
        return "Too low!"
    else:
        return "Correct!"



if __name__ == "__main__":
    app.run(debug=True)


