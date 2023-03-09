from core.init import db

class BooksModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128),  index=True)
    description = db.Column(db.String(255),  index=True)

