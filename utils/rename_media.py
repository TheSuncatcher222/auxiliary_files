"""
Переименовывает медиафайлы согласно паттерну.
"""

# TODO. Перезаписывать мета-информацию с вариантом выбора развития событий.

from os import listdir, path as os_path
from pathlib import Path
from re import fullmatch
from shutil import move

FILENAME_DELETE_PREFIX: tuple[str] = (
    'img_',
    'photo_',
    'screenshot_',
    'vid_',
    'video_',
)
FILENAME_DELETE_SUFFIX: tuple[str] = (
    '_telegram',
)
EXTENSION_REPLACE: dict[str, str] = {
    '.jpeg': '.jpg',
}
EXTENSION_SUPPORTED: list[str] = (
    '.jpg',
    '.jpeg',
    '.mp4',
)
GOOD_DIR_NAME: str = '__ok'


def prepare_dirs() -> tuple[Path, Path]:
    """Подготавливает директории к работе с файлами."""
    current_dir: Path = Path(__file__).parent
    good_dir: Path = current_dir / GOOD_DIR_NAME
    good_dir.mkdir(parents=True, exist_ok=True)
    return current_dir, good_dir


def replace_extension(file_extension: str) -> str:
    """Заменяет расширение файла."""
    file_extension: str = file_extension.lower()
    return EXTENSION_REPLACE.get(file_extension, file_extension)


def replace_name(file_name: str) -> tuple[str, bool]:
    """Заменяет имя файла."""
    filename_lower: str = file_name.lower()
    for start_val in FILENAME_DELETE_PREFIX:
        if filename_lower.startswith(start_val):
            file_name: str = file_name[len(start_val):]
    for end_val in FILENAME_DELETE_SUFFIX:
        if filename_lower.endswith(end_val):
            file_name: str = file_name[:len(filename_lower)-len(end_val)]

    if fullmatch(
        pattern=r'^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.*$',
        string=file_name,
    ):
        return file_name, True

    if not fullmatch(
        pattern=r'^\d{8}_\d{6}.*$',
        string=file_name,
    ):
        return file_name, False

    return (
        f"{file_name[:4]}-{file_name[4:6]}-{file_name[6:8]}_{file_name[9:11]}-{file_name[11:13]}-{file_name[13:]}",
        True,
    )


def move_object(src: Path, dst: Path) -> None:
    """Перемещает файл в указанный каталог."""
    counter: int = 1
    new_dst: Path = dst
    try:
        while new_dst.exists():
            new_dst = dst.parent / f'{dst.stem}_{counter}{dst.suffix}'
            counter += 1
        move(src=str(src), dst=str(new_dst))
    except Exception as err:
        print(f'File: {src}')
        print(err)
    return


def main():
    current_dir, good_dir = prepare_dirs()

    for obj in listdir(current_dir):
        obj_path: Path = current_dir / obj
        if (
            not obj_path.is_file()
            or
            obj_path.suffix not in EXTENSION_SUPPORTED
        ):
            continue

        name, extension = os_path.splitext(obj)
        extension: str = replace_extension(extension)
        name, ok = replace_name(file_name=name)
        if ok:
            move_object(
                src=obj,
                dst=good_dir / f'{name}{extension}',
            )
    

if __name__ == '__main__':
    main() 
