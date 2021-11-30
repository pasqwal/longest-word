import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_valid_empty_word(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_valid_word(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('EUREKA'), True)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched

    def test_invalid_word(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('COBRA'), False)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched
