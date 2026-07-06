# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: StudyCards
import datetime, json

class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.done = False
        self.created_at = datetime.datetime.now()

    def is_overdue(self):
        return not self.done and datetime.datetime.now() > self.due_date

class ReminderManager:
    def __init__(self, storage="reminders.json"):
        self.storage = storage
        self.reminders = []
        if os.path.exists(storage):
            with open(storage) as f:
                data = json.load(f)
            for r in data:
                self.reminders.append(Reminder(r["title"], datetime.datetime.strptime(r["due_date"], "%Y-%m-%d").date()))

    def add(self, title, due_date_str):
        try:
            due = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Неверный формат даты (YYYY-MM-DD)")
            return None
        r = Reminder(title, due)
        self.reminders.append(r)
        with open(self.storage, "w") as f:
            json.dump([{"title": x.title, "due_date": x.due_date.isoformat()} for x in self.reminders], f, indent=2)
        return r

    def get_overdue(self):
        return [r for r in self.reminders if r.is_overdue()]

    def mark_done(self, index):
        if 0 <= index < len(self.reminders):
            self.reminders[index].done = True
            with open(self.storage, "w") as f:
                json.dump([{"title": x.title, "due_date": x.due_date.isoformat()} for x in self.reminders], f, indent=2)
