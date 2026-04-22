import unittest
import Classes

class testquestion(unittest.TestCase):
    def setUp(self):
        #Reset global score before each test
        Classes.score = 0

    def test_get_points(self):
        question = Classes.Questions(1, "Test", "", "yes", "feedback", 10)
        self.assertEqual(question.getPoints(), 10)

    def test_set_points_valid(self):
        question = Classes.Questions(1, "Test", "", "yes", "feedback", 10)
        question.setPoints(20)
        self.assertEqual(question.getPoints(), 20)

    def test_set_points_if_invalid(self):
        question = Classes.Questions(1, "Test", "", "yes", "feedback", 10)
        question.setPoints(-5)
        self.assertEqual(question.getPoints(), 10)

    def test_add_points(self):
        question = Classes.Questions(1, "Test", "", "yes", "feedback", 10)
        question.addPoints()
        self.assertEqual(Classes.score, 10)

class TestMinigames(unittest.TestCase):

    def setUp(self):
        Classes.score = 0

    def test_minigame_points(self):
        minigame = Classes.Minigames(1, "Test", "", "yes", "feedback")
        minigame.addPoints()
        self.assertEqual(Classes.score, 10)

