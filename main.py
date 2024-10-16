import dealer
from dealer import Dealer
from deck import Deck
from player import Player
from betting_system import Betting
from display import GameDisplay
display_logo = GameDisplay()
display_logo.logo()
class Main:
    def __init__(self):

        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(input("Enter your name: "))
        self.dealer = Dealer()
        self.betting = Betting()
        self.display = GameDisplay()
        self.is_test_mode = False

    def winner(self, bet):
        if self.player.points > 21:
            print("You Bust! The dealer wins.")
            self.betting.balance -= bet
        elif self.dealer.player.points > 21:
            print("Dealer busts! You win!")
            self.betting.win_bet(bet)
        elif self.player.points > self.dealer.player.points:
            print("You win!")
            self.betting.win_bet(bet)
        elif self.player.points < self.dealer.player.points:
            print("Dealer wins!")
            self.betting.balance -= bet
        else:
            print("It's a tie! You get your bet back.")
            self.betting.balance += bet


    def check_blackjack(self, bet):
        if self.player.points == 21:
            if self.dealer.player.points == 21:
                print("\nBoth you and the dealer have Blackjack! It's a tie!")
                self.betting.balance += bet
            else:
                print("\nYou have Blackjack! You win!")
                self.betting.balance += bet * 1.5
            return True
        elif self.dealer.player.points == 21:
            print("\nDealer has Blackjack! Dealer wins!")
            self.betting.balance -= bet
            return True
        return False

    def insurance(self, bet):
        if self.dealer.player.hand[0].rank == "Ace":
            print("Dealer's face-up card is an Ace.")

            if self.is_test_mode:
                insurance_bet = 'yes'
            else:
                insurance_bet = input(
                    "Do you want to place an insurance bet (up to half of your original bet)? (yes/no): ").strip().lower()

            if insurance_bet == 'yes':
                insurance_amount = min(bet / 2, self.betting.balance / 2)

                if self.dealer.player.points == 21:
                    print("Dealer has Blackjack! You win the insurance bet.")
                    self.betting.balance += 2 * insurance_amount
                else:
                    print("Dealer does not have Blackjack. You lose the insurance bet.")
                    self.betting.balance -= insurance_amount


    def play_another_round(self):
        while True:
            play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
            if play_again == "no":
                print("Thanks for playing!")
                return False
            elif play_again == "yes":
                return True
            else:
                print("Please enter a valid response (Yes or No).")

    def game(self):
        while True:
            if self.betting.balance <= 0:
                print("You don't have enough money. Game Over!")
                return

            bet = self.betting.place_bet()
            self.player.hand.clear()
            self.player.points = 0
            self.player.aces = 0
            self.dealer.player.hand.clear()
            self.dealer.player.points = 0
            self.dealer.player.aces = 0

            for _ in range(2):
                self.player.draw(self.deck)
                self.dealer.player.draw(self.deck)

            # Display the game table with ASCII cards
            self.display.print_table(self.player, self.dealer)

            self.insurance(bet)

            if self.check_blackjack(bet):
                continue

            surrender_choice = input("Do you want to surrender? (yes/no): ").strip().lower()
            if surrender_choice == "yes":
                loss = bet / 2
                self.betting.balance += loss
                print(
                    f"You chose to surrender. You lose half your bet. Your balance is now: ${self.betting.balance}")
                if not self.play_another_round():
                    return
                continue
            elif surrender_choice != "no":
                print("please enter a valid choice")


            while self.player.points < 21:
                turn = input("Do you want to hit or stand? ").lower()
                if turn == "hit":
                    self.player.draw(self.deck)
                    self.display.print_table(self.player, self.dealer)  # Show updated player hand
                elif turn == "stand":
                    break
                else:
                    print("Invalid input. Please enter 'hit' or 'stand'.")
                    
            if self.player.points > 21:
                print(f"You bust with {self.player.points}. Dealer wins.")
                self.betting.balance -= bet  # Deduct the bet for bust
                print(f"Your balance is now: ${self.betting.balance:.2f}")
            else:
                self.dealer.turn(self.deck)
                print(f"Dealer's final hand: {self.dealer.player.show_hand()}, "
                      f"Total Points: {self.dealer.player.points}")

                print("\nFinal hands:")
                self.display.print_table(self.player, self.dealer)  # Display final hands
                self.winner(bet)
                print(f"Your current balance: ${self.betting.balance:.2f}")

            if not self.play_another_round():
                return

            # Reshuffle if deck is low
            if len(self.deck.random_cards) < 10:
                print("Reshuffling")
                self.deck = Deck()
                self.deck.shuffle()