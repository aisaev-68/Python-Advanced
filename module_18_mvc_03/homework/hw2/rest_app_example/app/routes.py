from typing import Tuple, List, Dict
from wsgiref.simple_server import WSGIRequestHandler

from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flasgger import APISpec, Swagger

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

spec = APISpec(
    title='AuthorList',
    version='1.0.0',
    openapi_version='2.0',
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)


class AuthorList(Resource):
    def get(self) -> Tuple[List[Dict], int]:
        """
        This is an endpoint for obtaining the books list.
        ---

        tags:
          - get_all_authors_and_book
        summary: Returns authors
        responses:
          200:
            description: Authors data
            schema:
              type: array
              items:
                $ref: '#/definitions/Author'

        """

        schema = AuthorSchema()

        return schema.dump(get_all_books(), many=True), 200

    def post(self) -> Tuple[Dict, int]:
        """
        This is the endpoint for adding author and book
        ---
        tags:
         - add_authors_and_book
        parameters:
         - in: body
           name: new author
           schema:
             $ref: '#/definitions/AuthorBook'
        responses:
         201:
           description: The author and book has been created
           schema:
             $ref: '#/definitions/Author'
        definitions:
          AuthorBook:
            type:
              object
            properties:
              author:
                type:
                  string
                required:
                  True
              title:
                type:
                  string
                required:
                  True
        """

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


class AuthorBook(Resource):

    def get(self, id_author: int) -> Tuple[List[Dict], int]:
        """
        This is the endpoint for getting the author with his books by id
        ---
        tags:
          - get_authors_by_id
        responses:
          200:
            description: Authors data
            schema:
              type: array
              items:
                $ref: '#/definitions/Author'
          404:
            description: There is no record in the database
        produces:
          application/json
        parameters:
          - in: path
            name: id_author
            required: true
            type: integer
            format: int64

        """

        schema = AuthorSchema()
        if id_author:
            return schema.dump(get_author_by_id(int(id_author)), many=True), 200

    def delete(self, id_author: str):
        """
        This is the endpoint for deleting an author with his books by author id
        ---
        tags:
          - delete_author_and_books_by_id
        responses:
          200:
            description: The author with his books has been deleted
          404:
            description: There is no record in the database
        parameters:
          - in: path
            name: id_author
            required: true
            type: integer
            format: int64

        """

        if id_author:
            if delete_books_by_author(id_author):
                return f"Posts with id_author={id_author} deleted", 200
            else:
                return f"There is no record with id_author={id_author} in the database", 404


template = spec.to_flasgger(
    app,
    definitions=[AuthorSchema],
)

swagger = Swagger(app, template=template)

api.add_resource(AuthorList, '/api/authors', methods=['GET', 'POST'])
api.add_resource(AuthorBook, '/api/authors/<int:id_author>', methods=['GET', 'DELETE'])

if __name__ == '__main__':
    init_db(initial_records=DATA)
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(debug=True)
