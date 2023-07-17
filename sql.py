import pathlib
import sqlite3

DB_NAME: str = 'db.sqlite'

# Краткая шпаргалка, команды по порядку.
"""
SELECT ('столбцы (* - для выбора всех столбцов)')
       (могут применяться агрегатные функции COUNT, MIN, MAX, AVG и SUM)
       (и ключевое слово DISTINCT)
FROM ('таблица')
JOIN ('таблица') ON ('условие/фильтрация')
WHERE ('условие/фильтрация')
GROUP BY ('столбец, по которому нужно сгруппировать данные')
HAVING ('условие/фильтрация на уровне сгруппированных данных')
ORDER BY ('столбец, по которому нужно ранжировать вывод')
LIMIT ('сколько записей показывать')
OFFSET ('сколько записей в выборке пропустить')
"""

# Шпаргалка по JOIN
"""
INNER JOIN / JOIN - возвращает записи, отфильтрованные в ON.
    SELECT movies.name,
           slogans.name,
           types.name
    FROM movies
    JOIN slogans ON movies.slogan_id = slogans.id
    JOIN types ON movies.type_id = types.id; 

LEFT OUTER JOIN - возвращает все записи таблицы в FROM и отфильтрованные для других.
    SELECT movies.name,
           slogans.name
    FROM movies
    LEFT JOIN slogans ON movies.slogan_id = slogans.id; 

RIGHT OUTER JOIN - возвращает отфильтрованные записи таблицы в FROM и все для других.

FULL OUTER JOIN - возвращает все записи всех таблиц, несоответствующие значения
                  в ON в таблицах заменяются на NULL
    SELECT movies.name,
           slogans.name
    FROM movies
    FULL JOIN slogans ON movies.slogan_id = slogans.id;
        или
    SELECT movies.name,
           slogans.name
    FROM movies
    LEFT JOIN slogans ON movies.slogan_id = slogans.id
    UNION
    SELECT movies.name,
        slogans.name
    FROM slogans
    LEFT JOIN movies ON movies.slogan_id = slogans.id;

CROSS JOIN - возвращает декартовое произведение
    SELECT movies.name,
           slogans.name
    FROM movies
    CROSS JOIN slogans; 
"""

# Шпаргалки по изменению таблиц.
"""
Переименование таблицы
    ALTER TABLE <имя таблицы> RENAME TO <новое имя таблицы>; 

Добавление колонки
    ADD COLUMN <имя колонки> <тип колонки>;

Переименование колонки
    ALTER TABLE <название таблицы>
    RENAME COLUMN <старое имя колонки> TO <новое имя колонки>;

Удаление колонки
    ALTER TABLE <название таблицы>
    DROP COLUMN <имя колонки>; 

Удаление таблиц
    DROP TABLE <имя таблицы>;
"""

# Если в текущей директории не будет файла DB - он будет создан.
# con = connection
con = sqlite3.connect(DB_NAME)

# Необходимо создать курсор для выполнения команд SQL и получения результатов.
# cur = cursor
cur = con.cursor()

# Выполнение команд выполняется согласно код-стайлу SQL.
cur.execute('''
    CREATE TABLE IF NOT EXISTS directors(
        id INTEGER PRIMARY KEY,
        name TEXT,
        birthday_year INTEGER
    );
''')
cur.execute('''
    CREATE TABLE IF NOT EXISTS types(
        id INTEGER PRIMARY KEY,
        name TEXT
    );
''')
cur.execute('''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        type_id INTEGER NOT NULL,
        release_year INTEGER,
        director_id INTEGER NOT NULL,
        FOREIGN KEY(type_id) REFERENCES types(id),
        FOREIGN KEY(director_id) REFERENCES directors(id)
    );
''')

# Можно объединять команды в одну.
cur.executescript('''
    CREATE TABLE IF NOT EXISTS directors(
        id INTEGER PRIMARY KEY,
        name TEXT,
        birthday_year INTEGER
    );
    CREATE TABLE IF NOT EXISTS types(
        id INTEGER PRIMARY KEY,
        name TEXT
    );
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        type_id INTEGER NOT NULL,
        release_year INTEGER,
        director_id INTEGER NOT NULL,
        FOREIGN KEY(type_id) REFERENCES types(id),
        FOREIGN KEY(director_id) REFERENCES directors(id)
    );
''')

# Проверить существование таблиц можно, обратившись к таблице-мастеру.
# res = result
res = cur.execute("""
    SELECT name
    FROM sqlite_master;
""")
# Третья таблица - автоматически созданный индекс для отслеживания UNIQUE.
# Номер в конце не привязывается к номеру поля, а представляет собой просто
# порядковое число.
assert res.fetchall() == [('directors',), ('types',), ('movies',), ('sqlite_autoindex_movies_1',)]

# Вставка данных осуществляется двумя методами. В стиле SQL или кортежем.
cur.execute("""
    INSERT INTO directors(id, name, birthday_year)
    VALUES (1, 'Брайан Тейлор', NULL);
""")
cur.execute("""
    INSERT INTO directors(id, name, birthday_year)
    VALUES (2, 'Джон Мактирнан', 1951);
""")
cur.execute("""
    INSERT INTO directors
    VALUES(?,?,?);""",
    (3, 'Какой-то режисер', 2000))

# При использовании кортежей становится возможной вставка множества данных.
# В поле ID ничего передано не будет, БД сама поставит значение.
types = [
    ('Боевик',),
    ('Комедия',)]
movies = [
    ('Крепкий орешек', 1, 1988, 2),
    ('Адреналин', 1, 2006, 1),
    ('Один дома', 2, 1990, 3),
    ('Каникулы строго режима', 2, 2009, 3)]
cur.executemany("""
    INSERT INTO types
    VALUES(NULL, ?);""",
    types)
cur.executemany("""
    INSERT INTO movies
    VALUES(NULL, ?, ?, ?, ?);""",
    movies)

# Для выполнения команд INSERT необходимо создать коммит в БД.
# Создание таблиц коммитов не требует.
con.commit()

# Получение данных из таблицы.
# https://www.sqlite.org/lang.html
cur.execute("""
    SELECT name,
           release_year
    FROM movies
    WHERE
        release_year > 2000
        OR release_year = 1990
        OR NOT release_year BETWEEN 1999 AND 2000
        AND release_year <> 1988
        OR name IN ('Адреналин', 'Каникулы строго режима')
    ORDER BY name, release_year DESC
    LIMIT 5
    OFFSET 0;
""")
result_list: list = []
for result in cur:
    result_list.append(result)
assert result_list == [
    ('Адреналин', 2006),
    ('Каникулы строго режима', 2009),
    ('Один дома', 1990),]

# Получение уникальных данных из таблиц.
cur.execute("""
    SELECT DISTINCT type_id
    FROM movies;
""")
result_list: list = []
for result in cur:
    result_list.append(result)
assert result_list == [
    (1,),
    (2,)]

# Использование агрегирующих функций.
# COUNT - посчитать количество объектов выборке
# MAX/MIN - найти максимальное/минимальное значение (игнорируют Null)
# AVG/SUM - привести среднее/суммарное значение (игнорируют Null)
cur.execute("""
    SELECT COUNT(*)
    FROM movies
    WHERE release_year > 1900;
""")
result_list: list = []
for result in cur:
    result_list.append(result)
assert result_list == [(4,)]

# Использование группировки и фильтрации.
# При группировки из всего множества допустимых записей будет выбрана лишь 1.
cur.execute("""
    SELECT type_id, AVG(release_year)
    FROM movies
    GROUP BY type_id
    HAVING release_year IS NOT NULL
""")
result_list: list = []
for result in cur:
    result_list.append(result)
assert result_list == [(1, 1997.0), (2, 1999.5)]

# Получение значений по FK из таблиц.
cur.execute("""
    SELECT movies.name,
           directors.name
    FROM movies,
         directors
    WHERE movies.director_id = directors.id
""")
result_list: list = []
for result in cur:
    result_list.append(result)
assert result_list == [
    ('Крепкий орешек', 'Джон Мактирнан'),
    ('Адреналин', 'Брайан Тейлор'),
    ('Один дома', 'Какой-то режисер'),
    ('Каникулы строго режима', 'Какой-то режисер')]

# По стандарту SQL92 принято разделять соединение таблиц в выборку (FROM)
# и фильтрацию (WHERE) при помощи оператора JOIN.
# Оператор пересечения INNER JOIN допускается указывать как просто JOIN.
cur.execute("""
    SELECT movies.name,
           directors.name
    FROM movies
    JOIN directors ON movies.director_id = directors.id
""")
result_list: list = []
for result in cur:
    result_list.append(result)
assert result_list == [
    ('Крепкий орешек', 'Джон Мактирнан'),
    ('Адреналин', 'Брайан Тейлор'),
    ('Один дома', 'Какой-то режисер'),
    ('Каникулы строго режима', 'Какой-то режисер')]

# В целях безопасности, что все операции с БД будут успешно завершены,
# перед выходом необходимо завершить соединение с БД.
con.close()

input('Для удаления БД нажмите "Enter", или закройте консоль для отмены.')
try:
    pathlib.Path(DB_NAME).unlink()
except Exception as err:
    print(f"Ошибка при удалении файла: {err}")

"""
Резидентные базы данных / Базы данных реального времени (RTDB).
Базы данных, которые хранятся в оперативной памяти компьютера.
Требуются там, где есть потребность в быстрой обработке больших объемов данных:
- тестирование кода
- мониторинг мед.оборудования
- аналитика/торги в режиме реального времени
- машинное обучение
- потоковая передача данных с датчиков
- и т.д.
"""

con_res = sqlite3.connect(':memory:')

con_res.close()
