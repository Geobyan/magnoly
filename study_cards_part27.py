# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: StudyCards
def reset_demo_data():
    """Сбросить демо-данные в дефолтные значения."""
    global cards, deck_order, current_theme, stats, history, streaks
    
    default_cards = [
        {"id": 1, "front": "Python - язык программирования", "back": "Высокоуровневый интерпретируемый язык", "category": "Programming", "difficulty": "easy"},
        {"id": 2, "front": "HTTP - протокол передачи данных", "back": "Гипертекстовая передача гипердокументов", "category": "Web Development", "difficulty": "medium"},
        {"id": 3, "front": "CSS Grid Layout", "back": "Система сеток для расположения элементов", "category": "Web Development", "difficulty": "hard"},
        {"id": 4, "front": "Git - система контроля версий", "back": "Дистрибутивная система управления изменениями кода", "category": "Programming", "difficulty": "medium"},
        {"id": 5, "front": "Django - веб-фреймворк", "back": "Модель MVC для Python с ORM и админкой", "category": "Web Development", "difficulty": "hard"}
    ]
    
    cards = default_cards
    deck_order = list(range(len(cards)))
    current_theme = None
    stats = {"total_reviews": 0, "correct_answers": 0, "incorrect_answers": 0}
    history = []
    streaks = {}

def clear_state():
    """Полностью очистить состояние приложения."""
    global cards, deck_order, current_theme, stats, history, streaks
    
    cards = []
    deck_order = []
    current_theme = None
    stats = {"total_reviews": 0, "correct_answers": 0, "incorrect_answers": 0}
    history = []
    streaks = {}

if __name__ == "__main__":
    print("StudyCards Demo Data Reset")
    reset_demo_data()
    print(f"Total cards: {len(cards)}")
    
    print("\nClear State Test")
    clear_state()
    print(f"Cards after clear: {len(cards)}")
