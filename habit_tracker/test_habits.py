import unittest
from management import create_habit, delete_habit, get_all_habits
from analytics import calculate_streak, longest_streak


class TestHabitTracker(unittest.TestCase):

    # Test if a habit is correctly created and stored
    def test_create_habit(self):
        create_habit("test habit", "daily")
        habits = get_all_habits()
        self.assertTrue(any(h.name == "test habit" for h in habits))

    # Test if a habit can be deleted properly
    def test_delete_habit(self):
        create_habit("delete me", "daily")
        delete_habit("delete me")
        habits = get_all_habits()
        self.assertFalse(any(h.name == "delete me" for h in habits))

    # Test streak calculation for at least one habit
    def test_calculate_streak(self):
        habits = get_all_habits()
        self.assertTrue(len(habits) > 0)  # make sure we have data

        streak = calculate_streak(habits[0])
        self.assertTrue(streak >= 0)

    # Test longest streak across all habits
    def test_longest_streak(self):
        habits = get_all_habits()
        result = longest_streak(habits)
        self.assertTrue(result >= 0)


if __name__ == "__main__":
    unittest.main()