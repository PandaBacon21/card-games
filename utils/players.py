class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []# array of cards to be played
        self.hands_won = 0

    def add_card(self, card):
        """function to add card to player's cards array"""
        self.cards.append(card)
  
    def play_card(self):
        card = self.cards.pop()
        return card
    
    def increment_hands_won(self):
        self.hands_won += 1
