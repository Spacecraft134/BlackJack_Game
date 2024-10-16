import random
from game_files.card import Card

class Deck:
    def __init__(self):
        self.random_cards = []
        self.create_deck_list()

    def create_deck_list(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for rank in ranks:
                current_card = Card(rank, suit)
                self.random_cards.append(current_card)

    def deal(self):
        if self.random_cards:
            return self.random_cards.pop()
        else:
            return None

    def shuffle(self):
        random.shuffle(self.random_cards)

