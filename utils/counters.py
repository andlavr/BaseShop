import uuid


class IdCounter:

    @staticmethod
    def generate_id() -> str:
        """
        Генерация id продукта

        :return: Объект типа id
        """

        while True:
            yield uuid.uuid4()



class UserIdCounter:

    @staticmethod
    def user_id_generator():
        """
        Генерация id пользователя

        :return: Объект типа id
        """

        while True:
            yield uuid.uuid4()


if __name__ == '__main__':
    print(next(IdCounter.generate_id()))



