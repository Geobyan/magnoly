# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: StudyCards
def demo_commands():
    print("=== StudyCards Demo ===")
    for cmd in [
        "add_card('Python', 'print() выводит текст')",
        "add_card('JS', 'console.log() выводит в консоль')",
        "add_card('Java', 'System.out.println() выводит строку')",
        "add_theme('Frontend', ['Python', 'JS'])",
        "add_theme('Backend', ['Python', 'Java'])",
    ]:
        print(f"> {cmd}")

demo_commands()
