from player import Player

class Dealer:
    def __init__(self):
        self.player = Player("Dealer")

    def first_card(self,deck):
        card = deck.deal()
        if card:
            self.player.hand.append(card)
            self.player.calculate_points()

    def calculate_points(self):
        self.player.points = 0
        ace = 0
        for card in self.player.hand:
            self.player.points += card.value
            if card.rank == "ace":
                ace += 1

        while self.player.points > 21 and ace:
            self.player.points -= 10
            ace -= 1

    def turn(self,deck):
        while self.player.points < 17:
            self.player.draw(deck)

    def show_hand(self):
        if len(self.player.hand) > 1:
            output = f"{self.player.hand[0]}, Face down card"
            return output
        elif len(self.player.hand) == 1:
            output = str(self.player.hand[0])
            return output
        return f"No Cards"