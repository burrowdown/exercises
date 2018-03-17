import unittest
import deck


class TestCardCreation(unittest.TestCase):

    def setUp(self):
        self.king_hearts = deck.Card(13, "hearts")
        self.four_diamonds = deck.Card(4, "diamonds")

    def test_card_creation(self):
        self.assertEqual(self.king_hearts.suit, "hearts")
        self.assertEqual(self.four_diamonds.face, "4")