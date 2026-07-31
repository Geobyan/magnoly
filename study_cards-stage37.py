# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: StudyCards
import unittest


class TestStudyCards(unittest.TestCase):
    def test_add_card(self):
        app = StudyCards()
        card = {"front": "capital", "back": "Paris"}
        self.assertEqual(len(app.cards), 0)
        app.add_card(card)
        self.assertEqual(len(app.cards), 1)

    def test_find_by_id(self):
        app = StudyCards()
        card = {"id": 42, "front": "A", "back": "B"}
        app.add_card(card)
        found = app.find_card(42)
        self.assertEqual(found["back"], "B")

    def test_find_not_exists(self):
        app = StudyCards()
        card = {"id": 7, "front": "X", "back": "Y"}
        app.add_card(card)
        result = app.find_card(99)
        self.assertIsNone(result)

    def test_get_stats_empty(self):
        app = StudyCards()
        stats = app.get_stats()
        self.assertEqual(stats["total_cards"], 0)
        self.assertEqual(stats["learned_cards"], 0)

    def test_get_stats_after_study(self):
        app = StudyCards()
        card = {"id": 1, "front": "Q", "back": "A"}
        app.add_card(card)
        app.study_card(1)
        stats = app.get_stats()
        self.assertEqual(stats["total_cards"], 1)
        self.assertEqual(stats["learned_cards"], 1)

    def test_get_stats_after_fail(self):
        app = StudyCards()
        card = {"id": 3, "front": "Q", "back": "A"}
        app.add_card(card)
        app.study_card(3)
        self.assertEqual(app.get_stats()["learned_cards"], 0)

    def test_get_learned(self):
        app = StudyCards()
        card = {"id": 5, "front": "Q", "back": "A"}
        app.add_card(card)
        app.study_card(5)
        self.assertIn("cards", app.get_learned())

    def test_get_unlearned(self):
        app = StudyCards()
        card = {"id": 8, "front": "Q", "back": "A"}
        app.add_card(card)
        self.assertIn("cards", app.get_unlearned())


if __name__ == "__main__":
    unittest.main()
