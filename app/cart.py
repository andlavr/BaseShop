from app.product import Product
import typing

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
        for product in self.products:
            print(product)

        sum_price = sum([product.price for product in self.__products])
        print('_____________________________________________________________________________________________________')
        print('Общая сумма покупок:'.ljust(70), sum_price, 'у.е.')
        print('_____________________________________________________________________________________________________')

        # print('Наименование', products.name)


if __name__ == '__main__':
    cart = Cart()

    # print(cart)
    #
    item_product = Product(name='TV Gorizont', price=3000, rating=9.8)
    # print(item_product)
    item_product_2 = Product(name='Computer', price=300000, rating=10)
    # print(item_product_2)
    item_product_3 = Product(name='Картошка', price=60, rating=2.8)
    # print(item_product_3)

    products = [item_product, item_product_2, item_product_3]
    cart_2 = Cart(products)
    cart_2.show()
    #
    # cart.add_product(item_product)
    # print(cart)
    # print(cart.products)
    # cart.add_product(item_product_2)
    # print(cart)
    # print(cart.products)
    # cart.add_product(item_product_3)
    # print(cart)
    # print(cart.products)
    #
    # dell_potato = cart.del_product(item_product_3)
    # print('Картошка удалена', dell_potato)

    # def check_and_add_product_in_cart(self, products_list, product):
    #     count = 0
    #
    #     if len(self.products_list) > 0:
    #         for product in self.products_list:
    #             if (product in self.products_list):
    #                 count += 1

    # def add_product_to_cart(self, product, products_list):
    #     self.products_list = []
    #     count = 0
    #     for product in self.products_list:
    #         # if len(products_list) == 0:
    #         products_list.append(product)

    # Думал о том если корзина уже не пустая, потом понял, что это не имеет значение т.к. потом просто посчитаем количество одинаковых элементов в списке
    # if len(self.products_list) > 0:
    #     for product in self.products_list:
    #         if (product in self.products_list):
    #             count += 1
    #             products_list.ap

    # elif product in self.products_list:
    #     self.products_list[product] + product

#
#     def dell_product_from_cart(self, product):
#          pass
#
# if __name__ == '__main__':
#     Cart.add_product_to_cart()
