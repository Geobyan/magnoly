# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: StudyCards
class ProfileManager:
    def __init__(self, storage):
        self.storage = storage
        self.active_profile = None
        if not self.storage.profiles:
            self.add_default()

    def add_default(self):
        default_id = len(self.storage.profiles) + 1
        profile = {
            'id': default_id,
            'name': 'Дефолтный',
            'stats': {'total_cards': 0, 'reviews_done': 0},
            'settings': {}
        }
        self.storage.profiles[default_id] = profile
        self.active_profile = default_id

    def switch(self, profile_name):
        for pid, p in self.storage.profiles.items():
            if p['name'] == profile_name:
                self.active_profile = pid
                return True
        print(f"Профиль '{profile_name}' не найден")
        return False

    def get_active(self):
        if not self.active_profile:
            self.add_default()
        return self.storage.profiles[self.active_profile]

    def list_profiles(self):
        return {pid: p['name'] for pid, p in self.storage.profiles.items()}
