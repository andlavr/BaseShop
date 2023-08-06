import sys

from app.category import Category
from app.cms import category_manager
from app.product import Product
from app.user import User
from utils.auth import AuthManager
from utils.errors import WrongLogin, ShopNameError, RegistrationError, WrongChooseCategory, WrongChooseProduct


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
        Установка названия магазина

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

    def __init_categories(self) -> list:  # В идеале создавать продукты и категории не в самом магазине, а в отдельном классе получая из БД
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

            if user_choose in range(len(self.__categories)):
                return self.__categories[user_choose]

            print("Введено не верное значение, выберите нужное из списка")


    def __choose_product(self, category: Category) -> Product:
        """
        Выбор продукта в категории

        :param category: объект типа Category
        :return: Объект типа Product
        """

        while True:
            for index, product in enumerate(category.products, 1):
                print(index, product)

            print("0 - назад (вернуться к выбору категории)")

            try:
                user_choose = int(input("Выберете номер интересующего вас продукта: ")) - 1
            except ValueError:
                print("Введено не верное значение, выберете нужное из списка")
                continue

            if user_choose == -1:
                raise WrongChooseCategory


            if user_choose in range(len(category.products)):
                try:
                    current_unit = int(input("Введите количество товара"))
                except ValueError:
                    print("Введено не верное значение, введите целое число!")
                    continue

                return category.products[user_choose], current_unit

            print("Введено не верное значение, выберите нужное из списка")

    def __show_cart(self) -> None:
        """
        Демонстрация корзины

        :return: None
        """

        print("Ваша корзина:")

        self.user.cart.show()


    def __buy_products(self) -> None:
        """
        Оплата продуктов в корзине

        :return:  None
        """
        print('Продукты оплачены')
        sys.exit(0)

    def run(self) -> None:
        """
        Основной метод для работы приложения

        :return: None
        """

        # TODO: 1. Предусмотреть возврат из категории если зашли не правильно  !OK
        # TODO: 2. Возврат из продуктов, если зашел не правильно  !OK
        # TODO: 3. Красивый вывод продуктов  !OK
        # TODO: 4. Красивый вывод корзины !OK
        # TODO: 5. Возможность выбора количества продукта (шт) !Ok

        self.__enter_to_web()
        self.__authentification_user()

        while True:

            category = self.__choose_categories()

            try:   # здесь try используется чтобы вернуться в категорию
                product, count = self.__choose_product(category)
                for i in range(count):
                    self.user.cart.add_product(product)
            except WrongChooseCategory:
                continue


            while True:
                print('Выберите дальнейшее действие:')
                print('1 - показать корзину')
                print('2 - продолжить покупки')
                print('3 - оплатить товары')

                try:
                    user_choose = int(input('Ваш выбор: '))
                except ValueError:
                    print("Выбрано не правильное действие!!!")
                    continue


                if user_choose == 1:
                    self.__show_cart()
                    break

                elif user_choose == 2:
                    break

                elif user_choose == 3:
                    self.__buy_products()
                    break
                else:
                    print("Выбрано не правильное действие!!!")
                    continue

