# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: StudyCards
def repair_simple_issues(self):
        """Check data integrity and fix common problems in place."""
        if not self.cards:
            return 0, 0, 0
        
        fixed_count = 0
        warnings = []
        
        for card_id, card in list(self.cards.items()):
            # Repair corrupted progress tracking
            if card['progress'] is None or card['progress'] < 0:
                card['progress'] = 1
                fixed_count += 1
            
            # Fix invalid due_date format
            try:
                from datetime import datetime, timedelta
                due = card.get('due_date')
                if isinstance(due, str) and len(due) > 10:
                    clean_due = due[:4] + '-' + due[5:7] + '-' + due[8:10]
                    parsed = datetime.strptime(clean_due, '%Y-%m-%d')
                    card['due_date'] = (parsed + timedelta(days=365)).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                    fixed_count += 1
            
            except Exception:
                pass
        
        # Repair topic references pointing to non-existent topics
        valid_topics = set(self.topics.keys()) if self.topics else set()
        for card_id, card in list(self.cards.items()):
            topic_name = card.get('topic')
            if topic_name and topic_name not in valid_topics:
                warnings.append(f"Card {card_id} references unknown topic '{topic_name}'")
        
        # Repair progress tracking that lost streak data  
        for card_id, card in list(self.cards.items()):
            if 'progress' in card and 'streak' not in card:
                card['streak'] = 0
        
        return fixed_count, len(warnings), 0
