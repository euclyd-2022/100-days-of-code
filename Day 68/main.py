from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    plainpw = db.Column(db.String(100))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        if User.query.filter_by(email=email).first() == None:
            new_user = User(email=email, name=name, password=hash, plainpw=password)
            db.session.add(new_user)
            db.session.commit()
            db.session.refresh(new_user)
            login_user(new_user)
            return redirect(url_for('secrets'))
        else:
            flash("User already exists")
            return render_template("login.html")
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        error= None
        email = request.form.get('email')
        password = request.form.get('password') # 1234

        user = User.query.filter_by(email=email).first()
        print(user)
        if user == None:
            flash("error - user not found")
            return render_template("login.html")
        else:
            print(f"{password} / {user.password}")

            if check_password_hash(user.password, password):

                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash("error logging in!")
                return render_template("login.html")





    return render_template("login.html")


@app.route('/secrets/')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
   return send_from_directory("./static/files", "cheat_sheet.pdf")



if __name__ == "__main__":
    app.run(debug=True)
