from sqlalchemy import String, select, distinct
from flask import Flask, jsonify, request
from models import engine, Base, session, User, Coffee
from request_http import main

app = Flask(__name__)

@app.before_first_request
def before_first_request_func() -> None:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    object = []
    if not session.query(Coffee).all():
        data = main()
        for user in data['user']:
            object.append(User(name=user['name'],
                               has_sale=user['has_sale'],
                               address=user['address'],
                               coffee_id=user['coffee_id']))

        for coffee in data['coffees']:
            # id=coffee['id'],
            object.append(Coffee(title=coffee['title'],
                                 origin=coffee['origin'],
                                 intensifier=coffee['intensifier'],
                                 notes=coffee['notes']))

        session.add_all(object)
        session.commit()


@app.route("/users", methods=['GET'])
def get_users():
    users = session.query(User).all()
    users_list = []
    for u in users:
        user_obj = u.to_json()
        user_obj['coffee'] = u.coffee.to_json()
        users_list.append(user_obj)
    return jsonify(users_list)


@app.route('/users/', methods=['POST'])
def add_user():
    data = request.json
    if data:
        session.add(User(**data))
        session.commit()
    return 'User added', 201


@app.route('/coffees/', methods=['GET'])
def search_coffee():
    search_title = ''
    if request.args.get('search_title') and request.args.get('search_title') != '':
        search_title = request.args.get('search_title', type=str)

    query = select(Coffee.id, Coffee.title, Coffee.origin, Coffee.intensifier, Coffee.notes). \
        where(Coffee.title.match(search_title, postgresql_regconfig='english'))

    coffees = session.execute(query).all()
    coffees_list = []

    fields = ['id', 'title', 'origin', 'intensifier', 'notes']
    for coffee in coffees:
        coffees_as_dict = dict(zip(fields, coffee))
        coffees_list.append(coffees_as_dict)

    return jsonify(coffees_list), 200


@app.route('/countryes/', methods=['GET'])
def get_users_country():
    country_search = ''
    if request.args.get('country') and request.args.get('country') != '':
        country_search = request.args.get('country', type=str)

    users_country = session.query(User.id, User.name, User.has_sale, User.address). \
        filter(User.address['country'].astext.cast(String) == country_search).all()

    users_list = []
    fields = ['id', 'name', 'has_sale', 'address']
    for user in users_country:
        users_as_dict = dict(zip(fields, user))
        users_list.append(users_as_dict)
    return jsonify(users_list), 200


@app.route("/unique_notes/", methods=['GET'])
def get_unique_notes():
    notes = session.query(distinct(Coffee.notes)).all()
    list_notes = set()
    for note in notes:
        for item in tuple(note[0]):
            list_notes.add(item)
    return jsonify([{'unique_notes': sorted(list(list_notes))}]), 201
