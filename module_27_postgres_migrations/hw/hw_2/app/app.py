from typing import Dict, Any

from sqlalchemy import Column, Integer, String, Boolean, \
    ForeignKey, select, create_engine, ARRAY, distinct
from sqlalchemy.sql import expression
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import sessionmaker, relationship
from request_http import main

app = Flask(__name__)

DATABASE_URL = "postgresql+psycopg2://dbadmin:12345@postgresql:5432/skillbox_db"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Coffee(Base):
    __tablename__ = 'coffee'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    origin = Column(String(200))
    intensifier = Column(String(200))
    notes = Column(ARRAY(item_type=String, as_tuple=True))

    def __repr__(self):
        return f"Товар {self.title}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    has_sale = Column(Boolean, server_default=expression.true(), nullable=False)
    address = Column(JSON, default=[])
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    coffee = relationship("Coffee", backref="coffee")

    def __repr__(self):
        return f"Пользователь {self.name}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


@app.before_first_request
def before_first_request_func() -> None:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    object = []
    if not session.query(Coffee).all():
        data = main()
        print(data)
        for user in data['user']:
            # id=user['id'],
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
