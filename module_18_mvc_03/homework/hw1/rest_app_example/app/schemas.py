from typing import Dict

from marshmallow import Schema, fields, ValidationError, post_load, validates_schema

from models import get_book_by_title, Book, get_author


class AuthorSchema(Schema):
    id_author = fields.Int(dump_only=False)
    title = fields.Str(required=True)
    author = fields.Str(required=True)

    @validates_schema
    def validate_author_and_title(self, data, **kwargs) -> None:
        if get_author(data['author']) is not None:
            if get_book_by_title(data['title']) is not None:
                raise ValidationError(
                    'Book with title "{title}" already exists, '
                    'please use a different title.'.format(title=data['title'])
                )

    @post_load
    def create_book(self, data: Dict, **kwargs) -> Book:
        return Book(**data)

