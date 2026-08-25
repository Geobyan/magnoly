# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: StudyCards
def dry_run(operation, *args, **kwargs):
    """Log a data mutation as a dry-run entry without persisting it."""
    record = {
        "timestamp": datetime.now().isoformat(),
        "mode": "dry-run",
        "operation": operation,
        "args": args,
        "kwargs": kwargs,
    }
    print(f"[DRY-RUN] {operation} {record['args']}")
    return record
