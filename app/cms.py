import time
import typing

from app.category import Category
from app.product import Product
from utils.errors import CategoryTypeError, ProductTypeError

import utils.generators as gen


class CategoryManager:
    def __init__(self, categories: typing.Union[typing.List[Category], None] = None):

        if categories is None:
            self.__categories = []
        else:
            if not isinstance(categories, list):
                raise CategoryTypeError(f"Ожидается тип list, передан {type(categories)}!")

            for category in categories:
                self.check_category(category)

            self.__categories = categories

        self.__available_products_type = {
            "Мясо": gen.Meat().get_products,
            "Части животных": gen.AnimalParts().get_products,
            "Колбасные изделия": gen.Sausage().get_products,
            "Копчености": gen.SmokedMeats().get_products,
            "Консервы": gen.Preserves().get_products,
            "Фарш": gen.MincedMeat().get_products
        }




    @property
    def categories(self):
        return self.__categories

    def add_category(self, category: Category) -> None:
        """
        Добавление объекта категория в список

        :param category: str
        :return: None
        """

        self.check_category(category)

        self.__categories.append(category)


    def create_category(self, name, products_type, count):
        if not isinstance(name, str):
            raise TypeError(f'Ожидается тип str, получен {type(name)}')

        if not isinstance(products_type, str):
            raise TypeError(f'Ожидается тип str, получен {type(products_type)}')

        if not isinstance(count, int):
            raise TypeError(f'Ожидается тип str, получен {type(count)}')

        if products_type not in self.__available_products_type.keys():
            raise ProductTypeError(
                f"Поддерживаются следующие типы продуктов: {list(self.__available_products_type.keys())}")

        category = Category(name, self.__available_products_type[products_type](100, 2000, count))

        self.add_category(category)

    def check_category(self, category):
        if not isinstance(category, Category):
            raise CategoryTypeError(f"Ожидается тип Category, передан {type(category)}!")


    def del_category(self, name):
        for index, category in enumerate(self.__categories):
            if category.name == name:
                self.__categories.remove(category)
                return True
        # return False
        raise ValueError("Такой категории нет")

    def del_product_from_category(self, category_name, product_name):
        for category in self.__categories:
            if category.name == category_name:
                for product in category.products:
                    if product.name == product_name:
                        category.del_product(product)


print(f"{time.ctime()}: Инициализация категорий")
category_manager = CategoryManager()
category_manager.create_category("Мясо свежее", "Мясо", 20)
category_manager.create_category("Мясо замороженное", "Мясо", 20)
category_manager.create_category("Субпродукты", "Части животных", 20)
category_manager.create_category("Колбасы копченые", "Колбасные изделия", 20)
category_manager.create_category("Колбасы сыровяленые", "Колбасные изделия", 20)
category_manager.create_category("Копчености", "Копчености", 20)
category_manager.create_category("Консервы", "Консервы", 20)
category_manager.create_category("Фарш", "Фарш", 20)

print(f"{time.ctime()}: Категории инициализированы")
