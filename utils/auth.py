import hashlib
import secrets
import string
import sys

from utils.errors import PasswordTooShortError, WrongLogin, RegistrationError
from app.models import db


def is_good_password(password:str) -> str:
    """
    Проверка пароля

    :param password: пароль для проверки
    :return: ???
    """
    # TODO: Переделать при реализации регистрации

    if len(password) < 8:
        raise PasswordTooShortError('Пароль слишком короткий')
    else:
        if password.isalnum():
            return password


class RegistrationManager:
    ...


class AuthManager:

    def __init__(self) -> None:
        self.__db = db["users"]

    def check(self, login, password) -> bool:
        """
        Проверка пароля

        :return: True или False
        """

        if login not in self.__db.keys():

            while True:
                print("Пользователь не найден\n")
                user_choose = input(
                    "Для регистрации введите - 0\nДля повторного ввода введите - 1\nДля выхода введите - 2\nВвод: "
                )
                if user_choose not in ['0', '1', '2']:
                    print("Введено неверное значение")
                    continue

                if user_choose == '0':
                    raise RegistrationError
                elif user_choose == '1':
                    raise WrongLogin(f"Внимание! Такого логина '{login}' не существует! Проверьте правильность логина.")
                elif user_choose == '2':
                    sys.exit()

        db_password = self.__db[login]

        if db_password == hashlib.sha256(password.encode()).hexdigest():
            return True
        else:
            return False


if __name__ == '__main__':
    auth_manager = AuthManager()
    print(auth_manager.check('user_1', '123456789q!'))

    # print(password)
    # print(password.password)
    # print(password.get())
    # print(password.check("g23SD45sa"))
    # print(password.check("GRz3988XV"))
