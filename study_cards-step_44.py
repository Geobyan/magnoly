# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: StudyCards
import os, shutil, datetime
def backup_data_file(data_path, backup_dir="backups"):
    if not os.path.exists(data_path):
        return
    os.makedirs(backup_dir, exist_ok=True)
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"data_{now}.bak")
    shutil.copy2(data_path, backup_path)
    print(f"Backed up to {backup_path}")
