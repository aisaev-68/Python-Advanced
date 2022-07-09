import os
from typing import Tuple, List, Dict, Any
import csv
from flask import Flask, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename

from handlers import get_books, get_count_books_for_author, \
    get_count_date_with_book, get_book_by_id, get_student_by_id, \
    get_issue_book, add_issue_book, update_return_date, get_search_books, \
    get_havents_read, get_avg_count_books_by_month, popular_book, most_reading_students, \
    insert_many_students

from database import create_db
from handlers import insert_data

UPLOAD_FOLDER = 'uploads/'
EXTENSIONS = 'csv'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename) -> bool:
    if '.' in filename:
        file_name, file_ext = filename.split('.')
        if file_ext == EXTENSIONS:
            return True
        else:
            return False
    return False


@app.before_request
def before_request_func():
    create_db()
    insert_data()


@app.route("/books", methods=["GET"])
def get_books_all():
    books = get_books()
    return jsonify(books), 200


@app.route("/debtors", methods=["GET"])
def get_debtors():
    debtors_student = get_count_date_with_book()

    return jsonify(debtors_student), 200


@app.route("/issue_books", methods=["POST"])
def issue_books():
    id_book = None
    id_student = None
    if request.args.get('id_book') and request.args.get('id_book') != '':
        id_book = int(request.args.get('id_book', type=str))

    if request.args.get('id_student') and request.args.get('id_student') != '':
        id_student = int(request.args.get('id_student', type=str))

    book = get_book_by_id(id_book, True)
    student = get_student_by_id(id_student)
    issue_book = get_issue_book(id_book, id_student)

    if book and student:
        if not issue_book:
            count = book.count - 1
            add_issue_book(book.id, student.id, count)
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

    book = get_book_by_id(id_book, False)
    student = get_student_by_id(id_student)
    issue_book = get_issue_book(id_book, id_student)
    if book and student:
        if issue_book:
            if not issue_book[0].date_of_return:
                count = book.count + 1
                update_return_date(id_book, id_student, count)
                return 'Книга возвращена в библиотеку', 201
            else:
                return 'Книга возвращена ранее в библиотеку', 201
        else:
            return f'Студент с id={id_student} не получал книгу с id={id_book}', 404

    else:
        return 'Ошибка! Студент или книга не регистрировались в библиотеке', 404


@app.route("/search_books", methods=["POST"])
def search_books():
    txt = ''
    if request.args.get('txt') and request.args.get('txt') != '':
        txt = request.args.get('txt', type=str)
    books_list = []
    books = get_search_books(txt)
    for book in books:
        books_as_dict = book.to_json()
        books_list.append(books_as_dict)
    return jsonify(books_list), 200


@app.route("/author_books/<int:id>", methods=["GET"])
def get_author_books(id: int):
    return jsonify(get_count_books_for_author(id)), 200


@app.route("/havent_read", methods=["GET"])
def get_havent_read():
    id_student = 0
    id_book = 0
    if request.args.get('student_id') and request.args.get('student_id') != '':
        id_student = int(request.args.get('student_id', type=str))

    if request.args.get('book_id') and request.args.get('book_id') != '':
        id_book = int(request.args.get('book_id', type=str))

    havent_books = get_havents_read(id_student, id_book)
    if havent_books:
        return jsonify(havent_books), 200
    else:
        return 'У автора нет других книг', 201


@app.route("/books/reads/avg", methods=["GET"])
def get_avg_books_by_month():
    month_avg_books = get_avg_count_books_by_month()
    if month_avg_books:
        return {'avg_amount_books': month_avg_books}, 200
    else:
        return 'Нет данных', 201


@app.route("/books/populars", methods=["GET", 'POST'])
def get_popular_book():
    book = popular_book()
    if book:
        return book, 200
    else:
        return 'Нет данных', 201


@app.route("/students/most_reading", methods=["GET"])
def get_most_reading_students():
    students = most_reading_students()
    if students:
        return students, 200
    else:
        return 'Нет данных', 201


@app.route('/students/uploads', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            students_list = list()
            with open(UPLOAD_FOLDER + filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=";")
                for row in reader:
                    student = {
                        'name': row['name'],
                        'surname': row['surname'],
                        'phone': row['phone'],
                        'email': row['email'],
                        'average_score': float(row['average_score']),
                        'scholarship': True if row['scholarship'] == 'True' else False
                    }
                    students_list.append(student)
            insert_many_students(students_list)

            return redirect(url_for('upload_form',
                                    filename=filename))
    return """
    <!doctype html>
    <title>Загрузить новый файл</title>
    <h1>Загрузить новый файл</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </html>
    """


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
