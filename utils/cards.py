import random

CARD_SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

CARD_NUMBERS = {
        1: '2',
        2: '3',
        3: '4',
        4: '5',
        5: '6',
        6: '7',
        7: '8',
        8: '9',
        9: '10',
        10: 'J',
        11: 'Q',
        12: 'K',
        13: 'A'
    }

class Card():
    def __init__(self, suit, number):
        self.name = f"{CARD_NUMBERS[number]} of {suit}"
        self.suit = suit
        self.number = number

class CardDeck():
    def __init__(self, card_suits=CARD_SUITS, card_numbers=CARD_NUMBERS):
        self.cards = []
        for suit in card_suits:
            for k,_ in card_numbers.items():
                self.cards.append(Card(suit=suit, number=k)) # array of cards to be dealt to players 
        
    def add_card(self, Card):
        """Add card to cards array - used in game setup"""
        self.cards.append(Card)

    def shuffle_deck(self):
        """Shuffle the cards to a random order"""
        random.shuffle(self.cards)
    
    def deal_cards(self, Player1, Player2):
        """Deal the cards from the Deck.cards array to each Player.cards array, alternating each time"""
        
        # print(f"Starting Deck Count: {len(self.cards)}")
        while len(self.cards) > 0: 
            player1_card = self.cards.pop()
            Player1.add_card(player1_card)

            player2_card = self.cards.pop()
            Player2.add_card(player2_card)
        print("All cards dealt")
        print("")
        # print(f"Ending Deck Count: {len(self.cards)}")