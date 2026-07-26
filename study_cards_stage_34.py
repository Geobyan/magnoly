# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: StudyCards
TEMPLATES = {
    "english": {"question": "{{text}}", "answer": "{{meaning}}"},
    "math": {"question": "{{problem}}", "answer": "{{solution}}"},
    "flashcard": {"question": "{{front}}", "answer": "{{back}}"},
}

def get_template(name):
    if name not in TEMPLATES:
        print(f"Unknown template: {name}. Available: {list(TEMPLATES.keys())}")
        return None
    return TEMPLATES[name].copy()

def create_note_from_template(template_name, **fields):
    tpl = get_template(template_name)
    if tpl is None:
        return None
    for key in tpl["question"].split("{{", 1)[1].rsplit("}}", 1)[0]:
        fields[key] = input(f"Enter {key}: ")
    q = tpl["question"].replace("{{text}}", str(fields.get("text", ""))).replace("{{problem}}", str(fields.get("problem", ""))).replace("{{front}}", str(fields.get("front", "")))
    a = tpl["answer"].replace("{{meaning}}", str(fields.get("meaning", ""))).replace("{{solution}}", str(fields.get("solution", ""))).replace("{{back}}", str(fields.get("back", "")))
    return Note(theme=template_name, question=q, answer=a)
