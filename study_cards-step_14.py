# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: StudyCards
def generate_summary():
    if not cards: return None
    total = len(cards)
    mastered = sum(1 for c in cards if c.get('status') == 'mastered')
    themes = set(c['theme'] for c in cards)
    stats = {t: [c for c in cards if c['theme'] == t] for t in themes}
    return f"Всего карточек: {total}, Овладение: {mastered}/{total} ({100*mastered//max(1,total)}%), Темы: {', '.join(sorted(themes))}"
