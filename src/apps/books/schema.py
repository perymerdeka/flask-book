from core.init import ma
from apps.books.models import BooksModel


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BooksModel
        include_fk = True

book_schema = BookSchema()
books_schema = BookSchema(many=True)


