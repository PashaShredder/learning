"""библиотека для работы с базами данных"""
# pip install sqlalchemy
#  Транзакция
# from sqlalchemy import create_engine
#
# engine = create_engine("sqlite:///test.db")
# conn = engine.connect()
# trans = conn.begin()
# conn.execute(
#     "insert into user (firstname, lastname) values (:firstname,:lastname)", firstname = 'Pasha', lastname='Shredder')
# trans.commit()# .commit - применение транзакции .rollback -отмена транзакции
# conn.close()
"""Сеанс для работы с базой данных"""
# Сессия
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bing = engine)
# session = Session()
# session.add(Person('Pavel','Shredder'))
# session.add_all([Person('Pavel','Shredder'), Person('Pavel','Pavlovich')])
# session.commit()
"""библотека для работы с ORM"""
# from peewee import *

""" создание Query запросов"""
# person = session.query(Person).filter_by(firstname='Pavel').first()
# person = session.query(Person).filter(Person.firstname == 'Pavel').first()
#
# person = session.query(Person).filter(and_(
#     Person.firstname =='Pavel',
#     Person.lastname =='Pavlovich',
#     )).all()
"""создание таблицы"""

# CREATE TABLE person (
#     id SERIAL PRIMARY KEY,
#     firstname varchar,
#     lastname varchar
# );
"""удаление таблицы"""
# DROP TABLE person;
# DROP COLUMN email -- #не работает для sqlite

"""изменение таблицы"""
# ALTER TABLE person
# ADD COLUMN email varchar(255);

"""Добавление данных в таблицу"""
# INSERT INTO person(id, firstname, lastname, email) VALUES (0, 'Pavel','Shredder','admin@gmail.com')

"""Выборка данных"""

# SELECT * FROM person;
# SELECT id FROM person;
# SELECT firstname, lastname FROM person;
# SELECT * FROM person WHERE firstname = 'Pavel'; # выборка с условием
# SELECT * FROM person WHERE firstname like '$avel$'; # выборка всех записей по указанному совпадению
#

"""Обновление данных"""
# UPDATE person SET firstname = 'Pavel' WHERE firstname = 'Pasha'
"""Удаление данных """
# DELETE FROM person WHERE firstname = 'Pavel;

