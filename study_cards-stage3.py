# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: StudyCards
class StudyCard:
    def __init__(self, topic, question, answer, created_at=None):
        self.id = len(cards_db) + 1 if cards_db else 1
        self.topic = topic
        self.question = question
        self.answer = answer
        self.created_at = created_at or datetime.now().isoformat()
        self.last_reviewed = None
        self.review_count = 0

cards_db = []

def add_card(topic, question, answer):
    new_card = StudyCard(topic=topic, question=question, answer=answer)
    cards_db.append(new_card)
    return new_card

def get_all_cards():
    return cards_db.copy()
