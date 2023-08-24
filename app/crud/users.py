from app.crud.models import session, Users


def login_is_exists(login: str) -> bool:
    """
    Проверка наличия пользователя в БД

    :param login: объект типа str
    :return: bool
    """

    result = session.query(Users).filter_by(login=login).first()
    return bool(result)


def add_user(login: str, password: str) -> None:
    """
    Добавление пользователя в БД

    :param login: объект типа str
    :param password: объект типа str
    :return: None
    """

    new_user = Users(login=login, password=password)
    session.add(new_user)

    # Добавить данные в таблицу
    session.commit()


def get_password(login: str) -> str:
    """
    Получение пароля

    :param login: объект типа str
    :return: объект типа str
    """

    result = session.query(Users).filter_by(login=login).first()
    return result.password


if __name__ == '__main__':
    print(login_is_exists("user_1"))
    print(login_is_exists("user_2"))
    print(login_is_exists("user_3"))
