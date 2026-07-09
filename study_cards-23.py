# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: StudyCards
def print_table(headers, rows):
    """Compact console table printer."""
    widths = [max(len(str(h)), max((len(str(r[i])) for r in rows), default=0)) for i, h in enumerate(headers)]
    header_line = " | ".join(f"{h:<{widths[i]}}" for i, h in enumerate(headers))
    sep_line = "-+-".join("-" * w for w in widths)
    print(header_line)
    print(sep_line)
    row_lines = [" | ".join(str(r[i]).ljust(widths[i]) if r else "-" * widths[i] for i, _ in enumerate(headers)) for r in rows]
    print("\n".join(row_lines))

# Example usage:
print_table(["Topic", "Cards", "Accuracy"], [["Math", 50, "87%"], ["History", 30, "92%"]])
