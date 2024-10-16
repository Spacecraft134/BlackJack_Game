from card import Card
from main import Main

class TestBlackjackGame:
    def __init__(self):
        self.game = Main()
        self.game.is_test_mode = True

    def test_initial_balance(self):
        if self.game.betting.balance == 100:
            print("Initial balance test passed.")
        else:
            print("Initial balance should be 100.")

    def test_winner_player_wins(self):
        self.game.betting.balance = 100
        self.game.player.points = 20
        self.game.dealer.player.points = 18
        initial_balance = self.game.betting.balance

        self.game.winner(10)

        if self.game.betting.balance == initial_balance + 20:
            print("Player wins test passed.")
        else:
            print(f"Player should win the bet. Current balance: {self.game.betting.balance}")

    def test_blackjack_player_wins(self):
        # Reset balance and state
        self.game.betting.balance = 100
        self.game.player.points = 21
        self.game.dealer.player.points = 18
        initial_balance = self.game.betting.balance

        if self.game.check_blackjack(10):
            if self.game.betting.balance == initial_balance + 15:
                print("Blackjack win test passed.")
            else:
                print(f"Balance should reflect win from blackjack. Current balance: {self.game.betting.balance}")
        else:
            print("Player should have blackjack and win.")

    def test_insurance_bet_loss(self):
        self.game.betting.balance = 100
        self.game.dealer.player.hand = [Card('Ace', 'Spades'), Card('5', 'Hearts')]
        self.game.player.points = 20

        self.game.insurance(20)

        if self.game.betting.balance == 90:
            print("Insurance bet loss test passed.")
        else:
            print(f"Player should lose the insurance bet. Current balance: {self.game.betting.balance}")
