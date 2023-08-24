import psycopg2

from sqlalchemy import create_engine, Column, Integer, VARCHAR, String, DateTime, FLOAT, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from conf import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, URI

# Подключаюсь к БД
engine = create_engine(URI)

DeclarativeBase = declarative_base()


class Users(DeclarativeBase):
    """
    Класс Users для создания объектов типа user и добавления их в БД
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column('login', String)
    password = Column('password', String)

    def __repr__(self):
        return f"id={self.id}, login={self.login}, password={self.password}"


class Category(DeclarativeBase):
    """
    Класс Category для создания объектов типа category и добавления их в БД
    """

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)

    def __repr__(self):
        return f"id={self.id}, name={self.name}"


class Product(DeclarativeBase):
    """
    Класс Product для создания объектов типа product и добавления их в БД
    """

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    price = Column('price', FLOAT)
    rating = Column('rating', FLOAT)

    def __repr__(self):
        return f"id={self.id}, name={self.name}, price={self.price}, rating={self.rating}"


class CategoryProducts(DeclarativeBase):
    """
    Класс CategoryProducts для создания объектов типа category_id, product_id и добавления их в БД
    """

    __tablename__ = 'category_products'
    __table_args__ = (
        PrimaryKeyConstraint('category_id', 'product_id'),
    )

    category_id = Column(Integer, ForeignKey('category.id'))

    product_id = Column(Integer, ForeignKey('product.id'))


DeclarativeBase.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


if __name__ == '__main__':
    pass
