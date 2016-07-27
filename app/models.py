from app import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    isbn = db.Column(db.Integer, unique=True, index=True)
    name = db.Column(db.String(120), index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    @staticmethod
    def search_for_book_by_name(book_name):
        return Book.query.filter(Book.name.like(book_name+'%')).all()

    def __repr__(self):
        return '<Book %r>' % self.name


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(64), index=True)
    books = db.relationship('Book', backref='category', lazy='dynamic')

    @staticmethod
    def search_books_by_cateory(category_name):
        return Category.query.filter(Category.name==category_name).all()

    def __repr__(self):
        return '<Category %r>' % self.name
