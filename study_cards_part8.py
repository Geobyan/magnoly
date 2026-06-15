# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: StudyCards
import sys
from typing import Dict, List, Optional

def print_menu() -> None:
    """Отображает текстовое меню приложения."""
    print("\n=== StudyCards Menu ===")
    print("1. Добавить новую карточку")
    print("2. Просмотреть все карточки")
    print("3. Удалить карточку по ID")
    print("4. Выход из программы")
    print("======================\n")

def get_int_input(prompt: str, min_val: Optional[int] = None) -> int:
    """Запрашивает целое число у пользователя с валидацией."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Ошибка: значение должно быть не меньше {min_val}.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите корректное число.")

def get_str_input(prompt: str) -> str:
    """Запрашивает строку у пользователя."""
    return input(prompt).strip()

class StudyCardsCLI:
    """Командная оболочка для приложения StudyCards."""
    
    def __init__(self, cards_data: Dict[str, List[Dict]]):
        self.cards = cards_data  # Структура данных карточек
    
    def run(self) -> None:
        """Запускает основной цикл командной строки."""
        while True:
            print_menu()
            choice = get_int_input("Выберите действие (1-4): ", min_val=1)
            
            if choice == 1:
                self.add_card()
            elif choice == 2:
                self.list_cards()
            elif choice == 3:
                self.delete_card()
            elif choice == 4:
                print("До свидания!")
                break
    
    def add_card(self) -> None:
        """Добавляет новую карточку в приложение."""
        topic = get_str_input("Введите тему карточки (или Enter для пропуска): ") or "Общее"
        question = get_str_input("Введите вопрос:")
        answer = get_str_input("Введите ответ:")
        
        if not self.cards.get(topic):
            self.cards[topic] = []
            
        card_id = len(self.cards[topic]) + 1
        new_card = {"id": card_id, "question": question, "answer": answer}
        self.cards[topic].append(new_card)
        print(f"Карточка #{card_id} добавлена в тему '{topic}'.")

    def list_cards(self) -> None:
        """Отображает список всех карточек."""
        if not self.cards:
            print("Список карточек пуст.")
            return
            
        for topic, cards in sorted(self.cards.items()):
            print(f"\n--- Тема: {topic} ---")
            for card in cards:
                print(f"ID: {card['id']}, Вопрос: {card['question']}")

    def delete_card(self) -> None:
        """Удаляет карточку по её ID."""
        topic = get_str_input("Введите тему, в которой искать карточку (или Enter для поиска везде): ") or "Все темы"
        
        if topic == "Все темы":
            topics_to_search = list(self.cards.keys())
        else:
            topics_to_search = [topic]
            
        card_id = get_int_input("Введите ID карточки для удаления:", min_val=1)
        
        deleted = False
        for t in topics_to_search:
            if topic == "Все темы":
                current_topic_name = t
            else:
                current_topic_name = topic
                
            # Ищем карточку в текущей теме (или во всех, если тема не задана)
            cards_list = self.cards.get(current_topic_name, [])
            for i, card in enumerate(cards_list):
                if card["id"] == card_id:
                    del self.cards[current_topic_name][i]
                    print(f"Карточка ID {card_id} удалена из темы '{current_topic_name}'.")
                    deleted = True
                    break
        
        if not deleted and topic != "Все темы":
             # Если тема была задана явно, но карточки там нет, пробуем поискать в других (опционально)
             pass 
        elif not deleted:
            print(f"Карточка с ID {card_id} не найдена.")
