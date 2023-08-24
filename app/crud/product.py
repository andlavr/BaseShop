import typing

from app.cms import category_manager
from app.crud.category import get_category_id
from app.crud.models import session, Product, Category, CategoryProducts


def add_product(name: str, price: float, rating: float) -> None:
    """
    Добавление продуктов в БД

    :param name: объект типа str
    :param price: объект типа float
    :param rating: объект типа float
    :return: None
    """

    new_product = Product(name=name, price=price, rating=rating)

    session.add(new_product)

    session.commit()


def get_product_id(name: str) -> typing.Union[int]:
    """
    Получение id  продукта

    :param name: объект типа str
    :return: объект типа id
    """

    product_id = session.query(Product).filter_by(name=name).first()
    return product_id.id


def add_category_products(cat_db_id: int, prod_db_id: int) -> None:
    """
    Добавление id категории и id продукта в таблицу

    :param cat_db_id: объект типа id
    :param prod_db_id: объект типа id
    :return: None
    """

    add_idds = CategoryProducts(category_id=cat_db_id, product_id=prod_db_id)

    session.add(add_idds)
    session.commit()


if __name__ == '__main__':
    pass
