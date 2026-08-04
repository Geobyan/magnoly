# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: StudyCards
import argparse

def main():
    parser = argparse.ArgumentParser(description="StudyCards CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # create
    p_create = subparsers.add_parser("create", help="Создать новую карточку")
    p_create.add_argument("--term", type=str, required=True)
    p_create.add_argument("--definition", type=str, required=True)
    p_create.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="medium")

    # review
    p_review = subparsers.add_parser("review", help="Пересмотреть карточку по ID")
    p_review.add_argument("card_id", type=int)

    # stats
    p_stats = subparsers.add_parser("stats", help="Показать статистику")

    args = parser.parse_args()

    if args.command == "create":
        card = Card(args.term, args.definition, args.difficulty)
        cards.append(card)
        print(f"Карточка создана: {card.id}")
    elif args.command == "review":
        card = find_card_by_id(cards, args.card_id)
        if card is None:
            print("Ошибка: карточка не найдена")
        else:
            result = input("Вы знаете ответ? (да/нет): ").strip().lower()
            if result == "да":
                card.successful += 1
            else:
                card.failed += 1
                card.next_review = datetime.now() + timedelta(days=3)
            print(f"Результат записан для карточки {card.id}")
    elif args.command == "stats":
        if not cards:
            print("Нет данных для статистики")
        else:
            total_reviews = sum(c.successful + c.failed for c in cards)
            successful_rate = (sum(c.successful for c in cards) / total_reviews * 100) if total_reviews > 0 else 0
            print(f"Всего карточек: {len(cards)}")
            print(f"Общие ответы: {total_reviews}")
            print(f"Процент успешных: {successful_rate:.1f}%")

if __name__ == "__main__":
    main()
