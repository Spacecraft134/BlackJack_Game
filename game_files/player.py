class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.hand = []
        self.points = 0
        self.aces = 0

    def calculate_points(self):
        self.points = 0
        self.aces = 0
        for card in self.hand:
            self.points += card.value
            if card.rank == "Ace":
                self.aces += 1

        while self.points > 21 and self.aces > 0:
            self.points -= 10
            self.aces -= 1

    def draw(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)
            self.calculate_points()
        return card

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)

    def __str__(self):
        return f"{self.player_name} has {self.show_hand()} with a score of {self.points}"
