class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.assign_values()

    def assign_values(self):
        if self.rank in ["King", "Queen", "Jack"]:
            return 10
        elif self.rank == "Ace":
            # adjusted in player class
            return 11
        else:
            return int(self.rank)


    def __str__(self):
        return f"{self.rank} of {self.suit}"
