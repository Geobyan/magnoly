# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: StudyCards
from collections import Counter

def compute_metrics(cards, responses):
    """Compute key project metrics: accuracy, response distribution, topic stats."""
    if not responses:
        return {"total_responses": 0, "accuracy": 0.0, "response_types": {}, "topic_distribution": {}}

    total = len(responses)
    correct = sum(1 for r in responses if r.get("correct", False))
    
    type_counts = Counter(r.get("type", "unknown") for r in responses)
    topic_counts = Counter()
    for card in cards:
        topic_counts[card.get("topic", "default")] += 1
    
    return {
        "total_responses": total,
        "accuracy": correct / total if total else 0.0,
        "response_types": dict(type_counts),
        "topic_distribution": dict(topic_counts)
    }

metrics = compute_metrics(cards, responses)
