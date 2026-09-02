# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: StudyCards
def migrate_cards_structure():
    """Валидация и миграция структуры карточек при запуске."""
    global cards, themes, stats
    try:
        if not cards:
            cards = {}
        if not themes:
            themes = {}
        if not stats:
            stats = {}
        for card_id, card_data in cards.items():
            if 'created_at' not in card_data:
                card_data['created_at'] = current_time()
            if 'updated_at' not in card_data:
                card_data['updated_at'] = current_time()
            if 'version' not in card_data:
                card_data['version'] = 1
    except Exception:
        cards = {}
        themes = {}
        stats = {}
    return cards, themes, stats
