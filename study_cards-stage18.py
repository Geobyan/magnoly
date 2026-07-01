# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: StudyCards
class TagManager:
    def __init__(self):
        self.tags = {}  # {tag_name: count}
    
    def add_tag(self, card_id, tag_name):
        if not tag_name.strip():
            return False
        current_count = self.tags.get(tag_name, 0)
        self.tags[tag_name] = current_count + 1
        if card_id in CardDatabase.cards:
            CardDatabase.cards[card_id]['tags'].append(tag_name)
        return True
    
    def remove_tag(self, card_id, tag_name):
        if not tag_name.strip():
            return False
        if card_id not in CardDatabase.cards or tag_name not in CardDatabase.cards[card_id].get('tags', []):
            return False
        tags_list = CardDatabase.cards[card_id]['tags']
        if tags_list.count(tag_name) > 1:
            tags_list.remove(tag_name)
        else:
            tags_list.remove(tag_name)
            del self.tags[tag_name]
        return True
    
    def get_tag_count(self, tag_name):
        return self.tags.get(tag_name, 0)
