# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: StudyCards
class SearchFilter:
    def __init__(self, query):
        self.query = query.lower().strip() if query else ""
    
    def matches(self, card):
        if not self.query:
            return True
        
        text_fields = [card.get('front'), card.get('back'), card.get('title')]
        
        for field in text_fields:
            if field is None:
                continue
            
            # Ищем совпадение с учётом регистра, но игнорируя его в сравнении
            if self.query.lower() in str(field).lower():
                return True
        
        return False

def search_cards(cards, query):
    filter = SearchFilter(query)
    return [card for card in cards if filter.matches(card)]
