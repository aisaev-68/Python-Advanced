from typing import Tuple, List, Dict

from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError

from models import (
    DATA,
    get_all_books,
    init_db,
    add_book,
    get_author, get_author_by_id, add_author_and_book, delete_books_by_author,
)
from schemas import AuthorSchema

app = Flask(__name__)
api = Api(app)


class AuthorList(Resource):
    def get(self, id_author: int = None) -> Tuple[List[Dict], int]:
        schema = AuthorSchema()

        if id_author:
            return schema.dump(get_author_by_id(int(id_author)), many=True), 200
        else:
            return schema.dump(get_all_books(), many=True), 200

    def post(self) -> Tuple[Dict, int]:

        data = request.json

        schema = AuthorSchema()

        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        books_author = get_author(book.author)

        if books_author is None:
            books = add_author_and_book(book)
        else:
            book.id_author = books_author.id_author
            books = add_book(book)

        return schema.dump(books), 201

    def delete(self, id_author: str):
        if id_author:
            delete_books_by_author(id_author)
            return f"Posts with id_author={id_author} deleted", 200
        else:
            return f"There is no record with id_author={id_author} in the database", 404


api.add_resource(AuthorList, '/api/authors', '/api/authors/<int:id_author>')

if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)
