from typing import Tuple, List, Dict, Any

from flask import Flask, request, jsonify

from model import Author, Book, Student, ReceivingBook, Base, engine
from generate_date import insert_data

app = Flask(__name__)


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)
    if not Book.get_all_books():
        insert_data()


@app.route("/books", methods=["GET"])
def get_books_all():
    book_list = []
    books = Book.get_books()
    for book in books:
        book_as_dict = book.to_json()
        book_list.append(book_as_dict)

    return jsonify(book_list=book_list), 200


@app.route("/debtors", methods=["GET"])
def get_debtors():
    debtors_list = []
    debtors_student = ReceivingBook.get_count_date_with_book()
    for student in debtors_student:
        debtors_as_dict = student.to_json()
        debtors_list.append(debtors_as_dict)
    return jsonify(debtors_list), 200


@app.route("/issue_books", methods=["POST"])
def issue_books():
    id_book = None
    id_student = None
    if request.args.get('id_book') and request.args.get('id_book') != '':
        id_book = int(request.args.get('id_book', type=str))

    if request.args.get('id_student') and request.args.get('id_student') != '':
        id_student = int(request.args.get('id_student', type=str))

    book = Book.get_book_by_id(id_book, True)
    student = Student.get_student_by_id(id_student)
    issue_book = ReceivingBook.get_issue_book(id_book, id_student)

    if book and student:
        if not issue_book:
            count = book.count - 1
            ReceivingBook.add_issue_book(book.id, student.id, count)
            return 'Книга выдана студенту', 201
        else:
            return 'Книга выдана студенту ранее', 201
    else:
        return 'Студент или книга отсутствует в базе', 404


@app.route("/return_books", methods=["POST"])
def return_books():
    id_book = None
    id_student = None
    if request.args.get('id_book') and request.args.get('id_book') != '':
        id_book = int(request.args.get('id_book', type=str))

    if request.args.get('id_student') and request.args.get('id_student') != '':
        id_student = int(request.args.get('id_student', type=str))

    book = Book.get_book_by_id(id_book, False)
    student = Student.get_student_by_id(id_student)
    issue_book = ReceivingBook.get_issue_book(id_book, id_student)
    if issue_book:
        if book and student:
            count = book.count + 1
            ReceivingBook.update_return_date(id_book, id_student, count)
            return 'Книга возвращена в библиотеку', 201
        else:
            return 'Ошибка! Студент или книга отсутствует в базе', 404
    else:
        return 'Книга возвращена ранее в библиотеку', 201


@app.route("/search_books", methods=["POST"])
def search_books():
    txt = ''
    if request.args.get('txt') and request.args.get('txt') != '':
        txt = request.args.get('txt', type=str)
    books_list = []
    books = Book.get_search_books(txt)
    for book in books:
        books_as_dict = book.to_json()
        books_list.append(books_as_dict)
    return jsonify(books_list), 200


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
