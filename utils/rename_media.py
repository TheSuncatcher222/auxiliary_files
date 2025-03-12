"""
Переименовывает медиафайлы согласно паттерну.
"""

from os import listdir, path as os_path
from pathlib import Path
from re import fullmatch
from shutil import move

SUPPORTED_EXTENSION: list[str] = [
    '.jpg',
    '.jpeg',
    '.mp4',
]
EXTENSION_REPLACE: dict[str, str] = {
    '.jpeg':
    '.jpg',
}
VALID_EXTENSION: list[str] = [
    '.jpg',
    '.mp4',
]


def prepare_dirs() -> tuple[Path, Path, Path]:
    """Подготавливает директории к работе с файлами."""
    current_dir: Path = Path(__file__).parent
    bad_dir: Path = current_dir / '__bad'
    good_dir: Path = current_dir / '__ok'
    for dir in (bad_dir, good_dir):
        dir.mkdir(parents=True, exist_ok=True)
    return current_dir, good_dir, bad_dir


def replace_extension(file_extension: str) -> str:
    """Заменяет расширение файла."""
    file_extension: str = file_extension.lower()
    return EXTENSION_REPLACE.get(file_extension, file_extension)


def replace_name(file_name: str) -> tuple[str, bool]:
    """Заменяет имя файла."""
    if file_name.startswith('photo_'):
        file_name: str = file_name[6:]
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
    current_dir, good_dir, bad_dir = prepare_dirs()

    for obj in listdir(current_dir):
        obj_path: Path = current_dir / obj
        if (
            not obj_path.is_file()
            or
            obj_path.suffix not in SUPPORTED_EXTENSION
        ):
            continue

        name, extension = os_path.splitext(obj)
        extension: str = replace_extension(extension)

        dst_dir: Path = bad_dir
        if extension in VALID_EXTENSION:
            name, ok = replace_name(file_name=name)
            if ok:
                dst_dir = good_dir

        move_object(
            src=obj_path,
            dst=dst_dir / f'{name}{extension}',
        )
    
    input('Press Enter to continue...')


if __name__ == '__main__':
    main() 
