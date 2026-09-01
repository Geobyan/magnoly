# === Stage 45: Добавь восстановление из резервной копии ===
# Project: StudyCards
def restore_from_backup(backup_path):
    """Восстановить данные из резервной копии JSON."""
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка восстановления: {e}")
        return False

    if not isinstance(data, dict):
        print("Файл резервной копии некорректен.")
        return False

    global cards, themes, stats, settings, user_settings
    cards = data.get('cards', [])
    themes = data.get('themes', [])
    stats = data.get('stats', {})
    settings = data.get('settings', {})
    user_settings = settings.get('user_settings', {})

    print(f"Резервная копия успешно восстановлена ({len(cards)} карточек).")
    return True
