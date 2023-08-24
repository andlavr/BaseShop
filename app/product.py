from utils import counters
import typing

from utils.errors import ProductNameError, PriceError, RatingError


class Product:
    def __init__(self, name: str, price: typing.Union[float, int], rating: typing.Union[float, int]):

        if not isinstance(name, str):
            raise ProductNameError(f'Ожидается тип str, получен тип {type(name)}')

        self.__id = next(counters.IdCounter.generate_id())
        self.__name = name
        self.price = price
        self.rating = rating

    def __repr__(self):
        """
        Возврат строки при помощи которой был создан объект

        :return: строка для __repr__
        """

        return f"{self.__class__.__name__}(name={self.__name!r}, price={self.__price}, rating={self.__rating})"

    def __str__(self):
        """
        Возврат удобного для чтения варианта строки при помощи которой был создан объект

        :return: строка для __str__
        """

        return f"Наименование: {self.__name.ljust(50)} цена: {str(self.__price).ljust(15)} рейтинг: {str(self.__rating)}"

    @property
    def id_(self) -> str:
        """
        Получение id продукта

        :return: объект типа str
        """

        return self.__id

    @property
    def name(self) -> str:
        """
        Получение названия продукта

        :return: объект типа str
        """

        return self.__name

    @property
    def price(self) -> float:
        """
        Получение цены

        :return: Объект типа price
        """

        return self.__price

    @price.setter
    def price(self, price: typing.Union[float, int]) -> None:
        """
        Установка цены

        :param price:  int, float
        :return: Объект типа price
        """

        if price <= 0:
            raise ValueError('Ошибка - не верно указан  прайс (значение меньше нуля!)')

        if not isinstance(price, (float, int)):
            raise PriceError(f'Ожидается тип int, float, получен тип {type(price)}')

        self.__price = price

    @property
    def rating(self) -> typing.Union[float, int]:
        """
        Получение рейтинга

        :return: Объект типа rating
        """

        return self.__rating

    @rating.setter
    def rating(self, rating: typing.Union[float, int]) -> None:
        """
        Установка рейтинга

        :param rating: float, int
        :return: Объект типа rating
        """

        if rating <= 0:
            raise ValueError('Ошибка - не верно указан  рейтинг (значение меньше нуля!')

        if not isinstance(rating, (float, int)):
            raise RatingError('Ошибка - не верно указан  рейтинг (только цифры!)')

        self.__rating = rating


if __name__ == '__main__':
    item_product = Product(name='David', price=3.3, rating=9.8)
    print(item_product)
    print(repr(item_product))
