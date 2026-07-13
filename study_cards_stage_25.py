# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: StudyCards
import sys

def parse_date(date_str):
    try:
        if isinstance(date_str, str) and date_str.strip() == '':
            return None
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError('Некорректный формат даты')
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if month < 1 or month > 12:
            raise ValueError('Месяц вне диапазона 1-12')
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days_in_month[1] = 29
        if day < 1 or day > days_in_month[month - 1]:
            raise ValueError('День вне диапазона')
        return (year, month, day)
    except Exception as e:
        print(f'Ошибка: {e}')
        sys.exit(1)

def format_date(year, month, day):
    month_names = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                   'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    return f'{day} {month_names[month - 1]} {year}'
