from typing import List

from fastapi import FastAPI
from sqlalchemy.future import select
from sqlalchemy import update, desc
import models
import schemas
from database import engine, session

app = FastAPI()


@app.on_event("startup")
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


# @app.post('/books/', response_model=schemas.BookOut)
# async def books(book: schemas.BookIn) -> models.Book:
#     new_book = models.Book(**book.dict())
#     async with session.begin():
#         session.add(new_book)
#     return new_book

@app.get('/books/{recipes_id}', response_model=List[schemas.BookOut], name='Get recipes by id')
async def books(recipes_id: int) -> List[models.Book]:

    await session.execute(update(models.Book).where(
        models.Book.id == recipes_id).values(number_of_views=models.Book.number_of_views + 1))
    await session.commit()
    res = await session.execute(select(models.Book).where(models.Book.id == recipes_id))

    return res.scalars().all()


@app.get("/books/", response_model=list[schemas.Recipes], name='Get all recipes')
async def get_recipes() -> List[models.Book]:
    res = await session.execute(select(models.Book).order_by(desc('number_of_views')).order_by(desc('time_for_preparing')))

    return res.scalars().all()
