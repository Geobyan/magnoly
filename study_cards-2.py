# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: StudyCards
class Card:
    def __init__(self, id_, question, answer, theme="General", due_date=None):
        self.id = id_
        self.question = question
        self.answer = answer
        self.theme = theme
        self.due_date = due_date

    def is_due(self, current_date=None):
        if current_date is None:
            current_date = datetime.now()
        return self.due_date <= current_date

class StudyStats:
    def __init__(self):
        self.total_cards = 0
        self.reviewed_today = 0
        self.last_review = None

def validate_input(user_input, expected_type=str, min_length=1, max_length=None):
    if not user_input or not isinstance(user_input, expected_type):
        return None
    user_input = user_input.strip()
    if len(user_input) < min_length:
        return None
    if max_length and len(user_input) > max_length:
        return None
    return user_input

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
