# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: StudyCards
import json, os, random, hashlib, time
from datetime import datetime, timedelta

INITIAL_DATA = '''
{
  "themes": ["Python", "JS", "Math"],
  "cards": [
    {"id": 1, "theme": "Python", "front": "Что делает print?", "back": "Выводит данные в консоль"},
    {"id": 2, "theme": "JS", "front": "Как объявить переменную (ES6)?", "back": "let или const"},
    {"id": 3, "theme": "Math", "front": "Квадрат числа 5?", "back": "25"}
  ],
  "stats": {}
}'''

def load_initial_data():
    try:
        data = json.loads(INITIAL_DATA)
        if not isinstance(data, dict): raise ValueError("Invalid JSON structure")
        
        # Seed stats with current date for first run
        today = datetime.now().strftime("%Y-%m-%d")
        if "stats" in data and today in data["stats"]:
            return data
        
        # Initialize stats if empty or missing
        if not isinstance(data.get("stats"), dict):
            data["stats"] = {}
        
        # Add first day entry if needed
        if today not in data["stats"]:
            data["stats"][today] = {"learned": 0, "reviewed": 0}
            
        return data
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse initial JSON: {e}")
