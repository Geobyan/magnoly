# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: StudyCards
import sys

def colorize(text, color):
    """Выводит текст с цветом ANSI, если терминал поддерживает."""
    if sys.stdout.isatty():
        codes = {
            'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m',
            'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m',
            'white': '\033[37m', 'bold': '\033[1m', 'reset': '\033[0m',
        }
        start = codes.get(color, '')
        end = '\033[0m' if color != 'bold' else '\033[22m'
        return f"{start}{text}{end}"
    return text

def print_colored(msg, color):
    print(colorize(msg, color))
