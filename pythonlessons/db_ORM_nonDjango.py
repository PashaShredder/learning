"""ORM  позволяет соиденить классы python
и таблицы SQL(грубоговоря)"""

# from sqlalchemy import create_engine
# from sqlalchemy import Table, Column, Integer, String, MetaData
# from sqlalchemy.orm import mapper
#
# engine = create_engine('sqlite:///test.db', echo=True)
# metadata = MetaData()# каталог с таблицами
# users_table = Table('user', metadata, # users_table - создание таблицы
#                     Column('id', integer, primary_key=True),
#                     Column('firstname', String),
#                     Column('lastname', String)
#                     )
# metadata.create_all(engine)
# class User:
#     def __init__(self,firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     mapper(User,users_table)
#     user = User('Pavel','Shredder')


"""!!!метод declarative_base!!!"""

# from sqlalchemy import create_engine
# from sqlalchemy import  Column, Integer, String
# from sqlalchemy.ext declarative import declarative_base
#
# engine = create_engine('sqlite:///test.db', echo=True)
# Base = declarative_base()
# class Person(Base):
#     __tablename__='person'
#     id = Column(Integer, primary_key=True)
#     firstname = Column(String)
#     lastname = Column(String)
#
#     def __init__(self,firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
# Base.metadata.create_all(engine)