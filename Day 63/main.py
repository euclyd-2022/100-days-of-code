from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///day63_books.db"
db = SQLAlchemy(app)
Bootstrap(app)

all_books = []


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


@app.route('/', methods=['GET','POST'])
def home():
    empty = ""


    #if len(all_books) == 0:
    if db.session.query(Books).all == 0:
        empty = "Library is empty"

    if request.args.get('id'):
        book_id = request.args.get('id')
        book_to_delete = Books.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))

    all_books = db.session.query(Books).all()

    return render_template('index.html', books=all_books, empty=empty)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        #add to dictionary
        new_book = {}
        new_book['title'] = request.form.get('title')
        new_book['author'] = request.form.get('author')
        new_book['rating'] = request.form.get('rating')

        # SQLite insert using sqlalchemy

        sqlite_book = Books(title=request.form.get('title'), author=request.form.get('author'), rating=request.form.get('rating'))
        db.session.add(sqlite_book)
        db.session.commit()
        all_books.append(new_book)
        print(all_books)
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['POST','GET'])
def edit(id):
    book = Books.query.filter_by(id=id).first()
    if request.method == 'POST':
        #update sql
        book_to_update = Books.query.get(id)
        book_to_update.rating = request.form.get('rating')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book)

if __name__ == "__main__":
    app.run(debug=True)

