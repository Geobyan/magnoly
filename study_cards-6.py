# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: StudyCards
from typing import Callable, Optional
def filter_cards(
    cards: list[dict],
    status_filter: Optional[str] = None,
    category_filter: Optional[str] = None,
    tag_filters: Optional[list[str]] = None
) -> list[dict]:
    filtered = []
    for card in cards:
        if status_filter and card.get("status") != status_filter:
            continue
        if category_filter and card.get("category") != category_filter:
            continue
        if tag_filters:
            card_tags = card.get("tags", [])
            if not any(t in card_tags for t in tag_filters):
                continue
        filtered.append(card)
    return filtered

def get_filtered_cards(
    status: Optional[str] = None,
    category: Optional[str] = None,
    tags: Optional[list[str]] = None
) -> list[dict]:
    all_cards = load_all_cards()
    if not all_cards:
        print("Нет доступных карточек.")
        return []
    try:
        filtered_list = filter_cards(
            cards=all_cards,
            status_filter=status,
            category_filter=category,
            tag_filters=tags
        )
        if filtered_list:
            for idx, card in enumerate(filtered_list, 1):
                print(f"{idx}. {card['question']} [{card.get('status', 'unknown')}]")
            return filtered_list
    except Exception as e:
        print(f"Ошибка фильтрации: {e}")
    return []
