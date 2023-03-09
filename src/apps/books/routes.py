# daftar views si route nya

from flask import Blueprint
from flask_restx import Api

# import View yang akan dipake
from apps.books.views import BooksAPIView

books_bp = Blueprint("books", __name__)

# api
books_api = Api(books_bp)

# konfigurasi rute yang ada di views

books_api.add_resource(BooksAPIView, "/books")