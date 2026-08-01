# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: StudyCards
def test_edge_cases(self):
        self.assertEqual(App.study(1, 0), "Неизвестно")
        self.assertEqual(App.study(-1, 0), "Неизвестно")
        self.assertEqual(App.study(5, -3), "Никогда не отвечал на вопрос")

        self.assertFalse(App.is_answered(2))
        self.assertTrue(App.is_answered(2, True))
        self.assertFalse(App.is_correct(2, False))
        self.assertTrue(App.is_correct(2, True))

        App.save_all()
        self.assertEqual(len(App.get_cards()), 0)
        App.load_all()
        self.assertEqual(len(App.get_cards()), 0)
        self.assertEqual(App.cards(), [])
        self.assertEqual(App.next_card_num(), None)
