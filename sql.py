import pathlib
import sqlite3

DB_NAME: str = 'db.sqlite'

# Краткая шпаргалка, команды по порядку
"""
SELECT ('столбцы (* - для выбора всех столбцов)')
       (могут применяться агрегатные функции COUNT, MIN, MAX, AVG и SUM)
       (и ключевое слово DISTINCT)
FROM ('таблица')
WHERE ('условие/фильтрация')
GROUP BY ('столбец, по которому нужно сгруппировать данные')
HAVING ('условие/фильтрация на уровне сгруппированных данных')
ORDER BY ('столбец, по которому нужно ранжировать вывод')
LIMIT ('сколько записей показывать')
OFFSET ('сколько записей в выборке пропустить')
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
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name TEXT,
        type TEXT,
        release_year INTEGER
    );
''')

# Можно объединять команды в одну.
cur.executescript('''
    CREATE TABLE IF NOT EXISTS directors(
        id INTEGER PRIMARY KEY,
        name TEXT,
        birthday_year INTEGER
    );

    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name TEXT,
        type TEXT,
        release_year INTEGER
    );
''')

# Проверить существование таблиц можно, обратившись к таблице-мастеру.
# res = result
res = cur.execute("""
    SELECT name
    FROM sqlite_master;
""")
assert res.fetchall() == [('directors',), ('movies',)]

# Вставка данных осуществляется двумя методами. В стиле SQL или кортежем.
cur.execute("""
    INSERT INTO movies(id, name, type, release_year)
    VALUES (1, 'Крепкий орешек', 'Боевик', 1988);
""")
cur.execute("""
    INSERT INTO movies
    VALUES(?,?,?,?);""",
    (2, 'Адреналин', 'Боевик', 2006))

# При использовании кортежей становится возможной вставка множества данных.
# В поле ID ничего передано не будет, БД сама поставит значение.
movies = [
    ('Один дома', 'Комедия', 1990),
    ('Каникулы строго режима', 'Комедия', 2009)]
cur.executemany("""
    INSERT INTO movies
    VALUES(NULL, ?, ?, ?);""",
    movies
)

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
        OR type LIKE 'Ко_е%'
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
    SELECT DISTINCT type
    FROM movies;
""")
result_list: list = []
for result in cur:
    result_list.append(result)
assert result_list == [
    ('Боевик',),
    ('Комедия',)]

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
    SELECT type, AVG(release_year)
    FROM movies
    GROUP BY type
    HAVING release_year IS NOT NULL
""")
result_list: list = []
for result in cur:
    result_list.append(result)
assert result_list == [('Боевик', 1997.0), ('Комедия', 1999.5)]

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
