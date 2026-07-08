# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: StudyCards
def check_due_reminders(cards_db, user_id):
    """Проверяет просроченные напоминания и выводит список."""
    reminders = [r for r in cards_db.get("reminders", []) if r["user_id"] == user_id]
    now = datetime.now()
    due_now = [r for r in reminders if now >= r["scheduled_for"]]
    overdue = [r for r in due_now if now > r["deadline"]]
    print(f"Просрочено напоминаний: {len(overdue)}")
    return len(overdue) == 0
