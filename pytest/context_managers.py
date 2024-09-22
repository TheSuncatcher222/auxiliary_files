"""
Класс контекстного менеджера.

Контекстный менеджер - это объект, который управляет ресурсами памяти,
которе должны быть правильно и гарантировано завершены после их использования.

Контекстные менеджеры используются, например, при открытии файлов,
обращения к внешним ресурсам (каналы связи), подключениях к базам данных.
Python позволяет создавать свои контекстные менеджеры помощью двух способов:
    - через класс: в нем должны быть реализованы методы __enter__ и __exit__
    - через декоратор: при использовании библиотеки contextlib

Помимо этого, контекстные менеджеры могут реализовывать любую дополнительную логику
в процессе управления ресурсами памяти.

Метод __enter__ открывает ресурс и загружает данные в оперативную память,
а также возвращает объект, к которым ведется работа (например внутри with)

Метод __exit__ освобождает ресурсы и обрабатывает исключения, если они
возникли в блоке with. Внутри __exit__ можно управлять тем, как контекстный
менеджер будет реагировать на ошибки. Если он возвращает True, исключение
будет подавлено и не всплывет за пределы with блока, если False | None - 
исключение пойдет дальше. Этот метод вызовется автоматически при возникновении исключения.

Преимущество contextlib:
    - позволяет создавать контекстные менеджеры из генераторов (компактность и лаконичность)
    - он уже написан и протестирован разработчиками Python
    - предоставляет дополнительные варианты реализации, например управление
      несколькими контекстными менеджерами одновременно (ExitStack)

Контекстные менеджеры могут быть использованы в асинхронном коде.
Для этого надо реализовать методы __aenter__ и __aexit__.

Области применения:
    - работа с файлами
    - работа с БД
    - работа с переменными окружения
    - откладывание выполнения кода после выполнения with блока
    - логирование исключений
"""

from contextlib import (
    ExitStack,
    contextmanager,
)
import os
from types import TracebackType
from typing import IO

class MyContextManager:


    def __init__(
        self,
        *,
        filename: str,
        mode: str,
        newline: str = "\n",
        encoding: str = "utf-8",
    ) -> None:
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.newline = newline

    def __enter__(self) -> IO[any]:
        self.file: IO[any] = open(
            file=self.filename,
            mode=self.mode,
            encoding=self.encoding,
            newline=self.newline,
        )
        return self.file

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: str | None,
        traceback: TracebackType,
    ) -> None:
        if exc_type:
            return False
        if self.file:
            self.file.close()
        return True


class MyAsyncContextManager:

    def __init__(
        self,
        *,
        filename: str,
        mode: str,
        newline: str = "\n",
        encoding: str = "utf-8",
    ):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.newline = newline

    async def __aenter__(self) -> IO[any]:
        self.file: IO[any] = open(
            file=self.filename,
            mode=self.mode,
            encoding=self.encoding,
            newline=self.newline,
        )
        return self.file

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: str | None,
        traceback: TracebackType,
    ) -> bool:
        if exc_type:
            return False
        if self.file:
            self.file.close()
        return True


@contextmanager
def my_context_manage(
    *,
    filename: str,
    mode: str,
    encoding: str = 'utf-8',
    newline: str = '\n',
):
    f: IO[any] = open(
        file=filename,
        mode=mode,
        encoding=encoding,
        newline=newline,
    )
    try:
        yield f
    finally:
        f.close()


# -----------------------------------------------------------------------------


@contextmanager
def change_environment(key: str, value: str):
    old_value: str = os.getenv(key=key)
    os.environ[key] = value
    try:
        yield
    finally:
        if old_value is None:
            del os.environ[key]
        else:
            os.environ[key] = old_value
    return

@contextmanager
def lazy_write(file: str, context: str):
    buffer = []
    buffer.append[file]
    try:
        yield
    finally:
        with open(file=file, mode='w', encoding='utf-8') as f:
            f.writelines(buffer)
    return

class MyHandleExceptionContextManager:

    ...

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_value:
            print(f'Логируем исключение {exc_value}')
        return True


# -----------------------------------------------------------------------------


with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    data1 = file1.read()
    data2 = file2.read()
    print(data1, data2)

filenames = ['file1.txt', 'file2.txt', 'file3.txt']

with ExitStack() as stack:
    files = [stack.enter_context(open(fname, 'r')) for fname in filenames]
    for file in files:
        print(file.read())


# -----------------------------------------------------------------------------

    
class MyContext:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback: TracebackType):
        if exc_type:
            print(traceback.tb_lasti)
        return True  # Исключение будет подавлено

with MyContext():
    raise ValueError("Ошибка")
