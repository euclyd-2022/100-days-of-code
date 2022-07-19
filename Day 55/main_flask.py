from flask import Flask

#app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/")
@make_bold
@make_underline
@make_emphasis
def home():
    return "<h1 style='text-aligh:center'>home</h1>" \
           "<p>new paragraph</p>" \
           "<img src ='https://cdn.vox-cdn.com/uploads/chorus_asset/file/16019250/log_2048.png'>"


@app.route("/user/<name>/<int:age>")
def greet(name, age):
    return f"hello {name}, you are {age} years old"

# converter to path so that '/' can be included in the variable
# returns eg. paul/1/2/3 from http://127.0.0.1:5000/path_test/paul/1/2/3

@app.route("/path_test/<path:path>")
def display_path(path):
    return f"{path}"

if __name__ == "__main__":
    pass
    # app.run(debug=True)


