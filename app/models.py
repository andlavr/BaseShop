import psycopg2
from psycopg2 import connection

from conf import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

# db = {
#     "users": {
#         "user_1": "c209488a83c3f517aec78a832b021dc3fa23f099d3783e09eaa2ff62ff90d78c",  # 123456789q!
#         "user_2": "e468983ee01e0a197aed4d8c98a56cd119cc59258dda7c49e488148facce2c1b",  # !q987654321
#         # "tester":
#     }
# }


class ConnectorDB:
    def __init__(self, db_name, db_user, db_password, db_host):
        self.__db_name = db_name
        self.__db_user = db_user
        self.__db_password = db_password
        self.__db_host = db_host

        self.__connection = psycopg2.connect(
            f"dbname={self.__db_name} user={self.__db_user} password={self.__db_password} host={self.__db_host}"
        )

    @property
    def db_name(self) -> str:
        """
        Получение названия БД

        :return: название БД
        """
        return self.__db_name

    @property
    def db_user(self) -> str:
        """
        Получение имени пользователя

        :return: имя пользователя
        """
        return self.__db_user

    @property
    def db_password(self) -> str:
        """
        Получение пароля пользователя

        :return: пароль пользователя
        """
        return self.__db_password

    @property
    def db_host(self):
        """
        Получение адреса хоста

        :return: адрес хоста
        """
        return self.__db_host

    @property
    def connection(self) -> connection:
        """
        Получение доступа к подключению

        :return: объект типа connection
        """
        return self.__connection

if __name__ == '__main__':
    test_connection = ConnectorDB(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)
