from sqlalchemy import Column, Integer, String

from database import Base



class Book(Base):
    __tablename__ = "Book"
    id = Column(Integer, primary_key=True, index=True)
    dish_name = Column(String, index=True)
    ingredients = Column(String, index=True)
    description = Column(String, index=True)
    time_for_preparing = Column(Integer, index=True)
    number_of_views = Column(Integer, nullable=False, default=0)
