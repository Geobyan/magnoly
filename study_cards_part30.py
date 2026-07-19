# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: StudyCards
import json, os

PROFILES_DIR = "profiles.json"

def load_profiles():
    if not os.path.exists(PROFILES_DIR):
        return [{"name": "Гость", "cards": [], "stats": {"total_reviewed": 0}}]
    with open(PROFILES_DIR) as f:
        raw = json.load(f)
    # ensure every profile has a stats dict (backward compat)
    for p in raw:
        if "stats" not in p:
            p["stats"] = {"total_reviewed": 0}
    return raw

def save_profiles(profiles):
    with open(PROFILES_DIR, "w") as f:
        json.dump(profiles, f)

# ---- add_profile() ----
def add_profile(name="Гость"):
    profiles = load_profiles()
    for p in profiles:
        if p["name"].lower() == name.lower():
            return p  # already exists
    profiles.append({"name": name, "cards": [], "stats": {"total_reviewed": 0}})
    save_profiles(profiles)
    print(f"Профиль '{name}' создан.")

# ---- switch_profile() ----
def switch_profile(name):
    profiles = load_profiles()
    for p in profiles:
        if p["name"].lower() == name.lower():
            return p
    print(f"Профиль '{name}' не найден. Доступные: {', '.join(p['name'] for p in profiles)}")
    return None

# ---- get_current_profile() ----
current_profile = {"name": "Гость", "cards": [], "stats": {"total_reviewed": 0}}

def get_current_profile():
    global current_profile
    if not os.path.exists(PROFILES_DIR):
        profiles = [{"name": "Гость", "cards": [], "stats": {"total_reviewed": 0}}]
        save_profiles(profiles)
    else:
        with open(PROFILES_DIR) as f:
            profiles = json.load(f)
            if not profiles or not any(p["name"].lower() == current_profile["name"].lower() for p in profiles):
                # fallback to default
                save_profiles([{"name": "Гость", "cards": [], "stats": {"total_reviewed": 0}}])
                return load_profiles()[0]
    return current_profile

def set_current_profile(profile):
    global current_profile
    current_profile = profile
