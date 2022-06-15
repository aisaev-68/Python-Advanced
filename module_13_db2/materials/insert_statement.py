import sqlite3


class AddingItem:
    def __init__(self, name: str, description: str, amount: int) -> None:
        self.name = name
        self.description = description
        self.amount = amount


def input_new_item() -> AddingItem:
    name = input("Введите имя продукта\n>")
    description = input("Введите описание продукта\n>")
    amount = input("Введите остаток на складе\n>")

    amount_val = int(amount)

    return AddingItem(name=name, description=description, amount=amount_val)


if __name__ == "__main__":
    with sqlite3.connect("db_1.db") as conn:
        cursor = conn.cursor()

        new_item = input_new_item()

        cursor.execute(
                """
            INSERT INTO `table_warehouse` (name, description, amount) VALUES 
                (?, ?, ?);
            """,
                (new_item.name, new_item.description, new_item.amount),
        )
