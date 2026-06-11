# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: StudyCards
def delete_card(card_id):
    """Удалить карточку по ID. Возвращает True если удалено, False если не найдена."""
    if card_id not in cards:
        print(f"Карточка с ID {card_id} не найдена.")
        return False
    
    del cards[card_id]
    print(f"Карточка с ID {card_id} успешно удалена.")
    return True

def handle_delete_command(message):
    """Обработка команды удаления через парсинг текста."""
    if not message.text:
        return "Нет текста сообщения для обработки."
    
    text = message.text.lower()
    
    if "удалить" in text or "delete" in text:
        # Ищем число после ключевых слов
        import re
        match = re.search(r'(?:удалить|delete)\s*(\d+)', text)
        
        if match:
            card_id = int(match.group(1))
            if delete_card(card_id):
                return "Карточка удалена."
            else:
                return "Ошибка: карточка не найдена."
        else:
            return "Не удалось распознать ID карточки для удаления. Используйте формат: 'удалить 123'."
    else:
        return "Команда удаления не распознана. Используйте 'удалить [ID]'."
