"""Связь многие-к-одному(ForeignKey) sqlalchemy"""
#
# class Artist(Base):
#     __tablename__='artist'
#     id = Column(integer, primary_key=True)
#     name = Column(String)
#
# class Album(Base):
#     __tablename__ = 'album'
#     id = Column(String)
#     artist_id = Column(
#         Integer, ForeignKey('artist.id'), nullable = False)
#     artist = relationship(
#         'Artist', foreign_key = 'Album.artist_id', backref = 'albums')
#
#
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# artist = Artist(name='MyBand')
# album = Album(name='MyAlbum',artist=artist)
# session.add_all([artist,album])
# session.commit()
"""Many_to_one (ForeignKey) slq-запрос"""
# CREATE TABLE artist(
#     id INTEGER PRIMARY KEY,
#     name TEXT
# );
# CREATE TABLE album(
#     id INTEGER,
#     name TEXT,
#     artist_id INTEGER,
#     FOREIGN KEY (artist_id) REFERENCES artist(id)
# );
# # объединение таблиц artists + album
"""One_to_One (OneToOne) - дробление больших таблиц(моделей) на мелкие составляющие"""

# CREATE TABLE booklet(
#     id SERIALNOT NULL,
#     description VARCHAR,
#     album_id INTEGER NOT NULL,
#     PRIMARY KEY (album_id),
#     FOREIGN KEY (album_id) REFERENCES album (id)
# );

"""ManyToMany -- по сути реализация связи ForeignKey к третьей таблице
  в созданной промежуточной таблице связываем  две исходные
  (основная задача - связь множеств одних сущностей с множеством других)"""
#sql request

# CREATE TABLE track(
#     id SERIAL NOT NULL,
#     name VARCHAR,
#     duration FLOAT,
#     PRIMARY KEY (id)
# );
#
# CREATE TABLE association(
#     album_id INTEGER,
#     track_id INTEGER,
#     FOREIGN KEY(album_id) REFERENCES album (id),
#     FOREIGN KEY(track_id) REFERENCES track (id)
# )

"""!!!!JOIN - операция соединения, предназначена для обеспечения выборки
данных из двух и более таблиц и включения этих данных в один результирующий набор
по совпадающему условию. Существует только в реляционных БД(благодаря JOIN мощный функционал
позволяет вести хранение данных, а так же их простейший анализ с помощью запросов"""

# SELECT ИМЕНА_СТОЛБЦОВ(1..N)
#     FROM ИМЯ_ТАБЛИЦЫ_1 JOIN ИМЯ_ТАБЛИЦЫ_2
#         ON УСЛОВИЕ

"""INNER JOIN - внутреннее соединение - 
из 2х таблиц только то что пересекается
ТЗ - соединить 2 таблицы--в результирующей были поля Part,Cat,Price -- 
условие--совпадение номера категории(Catnumb) в таб. Categories и 
ссылки на категорию в таб. Parts"""

# SELECT Parts.Part, Categories.Cat_id AS Cat, Categories.Price
#     FROM Parts INNER JOIN Categories
#         ON Parts.Cat_id = Categories.Cat_id
"""LEFT OUTER JOIN - соединение табл. и вывода результирующей табл., в которой данну полностью пересекаются по условию,
указанному после ON - дополняется записями из первой по порядку (левой) табл. даже если они не соответствуют условию.
у записей левой табл, которые не соответствуют условию, значение столбца из правой будет NULL(неопределённым)
берёт из левой всё и все совпадения из правой, если не найдено то NULL"""

# SELECT Parts.Part, Categories.Cat_id AS Cat, Categories.Price
#     FROM Parts LEFT OUTER JOIN Categories
#         ON Parts.Cat_id = Categories.Cat_id
"""RIGHT OUTER JOIN аналог LEFT OUTER JOIN """
# SELECT Parts.Part, Categories.Cat_id AS Cat, Categories.Price
#     FROM Parts RIGHT OUTER JOIN Categories
#         ON Parts.Cat_id = Categories.Cat_id

"""FULL OUTER JOIN (полное внешнее соединение) все данные из левой и правой полностью пересекаются по 
указанному условию после ON, если не соответствует условию NULL"""

# SELECT Parts.Part, Categories.Cat_id AS Cat, Categories.Price
#     FROM Parts FULL OUTER JOIN Categories
#         ON Parts.Cat_id = Categories.Cat_id

"""Псевдоним для запросов"""

# SELECT P.Part, C.Cat_id AS Cat, C.Price
#     FROM Parts P INNER JOIN Categories C
#         ON P.Cat_id = C.Cat_id

"""Соединение более 2х таблиц"""

# SELECT ИМЕНА_СТОЛБЦОВ(1..N)
#     FROM ИМЯ_ТАБЛИЦЫ_1 JOIN ИМЯ_ТАБЛИЦЫ_2
#         ON УСЛОВИЕ
#         JOIN ИМЯ_ТАБЛИЦЫ_3
#             ON УСЛОВИЕ
#         ...
#         JOIN ИМЯ_ТАБЛИЦЫ_...N
#             ON УСЛОВИЕ

# SELECT C.Cat_name FROM Categories C JOIN Parts P
#     ON P.Cat_id=C.Cat_id JOIN ads A ON A.Part_id = P.Part_id
#     WHERE A.Date_end=CURDATE()

"""CROSS JOIN (перекрестное соединение) 
объединение каждой записи 1й табл с каждой 2й таблицы, 
и наоборот 2й к 1й
декартовое произведение"""

# SELECT(*)Categories CROSS JOIN Parts
# SELECT(*)Categories, Parts - #без явного указания CROSS JOIN
#
