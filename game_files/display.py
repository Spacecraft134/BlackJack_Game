class GameDisplay:

    def logo(self):
        logo = r"""
                .------.            _     _            _    _            _    
                |A_  _ |.          | |   | |          | |  (_)          | |   
                |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
                | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
                |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
                `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
                      |  \/ K|                            _/ |                
                      `------'                           |__/           
                """
        print(logo)


    def print_card(self, card):
        suits = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }

        rank = card.rank if card.rank != '10' else '10'
        suit = suits[card.suit]

        return f'''
            +-------+
            | {rank:<6} |
            |       {suit} |
            |         |
            |       {suit} |
            | {rank:>6} |
            +-------+
                '''

    def print_facedown_card(self):
        return '''
            +-------+
            |       |
            |       |
            |       |
            |       |
            |       |
            +-------+
                '''

    def print_table(self, player, dealer):
        print(f"\nDealer's Hand: {dealer.show_hand()}")
        print("Dealer's Cards:")
        if dealer.player.hand:
            print(self.print_card(dealer.player.hand[0]))
            print(self.print_facedown_card())

        print(f"\nYour Hand: {player.show_hand()}, Total points: {player.points}")
        print("Your Cards:")
        for card in player.hand:
            print(self.print_card(card))
