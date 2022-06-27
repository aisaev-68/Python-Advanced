from typing import Tuple, List, Dict

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from marshmallow import ValidationError

from models import (
    DATA,
    get_all_books,
    init_db,
    add_book,
    get_book_by_id,
    update_book_by_id,
    delete_book_by_id,
)
from schemas import BookSchema

app = Flask(__name__)
api = Api(app)


class BookList(Resource):
    def get(self, id_book: int = None) -> Tuple[List[Dict], int]:
        schema = BookSchema()

        if id_book:
            return schema.dump(get_book_by_id(int(id_book))), 200
        else:
            return schema.dump(get_all_books(), many=True), 200

    def post(self) -> Tuple[Dict, int]:

        data = request.json

        schema = BookSchema()

        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201

    def put(self, id_book: int):
        parser = reqparse.RequestParser()
        parser.add_argument("author", type=str)
        parser.add_argument("title", type=str)
        params = parser.parse_args()
        book = get_book_by_id(int(id_book))
        if book:
            book.author = params['author']
            book.title = params['title']
            update_book_by_id(book)
            return f"Post with id={id_book} updated", 200
        else:
            return f"There is no record with id={id_book} in the database", 404

    def delete(self, id_book: int):

        if get_book_by_id(int(id_book)):
            delete_book_by_id(int(id_book))
            return f"Post with id={id_book} deleted", 200
        else:
            return f"There is no record with id={id_book} in the database", 404


api.add_resource(BookList, '/api/books', '/api/books/<int:id_book>')

if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)
