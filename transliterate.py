"""
Модуль транслитерации текста.
"""

from transliterate import translit


def transliterate_to_russian(name: str, code: str = 'ru'):
    transliterated_name = translit(name, 'ru')
    return transliterated_name.strip()


names: list[str] = [
    'Kirill Свидунович',
    'Кирилл Svidunovich',
    'Кирилл Svidunovich',
    'Кiриlл Svидunoвich',
]

for name in names:
    print(transliterate_to_russian(name))  # Вывод: Кирилл Свидунович
