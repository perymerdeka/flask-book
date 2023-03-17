from flask_restx import Resource, reqparse

# import initial
from core.init import db

# import Model
from apps.books.models import BooksModel


# import schema
from apps.books.schema import book_schema, books_schema

books_parser = reqparse.RequestParser()

class BooksAPIView(Resource):
    def get(self):
        # logika yang akan diterapkan di API
        books = BooksModel.query.all()

        return books_schema.dump(books, many=True)
    
    def post(self):
        books_parser.add_argument('title', required=True, help="Name cannot be blank!")
        books_parser.add_argument('description', required=True, help="Name cannot be blank!")
        args = books_parser.parse_args()
       
        books = BooksModel(title=args['title'], description=args['description'])
         
        # serialisasi object

        # save ke database
        db.session.add(books)
        db.session.commit()
        return book_schema.dump(books)


         