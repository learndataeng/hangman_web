"""Unit test cases for hangman game."""
import unittest
import app as hangman


class HangmanTestCase(unittest.TestCase):

    # def setUp(self):
    #

    # checkCorrectAnswer(correctLetters, secretWord)
    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer("baon", "baboon")
        self.assertTrue(answer)

    def test_checkWrongAnswer(self):
        answer = hangman.checkWrongAnswer("zebrio", "zebra")
        self.assertTrue(answer)

    def test_1(self):
        answer = hangman.checkCorrectAnswer("bazn", "baboon")
        self.assertFalse(answer)

    def test_2(self):
        answer = hangman.checkCorrectAnswer("", " ")
        self.assertFalse(answer)

    def test_3(self):
        answer = hangman.checkCorrectAnswer("ZEBRA", "zebra")
        self.assertFalse(answer)


if __name__ == "__main__":
    unittest.main()
