from app.category import Category
from app.cms import category_manager
from app.product import Product
from app.user import User
from utils.auth import AuthManager
from utils.errors import WrongLogin, ShopNameError, RegistrationError


class Shop:
    def __init__(self, name: str):
        self.name = name
        self.__user = None

        self.__categories = self.__init_categories()

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

    def __init_categories(
            self) -> list:  # В идеале создавать продукты и категории не в самом магазине, а в отдельном классе получая из БД
        return category_manager.categories

    def __enter_to_web(self) -> str:
        """
        Формализованное приветствие

        :return: str
        """
        return f"Добро пожаловать в магазин '{self.name}'!"

    def __authentification_user(self) -> None:
        """
        Аутентификация пользователя

        :return: None
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

    def __choose_categories(self) -> Category:
        """
        Выбор категории продукта

        :return: Объект типа Category
        """

        while True:
            for index, category in enumerate(self.__categories, 1):
                print(index, category.name)

            try:
                user_choose = int(input("Выберете номер интересующей вас категории товара от 1 до 8 ")) - 1
            except ValueError:
                print("Введено не верное значение, выберите нужное из списка")
                continue

            print('Если вы зашли в неверную категорию то нажмите 11')
            if user_choose == 11:
                print(index, category.name)

            if user_choose in range(len(self.__categories)):
                return self.__categories[user_choose]

            print("Введено не верное значение, выберите нужное из списка")

    # def wrong_category(self, user_choose) -> Category:
    #
    #     if user_choose == 0:
    #         print()

    def __choose_product(self, category: Category) -> Product:
        """
        Выбор продукта в категории

        :param category: объект типа Category
        :return: Объект типа Product
        """

        while True:
            for index, product in enumerate(category.products, 1):
                print(index, product)

            try:
                user_choose = int(input("Выберете номер интересующего вас продукта: ")) - 1
            except ValueError:
                print("Введено не верное значение, выберете нужное из списка")
                continue

            if user_choose in range(len(category.products)):
                return category.products[user_choose]

            print("Введено не верное значение, выберите нужное из списка")

    def __show_cart(self):
        pass

    def __buy_products(self):
        pass

    def run(self):
        self.__enter_to_web()
        self.__authentification_user()

        while True:
            category = self.__choose_categories()
            product = self.__choose_product(category)
            self.user.cart.add_product(product)

    #TODO: 1. Предусмотреть возврат из категории если зашли не правильно
    #TODO: 2. Возврат из продуктов, если зашел не правильно
    #TODO: 3. Красивый вывод продуктов
    #TODO: 4. Красивый вывод корзины
    #TODO: 5. Возможность выбора количества продукта (шт)

            print("Ваша корзина:")
            print(self.user.cart.products)

            # if self.user is None:
            #     print("12312312")

            input("12312")
            print("Магазин запущен")
