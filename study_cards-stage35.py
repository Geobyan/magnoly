# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: StudyCards
def next_action_stats():
    """Выводит рекомендации следующего действия на основе статистики."""
    if not stats:
        print("Сначала создайте хотя бы одну карточку.")
        return
    
    total = sum(s["count"] for s in stats.values())
    average = total / len(stats) if stats else 0

    if average < 1.5:
        print("📚 Вы только начинаете — повторите уже изученные карты!")
    elif average > 3 and all(count >= 2 for count in stats.values()):
        print("🎉 Отлично! Все темы готовы к финальному тесту.")
    else:
        weak = {k: v for k, v in stats.items() if v < average}
        strong = [k for k, v in stats.items() if v >= average]
        if weak:
            print(f"💡 Проработайте слабые темы: {', '.join(weak.keys())}")
        else:
            print("✅ Вы на правильном пути — продолжайте обучение!")

next_action_stats()
