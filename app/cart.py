import collections
import typing

from app.product import Product
from utils.errors import ProductsListTypeError, ProductTypeError


class Cart:

    def __init__(self, products: typing.Optional[typing.List[Product]] = None):
        if products is not None:
            self.products = products
        else:
            self.products = []

    def __str__(self) -> str:
        """
        Возвращает читаемый вариант корзины

        :return: строка для __str__
        """

        return f"Ваша корзина: {[f'{item.name}: {item.price} у.е.' for item in self.__products]}"

    def __repr__(self) -> str:
        """
        Возвращает строку с помощью которой был создан объект

        :return: строка для __repr__
        """

        return f'{self.__class__.__name__}(products={self.__products})'

    @property
    def products(self) -> typing.List[Product]:
        """
        Получение списка продуктов

        :return: список объектов типа Product
        """

        return self.__products

    @products.setter
    def products(self, value: typing.List[Product]) -> None:
        """
        Установка списка продуктов

        :param value: список объектов типа Product
        :return: None
        """

        if not isinstance(value, list):
            raise ProductsListTypeError(f'Ожидается тип list, получен тип {type(value)}')

        for product in value:
            if not isinstance(product, Product):
                raise ProductsListTypeError(f'Ожидается тип Product, получен тип {type(product)}')

        self.__products = value

    def add_product(self, product: Product) -> None:
        """
        Добавление продукта в корзину

        :param product: объект типа Product
        :return: None
        """

        if not isinstance(product, Product):
            raise ProductTypeError(f'Ожидается тип Product, получен тип {type(product)}')

        self.__products.append(product)

    def del_product(self, product: Product) -> None:
        """
        Удаление продукта из корзины

        :param product: объект типа Product
        :return: None
        """

        if not isinstance(product, Product):
            raise ProductTypeError(f'Ожидается тип Product, получен тип {type(product)}')

        self.__products.remove(product)

    def show(self) -> None:
        """
        Красивый вывод корзины

        :return: None
        """

        cart_count = collections.Counter([product.name for product in self.products])
        result = []

        for product in self.products:
            if product.name not in result:
                print(
                    f"Наименование: {product.name.ljust(50)} "
                    f"цена за ед.: {str(product.price).ljust(15)} "
                    f"количество: {str(cart_count[product.name]).ljust(10)} "
                    f"общая стоимость: {str(product.price * cart_count[product.name]).ljust(20)} "
                    f"рейтинг: {str(product.rating)}")
                result.append(product.name)

        sum_price = sum([product.price for product in self.__products])
        print('_' * 180)
        print('Общая сумма покупок:'.ljust(133), sum_price, 'у.е.')
        print('_' * 180)


if __name__ == '__main__':

    item_product = Product(name='TV Gorizont', price=3000, rating=9.8)
    item_product_2 = Product(name='Computer', price=300000, rating=10)
    item_product_3 = Product(name='Картошка', price=60, rating=2.8)
    item_product_4 = Product(name='Картошка', price=60, rating=2.8)
    item_product_5 = Product(name='Картошка', price=60, rating=2.8)
    item_product_6 = Product(name='Картошка', price=60, rating=2.8)

    products = [item_product, item_product_2, item_product_3, item_product_4, item_product_5, item_product_6]
    cart_2 = Cart(products)
    cart_2.show()
