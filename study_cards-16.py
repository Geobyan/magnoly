# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: StudyCards
def get_monthly_stats(start_date, end_date):
    from datetime import timedelta
    stats = {}
    current = start_date
    while current <= end_date:
        month_key = current.strftime("%Y-%m")
        if month_key not in stats:
            stats[month_key] = {"total_cards": 0, "reviewed": 0, "new": 0}
        # Пример заполнения статистики (заглушка для структуры)
        stats[month_key]["total_cards"] += 1
        current += timedelta(days=1)
    return stats
