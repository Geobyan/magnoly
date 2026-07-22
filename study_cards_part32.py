# === Stage 32: Добавь журнал действий пользователя ===
# Project: StudyCards
class ActionLog:
    def __init__(self):
        self._entries = []
    
    def record(self, action_type, details=None):
        entry = {
            "time": datetime.now().isoformat(),
            "type": action_type,
            "details": details or ""
        }
        self._entries.append(entry)
    
    def log_study(self, card_id, result):
        self.record("study", f"Card #{card_id}: {result}")
    
    def log_review(self, cards_count, results):
        res_str = ", ".join(f"{k}:{v}" for k, v in results.items())
        self.record("review", f"N={cards_count}, {res_str}")
    
    def get_report(self):
        if not self._entries: return "Нет записей"
        from collections import Counter
        counts = Counter(e["type"] for e in self._entries)
        lines = [f"{t}: {counts[t]}" for t in sorted(counts)]
        return "\n".join(lines) + f"\nВсего: {len(self._entries)} действий"

    def get_recent(self, n=5):
        return self._entries[-n:] if self._entries else []

log = ActionLog()
