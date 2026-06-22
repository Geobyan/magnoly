# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: StudyCards
import json, os
from pathlib import Path

def load_study_data(file_path: str) -> dict | None:
    path = Path(file_path)
    if not path.exists():
        print(f"Файл {file_path} не найден.")
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Неверный формат JSON")
        print(f"Данные успешно загружены из {path}")
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON в файле {file_path}: {e}")
        return None
    except PermissionError:
        print(f"Нет прав доступа к чтению файла {file_path}.")
        return None
