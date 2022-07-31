from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_API_KEY = "3f0182be967bf9b731377774abfa8540"

# API read access token: eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZjAxODJiZTk2N2JmOWI3MzEzNzc3NzRhYmZhODU0MCIsInN1YiI6IjYyZTNhYWExZTI1ODYwMDA1Yzc2YzQ5YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._jHQkKRugn7eOr0gl1QqQ65eC_hen98UWiEk1a0TssY
# API example url - https://api.themoviedb.org/3/movie/550?api_key=3f0182be967bf9b731377774abfa8540


class MyForm(FlaskForm):
    update_rating = StringField(label='Rating out of 10', validators=[DataRequired()])
    update_review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label="Update")

class addForm(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///day64.db"
Bootstrap(app)
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    description = db.Column(db.String(255))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.Text)
    img_url = db.Column(db.String(255))


    def __repr__(self):
        return f"<Movie {self.title}>"

# create the database
# db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

# 10. Weird Science
# 9. Kick Ass
# 8. Supe 2
# 7. Usual Suspects
# 6. Flash G
# 5. ESB
# 4. Se7en
# 3. Die hard
# 2. Ferris B
# 1. Aliens

@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    for n in range(len(all_movies)):
        all_movies[n].ranking = len(all_movies) - n
        db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:id>", methods=['POST','GET'])
def edit(id):
    movie = Movie.query.filter_by(id=id).first()
    form = MyForm()

    if form.validate_on_submit():
        # update sql
        movie_to_update = Movie.query.get(id)
        # update using wtform
        movie_to_update.rating = request.form.get('update_rating')
        movie_to_update.review = request.form.get('update_review')
        # update using range slider
        # movie_to_update.rating = request.form.get('rating')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['POST','GET'])
def add():
    add_movie = addForm()
    new_movie_title = add_movie.movie_title.data
    print(new_movie_title)
    if add_movie.validate_on_submit():
        params = {
            "api_key": TMDB_API_KEY,
            "query": new_movie_title,
        }
        response = requests.get('https://api.themoviedb.org/3/search/movie', params=params)
        data = response.json()['results']
        return render_template("select.html", options=data)
    return render_template("add.html", add=add_movie)


@app.route("/select", methods=['POST','GET'])
def select():
    movieid=request.args.get('movieid')

    response = requests.get(f'https://api.themoviedb.org/3/movie/{movieid}?api_key={TMDB_API_KEY}')
    data = response.json()
    print(data)
    new_movie_id = add_new_movie(data)
    return redirect(url_for('edit', id=new_movie_id))

def add_new_movie(data):
    new_movie = Movie(
        title=data['original_title'],
        year=data['release_date'],
        description=data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    db.session.refresh(new_movie)
    print(new_movie.id)
    return new_movie.id





if __name__ == '__main__':
    app.run(debug=True)
