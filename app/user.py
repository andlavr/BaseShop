import hashlib
import typing

from app.cart import Cart
from utils.counters import UserIdCounter

from utils.errors import UsernameError, PasswordError


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.__cart = Cart()
        self.__id = next(UserIdCounter.user_id_generator())

    def __repr__(self):
        """
        Возвращение строки с помощью которой был создан объект

        :return: строка для __repr__
        """

        return f'{self.__class__.__name__}(username={self.__username!r}, password=<HIDDEN>)'

    def __str__(self):
        """
        Возвращение читаемого варианта строки с помощью которой был создан объект

        :return: строка для __str__
        """

        return f'Имя пользователя: {self.__username}'

    @property
    def username(self) -> str:
        """
        Передача имени пользователя

        :return: Объект типа str
        """

        return self.__username

    @username.setter
    def username(self, value: str) -> None:
        """
        Установка имени пользователя

        :param value: Объект типа str
        :return: None
        """

        if not isinstance(value, str):
            raise UsernameError(f'Ожидается тип str. Получен {type(value)}')

        self.__username = value

    @property
    def password(self) -> str:
        """
        Получение пароля пользователя

        :return: пароль в виде строки
        """

        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        """
        Установка пароля

        :param value: пароль в виде строки
        :return: None
        """

        if not isinstance(value, str):
            raise PasswordError(f'Ожидается тип str. Получен {type(value)}')

        self.__password = hashlib.sha256(value.encode()).hexdigest()

    @property
    def cart(self) -> Cart:
        """
        Получение корзины

        :return: Объект типа Cart
        """

        return self.__cart

    @property
    def id_(self):
        """
        Получение id

        :return: Объект типа str
        """
        return self.__id




if __name__ == '__main__':
    # print(User.creat_cart(username='Вася'))
    test_user = User(username='Вася', password='12345')
    # test_user.cart.add_product()
    test_user = User()

    print(repr(test_user))
    test_user_2 = User(username='Петя', password='12345')
    print(test_user_2)
    # print(test_user.create_username(username='Вася', users_list=[]))
