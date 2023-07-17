import pathlib
import sqlite3

DB_NAME: str = 'db_m_to_m.sqlite'

con = sqlite3.connect(DB_NAME)

cur = con.cursor()

cur.executescript("""
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS directors(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS directors_movies(
        director_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        PRIMARY KEY (director_id, movie_id),
        FOREIGN KEY(director_id) REFERENCES directors(id),
        FOREIGN KEY(movie_id) REFERENCES movies(id)
    );
""")

con.close()

input('Для удаления БД нажмите "Enter", или закройте консоль для отмены.')
try:
    pathlib.Path(DB_NAME).unlink()
except Exception as err:
    print(f"Ошибка при удалении файла: {err}")
