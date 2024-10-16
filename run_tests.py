from tests import TestBlackjackGame

tester = TestBlackjackGame()
tester.test_initial_balance()
tester.test_winner_player_wins()
tester.test_blackjack_player_wins()
tester.test_insurance_bet_loss()

print()
print("All tests completed.")