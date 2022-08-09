from typing import Dict, Any

from sqlalchemy import Column, Integer, String, ARRAY, Boolean, JSON, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import expression
from sqlalchemy.ext.declarative import declarative_base


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
    username = Column(String(50), nullable=False)
    has_sale = Column(Boolean, server_default=expression.true(), nullable=False)
    address = Column(JSON, default=[])
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    coffee = relationship("Coffee", backref="coffee")

    def __repr__(self):
        return f"Пользователь {self.name}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}
