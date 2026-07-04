# === Stage 20: Добавь восстановление записей из архива ===
# Project: StudyCards
import json, os, shutil, datetime

def restore_from_archive(archive_path: str) -> int | None:
    if not archive_path or not os.path.exists(archive_path):
        return None
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            archived_data = json.load(f)
        timestamp = datetime.datetime.now().isoformat()
        backup_file = f"{archive_path}.restored_{timestamp.replace(':', '_')}"
        shutil.copy2(backup_file if os.path.exists(backup_file) else archive_path, backup_file)
        with open(archive_path, 'w', encoding='utf-8') as f:
            json.dump({**archived_data, "restored_at": timestamp}, f, ensure_ascii=False, indent=4)
        return len(archived_data.get("cards", []))
    except Exception:
        return None
