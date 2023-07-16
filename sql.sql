-- Все команды пишутся БОЛЬШИМИ БУКВАМИ
-- После команды обязательно ставить ";"

-- Создать таблицу (если она не существует)
-- CREATE TABLE IF NOT EXISTS имя-таблицы(столбец ТИП-ДАННЫХ, …);
CREATE TABLE IF NOT EXISTS movies(name TEXT, release_year INTEGER);

-- Создать запись в таблице
-- INSERT INTO имя-таблицы VALUES(знач1, знач2, ….);
INSERT INTO movies VALUES('Весёлые мелодии', 1930);

-- Вернуть поля из таблицы: SELECT столбец1, столбец2… FROM имя-таблицы;
-- * означает вернуть все поля
SELECT *
FROM movies;

SELECT name
FROM movies;

SELECT name
FROM movies
WHERE release_year = 1930;
