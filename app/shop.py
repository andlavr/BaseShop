from app.user import User
from utils.auth import AuthManager
from utils.errors import WrongLogin, WrongPassword, ShopNameError, RegistrationError
from app import models


class Shop:
    def __init__(self, name: str):
        self.name = name
        self.__user = None

    @property
    def name(self) -> str:
        """
        Получение названия магазина

        :return: str
        """

        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Установка название магазина

        :param value: str
        :return: None
        """
        if not isinstance(value, str):
            raise ShopNameError(f"Ожидается тип str, получен тип {type(value)}")

        self.__name = value

    @property
    def user(self) -> str:
        """
        Получение usera

        :return: str
        """

        return self.__user

    def __enter_to_web(self) -> str:
        """
        Формализованное приветствие
        :return: str
        """
        return f"Добро пожаловать в магазин '{self.name}'!"

    def __authentification_user(self) -> None:
        """

        :return:
        """

        auth_manager = AuthManager()

        while True:  # начинаем процедуру аутентификации
            login = input("Введите логин: ")
            try:  # Если логин введен верно и он есть в БД, то проверяем только пароль
                while True:  # Если пароль верный, то создаем пользователя, а иначе запрашиваем пароль еще раз
                    password = input("Введите пароль: ")

                    if auth_manager.check(login, password):
                        self.__user = User(login, password)
                        break
                    else:
                        print("Введен неверный пароль")
                        continue
                break

            except RegistrationError:  # Если логин введен не верно и человек захотел зарегистрироваться, то:
                # TODO: Передаём управление в RegistrationManager
                print("Регистрация")
                break
            except WrongLogin:  # Если логин введен не верно и пользователь хочет повторить ввод логина (т.е. человек уверен, что он уже зарегистрирован)
                continue

    # TODO если нет логина и пароля, то регистрация нового пользователя (class User)

    def __show_categories(self):
        pass

    def __products_category(self):
        pass

    def __show_cart(self):
        pass

    def __buy_products(self):
        pass

    def run(self):
        self.__enter_to_web()

        self.__authentification_user()

        while True:
            # if self.user is None:
            #     print("12312312")

            input("12312")
            print("Магазин запущен")
