# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: StudyCards
def get_usage_scenarios(self):
        """Returns a list of documented use-case scenarios for StudyCards."""
        return [
            {
                "name": "Quick Review",
                "description": (
                    "User starts the app and immediately begins reviewing flashcards. "
                    "Each card is shown one at a time; user rates their recall as Correct, "
                    "Mostly Correct, or Incorrect. Based on the rating, StudyCards schedules "
                    "the next review using spaced repetition: easy cards appear later, "
                    "hard ones sooner."
                ),
            },
            {
                "name": "Add Cards with Themes",
                "description": (
                    "User creates a new theme (e.g., 'Python Basics', 'Spanish Verbs'). "
                    "Inside the theme they add cards by typing front and back text. "
                    "Cards are automatically grouped into their parent theme for organized learning."
                ),
            },
            {
                "name": "Theme-Based Quizzes",
                "description": (
                    "User selects a specific theme and requests a quiz. StudyCards pulls all cards "
                    "from the chosen theme, shuffles them, and presents them in quiz mode where "
                    "the user answers without hints. After each answer, immediate feedback is shown."
                ),
            },
            {
                "name": "Statistics Dashboard",
                "description": (
                    "User navigates to the stats screen to see overall progress: total cards created, "
                    "cards reviewed today, average accuracy percentage, and a breakdown of reviews per theme. "
                    "This helps identify weak areas needing more practice."
                ),
            },
            {
                "name": "Custom Scheduling",
                "description": (
                    "User can adjust the interval multipliers for spaced repetition intervals 1-5, "
                    "tailoring how quickly cards are re-presented based on their personal learning pace. "
                    "This allows advanced users to fine-tune the algorithm."
                ),
            },
        ]
