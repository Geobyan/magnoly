# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: StudyCards
import random

# --- StudyCards: Базовая структура и демо-данные ---

class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def __str__(self):
        return f"[{self.front}] -> [{self.back}]"

def generate_demo_cards():
    """Генерирует набор демонстрационных карточек по разным темам."""
    topics = {
        "Python": [
            Card("Что такое PEP 8?", "Стандарт кодирования для Python."),
            Card("Какой тип данных используется для словарей?", "dict"),
            Card("Как создать пустой список?", "[] или list()")
        ],
        "История": [
            Card("В каком году началась Вторая мировая война?", "1939"),
            Card("Столица Франции?", "Париж"),
            Card("Кто был первым президентом США?", "Джордж Вашингтон")
        ],
        "Математика": [
            Card("Результат 2^10?", "1024"),
            Card("Сколько градусов в прямом угле?", "90"),
            Card("Формула площади круга?", "S = πr²")
        ]
    }
    
    cards_list = []
    for topic, items in topics.items():
        for item in items:
            cards_list.append(Card(topic + ": " + item.front, item.back))
    return cards_list

def shuffle_cards(cards):
    """Перемешивает список карточек (алгоритм Фишера-Йейтса)."""
    shuffled = cards.copy()
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

def main():
    print("=== StudyCards: Запуск демо-режима ===")
    
    # 1. Создание данных
    deck = generate_demo_cards()
    print(f"Создано {len(deck)} карточек.")
    
    # 2. Перемешивание
    shuffled_deck = shuffle_cards(deck)
    
    # 3. Вывод первых 5 карточек
    for i, card in enumerate(shuffled_deck[:5], 1):
        print(f"\nКарточка {i}:")
        print(card)
        
    input("\nНажмите Enter для завершения демо...")

if __name__ == "__main__":
    main()
