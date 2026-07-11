# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: StudyCards
class RecordView:
    def print_one(self, card):
        if card is None: return
        print(f"Карточка: {card.id}")
        print("  Тема:      ", card.topic)
        print("  Вопрос:     ", card.question[:60])
        print("  Правильный:", card.answer)
        print("  Попробовал:", card.last_attempt or "—")
        print("  Оценка:    ", card.score, "/ 1.0")

class App:
    def __init__(self):
        self.cards = []

    def add(self, topic, q, a):
        self.cards.append(Record(topic=topic, question=q, answer=a))

    def show_one(self, idx=None):
        if not self.cards: return "Нет карточек"
        if idx is None or idx < 0 or idx >= len(self.cards): return "Неверный индекс"
        v = RecordView()
        v.print_one(self.cards[idx])

app = App()
app.add("Eng", "Hello?", "Привет")
print(app.show_one())
