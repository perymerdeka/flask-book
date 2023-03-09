from flask_restx import Resource, reqparse

# import initial
from core.init import db

# import Model
from apps.books.models import BooksModel


# import schema
from apps.books.schema import BookSchema

books_parser = reqparse.RequestParser()

class BooksAPIView(Resource):
    def get(self):
        # logika yang akan diterapkan di API
        books = BooksModel.query.all()
        book_schema = BookSchema()

        return book_schema.dump(books, many=True)
    
    def post(self):
        args = books_parser.parse_args()
        books = BooksModel(title=args['title'], description=args['description'])
         
        # serialisasi object
        book_schema = BookSchema()

        # save ke database
        db.session.add(books)
        db.session.commit()
        return book_schema.dump(books, many=True)


         