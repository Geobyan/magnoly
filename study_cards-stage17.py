# === Stage 17: Добавь группировку записей по категориям ===
# Project: StudyCards
from collections import defaultdict, Counter
def group_by_category(records: list[dict], key_field: str = "category") -> dict[str, list]:
    groups = defaultdict(list)
    for r in records:
        cat = r.get(key_field, "Uncategorized")
        if isinstance(cat, str):
            groups[cat].append(r)
        else:
            raise ValueError(f"Field '{key_field}' must be a string or None, got {type(cat)}")
    return dict(groups)

def get_category_stats(records: list[dict], key_field: str = "category", value_field: str = "score") -> dict[str, dict]:
    groups = group_by_category(records, key_field)
    stats = {}
    for cat, items in groups.items():
        scores = [i.get(value_field, 0) for i in items]
        if not scores:
            continue
        avg_score = sum(scores) / len(scores)
        correct_count = sum(1 for s in scores if s > 50)
        stats[cat] = {
            "count": len(items),
            "avg_score": round(avg_score, 2),
            "correct_rate": round(correct_count / len(items) * 100, 1)
        }
    return dict(sorted(stats.items(), key=lambda x: x["count"], reverse=True))
