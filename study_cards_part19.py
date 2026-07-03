# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: StudyCards
def archive_old_cards(min_days=30, dry_run=False):
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=min_days)
    archived_count = 0
    for card in cards:
        if card.last_reviewed and card.last_reviewed < cutoff:
            if not card.archived:
                card.archived = True
                print(f"Archived: {card.id} ({card.front})")
                archived_count += 1
    if dry_run:
        return f"Dry run: would archive {archived_count} cards."
    else:
        return f"Archived {archived_count} cards older than {min_days} days."
