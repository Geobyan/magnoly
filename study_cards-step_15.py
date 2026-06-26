# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: StudyCards
def calculate_weekly_stats(stats: dict) -> list[dict]:
    if not stats.get('cards'): return []
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    weekly_data = {d: 0 for d in range(week_start, week_end)}
    for card_id, info in stats.get('cards', {}).items():
        last_review = info.get('last_review')
        if isinstance(last_review, str):
            try: last_review = date.fromisoformat(last_review)
            except ValueError: continue
        elif not isinstance(last_review, date): continue
        if week_start <= last_review < week_end:
            weekly_data[last_review] += 1
    return [{'date': d, 'reviewed': count} for d, count in sorted(weekly_data.items()) if count > 0]
