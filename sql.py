import pathlib
import sqlite3

DB_NAME: str = 'db.sqlite'

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

# В целях безопасности, что все операции с БД будут успешно завершены,
# необходимо завершить соединение с БД.
con.close()

input('Для удаления БД нажмите "Enter", или закройте консоль для отмены.')
pathlib.Path(DB_NAME).unlink()

"""
Резидентные базы данных / Базы данных реального времени (RTDB).
Базы данных, которые хранятся в оперативной памяти компьютера.
Требуются там, где есть потребность в быстрой обработке больших объемов данных:
- тестирование кода
- мониторинг мед.оборудования
- аналитика в режиме реального времени
- машинное обучение
- потоковая передача данных с датчиков
- и т.д.
"""

con_res = sqlite3.connect(':memory:')

con_res.close()
