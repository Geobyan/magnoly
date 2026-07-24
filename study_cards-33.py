# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: StudyCards
def undo_last_action(self):
    """Откатывает последнее действие в текущем списке (показ/добавление/удаление)."""
    if not self.history:
        return False
    action = self.history.pop()
    if action['type'] == 'add':
        card = Card.from_dict(action['card'])
        self.cards[card.id] = card
        self._update_stats(card.id, 'updated')
    elif action['type'] == 'remove':
        card_id = action['card_id']
        if card_id in self.cards:
            del self.cards[card_id]
            self._update_stats(card_id, 'removed')
    elif action['type'] == 'answer':
        card_id = action['card_id']
        answer = action['answer']
        card = self.cards.get(card_id)
        if card:
            card.set_answer(answer)
            self._update_stats(card_id, 'answered', answer)
    elif action['type'] == 'review':
        card_id = action['card_id']
        card = self.cards.get(card_id)
        if card and not card.answered:
            card.mark_reviewed()
            self._update_stats(card_id, 'reviewed')
    return True
