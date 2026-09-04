# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: StudyCards
def demo():
    """Показать основной сценарий: создание карточки, тест, просмотр статистики."""
    # Создаём карточку
    card = Card(
        question="Что такое Python?",
        answer="Язык программирования с динамической типизацией",
        difficulty="easy",
        theme="Базовые понятия",
    )

    # Тестируем карточку — пользователь отвечает "Язык программирования"
    score = card.test("Язык программирования")
    print(f"Карточка: {card.question}")
    print(f"Правильный ответ: {card.answer}")
    print(f"Пользователь ответил: да" if score else "Пользователь ответил: нет")
    print(f"Оценка: {'✅' if score else '❌'}")
    print(f"Сложность: {card._difficulty}")
    print(f"Тема: {card._theme}")
    print(f"Повторы: {card._repeats}")
    print(f"Ошибок: {card._errors}")
    print(f"Последний просмотр: {card._last_review}")
    print(f"Будущий повтор: {card._next_review}")
    print(f"Всего создано: {Card._created}")
    print("\nДемо завершено.")
