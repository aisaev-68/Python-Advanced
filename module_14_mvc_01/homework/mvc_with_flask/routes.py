from typing import List, Dict

from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

from models import (DATA, add_book, get_all_books, init_db,
                    insert_book_counter, search_book, select_book_counter,
                    update_book_counter)

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    book_title = StringField(validators=[InputRequired()])
    author_full_name = StringField(validators=[InputRequired()])


class SearchForm(FlaskForm):
    author_full_name = StringField(validators=[InputRequired()])


def _get_html_table_for_books(books: List[Dict]) -> str:
    table = """
<table>
    <thead>
    <tr>
        <th>ID</td>
        <th>Title</td>
        <th>Author</td>
    </tr>
    </thead>
    <tbody>
        {books_rows}
    </tbody>
</table>
"""
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books():
    return render_template('index.html', books=get_all_books(),
    )


@app.route('/books/form')
def get_books_form():
    return render_template('add_book.html')


@app.route('/books/add', methods=['GET', 'POST'])
def add_book_form():
    form = RegistrationForm()
    book_title = request.form['book_title']
    author_full_name = request.form['author_full_name']
    if form.validate_on_submit():
        add_book((book_title, author_full_name))
    return redirect(url_for('get_books_form'))


@app.route('/books/form/search')
def search_books_form():
    return render_template('search.html')


@app.route('/books/results', methods=['GET', 'POST'])
def search_book_results():
    form = SearchForm()
    results = []
    search_string = request.form['author_full_name']
    counter = 0
    if form.validate_on_submit():
        results = search_book(search_string)
        id_table_books = results[0].id

        data_counter = select_book_counter((id_table_books,))
        if data_counter:
            counter = data_counter[0][2] + 1
            update_book_counter((counter, id_table_books))
        else:
            counter += 1
            insert_book_counter((id_table_books, counter))

    return render_template('index.html', books=results, count=counter)


if __name__ == '__main__':
    init_db(DATA)
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
