# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: StudyCards
def export_state():
    import json
    state = {
        "cards": cards,
        "themes": themes,
        "stats": stats,
        "last_review_date": last_review_date.isoformat() if last_review_date else None
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
