from pydantic import BaseModel


class BookIn(BaseModel):
    dish_name: str
    ingredients: str
    description: str
    time_for_preparing: int

    class Config:
        orm_mode = True


class BookOut(BaseModel):
    id: int
    dish_name: str
    ingredients: str
    description: str
    time_for_preparing: int

    class Config:
        orm_mode = True


class Recipes(BaseModel):
    dish_name: str
    number_of_views: int
    time_for_preparing: int

    class Config:
        orm_mode = True
