# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: StudyCards
def edit_card(card_id, new_data):
    if card_id not in cards:
        print(f"Карточка с ID {card_id} не найдена.")
        return False
    
    updated = False
    for key, value in new_data.items():
        if key in card_fields and value is not None:
            cards[card_id][key] = value
            updated = True
    
    if updated:
        print(f"Карточка {card_id} обновлена.")
        return True
    else:
        print("Нет изменений для обновления или некорректные поля.")
        return False
