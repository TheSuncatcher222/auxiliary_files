1. Подготовка виртуального окружения

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

2. Экспорт в .exe файл

```bash
pyinstaller --onefile "script.py"
mv dist/script.exe script.exe
rm -r build
rm -r dist
rm script.spec
```
