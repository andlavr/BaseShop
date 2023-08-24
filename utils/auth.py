import hashlib
import sys
import typing

from app.crud import users as users_crud
from app.user import User
from utils.errors import RegistrationError


def is_good_password(password: str) -> str:
    """
    Проверка пароля

    :param password: пароль для проверки
    :return: объект типа str
    """

    # TODO: Переделать в дальнейшем (добавить больше проверок)

    if len(password) < 8:
        return False
    return True


class RegistrationManager:
    def __init__(self):
        pass

    @staticmethod
    def __login_is_free(login: str) -> bool:
        """
        Проверка логина на существование

        :param login: login пользователя
        :return: True - логин свободен, иначе False
        """

        if not users_crud.login_is_exists(login):
            return True
        return False

    @staticmethod
    def __add_user(login: str, password: str) -> bool:
        """
        Добавление нового пользователя в БД

        :param login: login пользователя
        :param password: password пользователя
        :return: True если пользователь добавлен в БД, иначе - False
        """

        password = hashlib.sha256(password.encode()).hexdigest()
        users_crud.add_user(login, password)

        return True

    def registration(self) -> bool:
        """
        Регистрация пользователя

        :return: True - регистрация успешна, иначе False
        """

        while True:
            login = input("Введите ваш логин: ")

            if not self.__login_is_free(login):
                print("Такой логин уже существует, введите новый")
                continue
            break

        while True:
            password = input("Введите пароль: ")
            repeat_password = input("Повторите ввод пароля: ")
            if password != repeat_password:
                print("Введенные пароли не совпадают, повторите ввод")
                continue
            break

        return self.__add_user(login, password)


class AuthManager:

    def __init__(self) -> None:
        self.__user = None

    @property
    def user(self) -> typing.Union[User, None]:
        """
        Получение объекта типа User

        :return: User
        """

        return self.__user

    @staticmethod
    def __login_is_exists(login: str) -> bool:
        """
        Проверка существования логина в БД

        :param login: login пользователя
        :return:True - логин существует, иначе - False
        """

        if users_crud.login_is_exists(login):
            return True
        return False

    def authorization(self) -> bool:
        """
        Проверка пароля

        :return: True или False
        """

        login = input("Введите логин: ")

        if not self.__login_is_exists(login):

            while True:
                print("Пользователь не найден\n")
                user_choose = input(
                    "0 - регистрация\n1 - повторный ввод\n2 - выход2\nВвод: "
                )

                if user_choose not in ['0', '1', '2']:
                    print("Введено неверное значение")
                    continue

                if user_choose == '0':
                    raise RegistrationError
                elif user_choose == '1':

                    login = input("Введите логин: ")
                    if not self.__login_is_exists(login):
                        continue
                    break

                elif user_choose == '2':
                    sys.exit()

        db_password = users_crud.get_password(login)
        password = input("Введите пароль: ")
        if db_password == hashlib.sha256(password.encode()).hexdigest():
            self.__user = User(login, password)
            return True
        else:
            return False


if __name__ == '__main__':
    auth_manager = AuthManager()
    print(auth_manager.authorization('user_1', '123456789q!'))

    # print(password)
    # print(password.password)
    # print(password.get())
    # print(password.check("g23SD45sa"))
    # print(password.check("GRz3988XV"))
    regist_manager = RegistrationManager()
    print(regist_manager.check_login_db('test_1', 33333))
    print(regist_manager.check_password_db('test_1', 33333))
