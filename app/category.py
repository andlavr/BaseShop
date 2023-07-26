import typing

from app.product import Product
from utils.errors import ProductError, ProductsListTypeError


class Category:
    def __init__(self, name, products: typing.Union[Product, None] = None):
        self.__name = name

        if products is not None:
            self.__products = products
        else:
            self.__products = []

    @property
    def name(self):
        return self.__name

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):

        if not isinstance(value, list):
            raise ProductsListTypeError(f'Ожидается тип list, получен тип {type(value)}')

        for product in value:
            if not isinstance(product, Product):
                raise ProductsListTypeError(f'Ожидается тип Product, получен тип {type(product)}')

        return self.__products == value

    def add_product(self, product: Product) -> None:
        """
        Добавление объекта типа product в список продуктов

        :param product: str
        :return: None
        """

        if not isinstance(product, Product):
            raise ProductError(f'Ожидается тип Product, получен тип {type(product)}')

        self.__products.append(product)

    def del_product(self, product: Product) -> None:
        """
        Удаление объекта типа product из списка продуктов

        :param product:  str
        :return: None
        """

        if not isinstance(product, Product):
            raise ProductError(f"Ожидается тип Product, получен тип {type(product)}")

        self.__products.remove(product)


if __name__ == '__main__':
    from utils import generators

    cat_1 = Category("Сосиски", generators.Sausage().get_products(100, 500, 20))

    # for elem in generators.Sausage().get_products(100, 500, 20):
    #     cat_1.add_product(elem)

    print(cat_1.products)
