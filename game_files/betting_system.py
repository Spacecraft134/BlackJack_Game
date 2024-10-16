class Betting:
    def __init__(self):
        self.balance = 100

    def place_bet(self):
        while True:
            print(f"You have ${self.balance:}. Enter your bet: ", end="")
            bet_input = input()

            if not bet_input.isdigit():
                print("Invalid input. Please enter a numeric value.")
                continue

            bet = int(bet_input)

            # Validate the bet amount
            if bet <= 0:
                print("Bet must be greater than zero.")
            elif bet > self.balance:
                print(f"Bet exceeds current balance of ${self.balance:.2f}.")
            else:
                self.balance -= bet
                return bet

    def win_bet(self, bet):
        self.balance += bet * 2
