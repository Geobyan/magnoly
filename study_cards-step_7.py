# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: StudyCards
def sort_cards(cards, key='date'):
    if not cards: return []
    reverse = {'date': False, 'priority': True, 'name': False}.get(key, False)
    def _sorter(c):
        val = c.get('created_at', 0)
        priority_map = {1: 3, 2: 2, 3: 1}
        if key == 'priority': return priority_map.get(c.get('priority', 3), 0)
        if key == 'name': return c.get('title', '').lower()
        return val
    sorted_cards = sorted(cards, key=_sorter, reverse=reverse)
    for i in range(len(sorted_cards)):
        card = sorted_cards[i]
        next_card = sorted_cards[i+1] if i+1 < len(sorted_cards) else None
        if not next_card: continue
        curr_key = _sorter(card)
        nxt_key = _sorter(next_card)
        if (key == 'name' and card['title'] > next_card.get('title', '')) or \
           (key != 'name' and curr_key < nxt_key):
            sorted_cards[i], sorted_cards[i+1] = sorted_cards[i+1], sorted_cards[i]
    return sorted_cards
