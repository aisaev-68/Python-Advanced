from typing import List

from fastapi import FastAPI
from sqlalchemy import desc, insert, update
from sqlalchemy.future import select


import models as models
import schemas as schemas
from database import engine, session

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
        await session.execute(
            insert(models.Book).values(
                dish_name="Суп молочный",
                ingredients="Молоко, рис, соль",
                description="Очень вкусно",
                time_for_preparing=55,
            )
        )


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get(
    "/books/{recipes_id}",
    response_model=List[schemas.BookOut],
    name="Get recipes by id",
)
async def books(recipes_id: int) -> List[models.Book]:
    await session.execute(
        update(models.Book)
        .where(models.Book.id == recipes_id)
        .values(number_of_views=models.Book.number_of_views + 1)
    )
    await session.commit()
    res = await session.execute(select(models.Book).where(models.Book.id == recipes_id))

    return res.scalars().all()


@app.get("/books/", response_model=List[schemas.Recipes], name="Get all recipes")
async def get_recipes() -> List[models.Book]:
    res = await session.execute(
        select(models.Book)
        .order_by(desc("number_of_views"))
        .order_by(desc("time_for_preparing"))
    )

    return res.scalars().all()
