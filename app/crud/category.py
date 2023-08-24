import typing

from app.crud.models import session, Category


def add_category(name: str) -> None:
    """
    Добавление категории в БД

    :param name: объект типа str
    :return: None
    """

    new_category = Category(name=name)

    session.add(new_category)

    # Добавить данные в таблицу
    session.commit()


def get_category_id(name: str) -> typing.Union[int]:
    """
    Получение id категории

    :param name: объект типа str
    :return: id категории
    """

    category_id = session.query(Category).filter_by(name=name).first()
    return category_id.id
