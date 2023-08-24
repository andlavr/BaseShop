import typing

from app.crud.category import get_category_id
from app.crud.models import session, Category, Product, CategoryProducts


def show_categories() -> None:
    """
    Демонстрация списка категорий из БД

    :return: None
    """

    loaded_categories = session.query(Category)
    for cat in loaded_categories:
        print(cat.name)


def load_category_products(name: str) -> typing.List[tuple]:
    """
    Загрузка категории и списка продуктов относящихся к ней из БД

    :return: список кортежей типа (id продукта, название продукта, цена продукта, рейтинг продукта)
    """

    loaded_cat_prod = session.query(Product).join(CategoryProducts).filter(
        CategoryProducts.category_id == get_category_id(name))

    return [(prod.id, prod.name, prod.price, prod.rating) for prod in loaded_cat_prod]


if __name__ == '__main__':
    print(load_category_products('Мясо свежее'))
