import random
import secrets
import string
import typing

from faker import Faker

from app.product import Product


class BaseGenerator:
    def __init__(self):
        self.base = []

        self.faker = Faker("RU_ru")

    def get_product(self, min_price, max_price) -> typing.Union[Product, None]:
        """
        Генерация объекта типа Product

        :param min_price: int
        :param max_price: int
        :return: объект типа Product
        """

        if not self.base:
            return None

        name = f"{random.choice(self.base).title()} '{self.faker.word().title()}'"
        return Product(name, random.randint(min_price, max_price), round(random.uniform(0, 5), 2))

    def get_products(self, min_price, max_price, count) -> typing.List[Product]:
        """
        Генерация списка продуктов

        :param min_price: int
        :param max_price: int
        :param count: int
        :return: список объектов типа List[Product]
        """

        if not self.base:
            return []

        return [self.get_product(min_price, max_price) for _ in range(count)]


class Meat(BaseGenerator):
    def __init__(self):
        super().__init__()

        self.base = [
            'говядина', 'телятина', 'свинина', 'баранина', 'конина', 'дичь', 'субпродукты'
        ]


class AnimalParts(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.base = [
            'печень', 'языки', 'почки', 'мозги', 'сердце', 'диафрагма', 'мясокостный хвост', 'головы',
            'вымя говяжье', 'рубец с сеткой говяжий', 'калтык', 'легкие', 'ноги свиные', 'путовый состав говяжий',
            'уши говяжьи и свиные', 'губы говяжьи', 'мясная обрезь', 'щековина свиная'
        ]


class Sausage(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.base = [
            'колбасы (колбаски)', 'сосиски', 'сардельки', 'шпикачки', 'варено- копченые сосиски',
            'полукопченые сосиски', 'сырокопченые сосиски', 'сыровяленая колбаса', 'колбаса фаршированная', 'ливерная',
            'кровяная', 'паштет', 'холодец', 'студень', 'зельцы', 'сальтисоны'
        ]


class SmokedMeats(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.base = [
            'окорока', 'лопатки, рулеты', 'ветчина', 'балык', 'бекон', 'грудинка', 'корейка', 'филей',
            'буженина', 'карбонат', 'шейка', 'языки', 'свиные ребра копченые',
            'прессованное мясо свиных голов'
        ]


class Preserves(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.base = [
            'тушеная говядина', 'тушеная телятина', 'тушеная свинина', 'тушеная баранина',
            'тушеная конина', ' мясо кролика'
        ]


class MincedMeat(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.base = ['завтрак туриста', 'фарш сосисочный', 'фарш колбасный', 'мясо рубленное (в желе)']


class Password:

    @staticmethod
    def generate_password() -> str:
        """
        Генерация пароля

        :param self: str

        :return: Объект типа str
        """

        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8, 15))
        return password


if __name__ == '__main__':
    # print(BaseGenerator().get_product(1, 12))
    # print(BaseGenerator().get_products(1, 12, 10))

    print(Meat().get_product(1, 12))
    print(Meat().get_products(1, 12, 10))
    #
    # print(AnimalParts().get_product(1, 20))
    # print(AnimalParts().get_products(1, 20, 10))
    #
    # print(SausageProducts().get_product(1, 14))
    # print(SausageProducts().get_products(1, 24, 12))
    #
    # print(SmokedMeats().get_product(1, 30))
    # print(SmokedMeats().get_products(1, 31, 9))
    #
    # print(Preserves().get_product(1, 42))
    # print(Preserves().get_products(1, 56, 8))
    #
    # print(MincedMeat().get_product(1, 7))
    # print(MincedMeat().get_products(1, 53, 22))

    # full_list_products = [meat_list, animal_parts_list, sausage_products, smoked_meants, preserves, minced_meat]

    # def good_generator():
    #     """
    #     Генерирует товар из списков
    #
    #     :return: Объект типа str
    #     """
    #     for product_ in full_list_products:
    #         for i in product_:
    #             while True:
    #                 yield i
    #

    # def kopeck_generator():
    #     """
    #     Генерирует копейки
    #
    #     :return: Объект типа float
    #     """
    #
    #     for kopeck in [round(random.random(), 2)]:
    #
    #         while True:
    #             yield kopeck
    #
    #
    # def rubbles_generator():
    #     """
    #     Генерирует целое число
    #
    #     :return: Объект типа int
    #     """
    #
    #     for rub in [random.randint(10, 2000)]:
    #         while True:
    #             yield rub
    #
    #
    #
    # def cost_():
    #     res = 0
    #     a = yield from rubbles_generator()
    #     b = yield from kopeck_generator()
    #     return res == str(f"{a} + {b}")
    #
    #
    #
    #
    #
    # if __name__ == '__main__':
    #     test_good_gen = good_generator()
    #     print(next(test_good_gen))
    #
    #     test_kopeck = kopeck_generator()
    #     print(next(test_kopeck))
    #
    #     test_rub = rubbles_generator()
    #     print((next(test_rub)))
    #
    #     test_costs = cost_()
    #     print(next(cost_()))
    #
    #
    #
    #
    #
