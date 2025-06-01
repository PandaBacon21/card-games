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

class Card:
    def __init__(self, suit, number):
        self.name = f"{CARD_NUMBERS[number]} of {suit}"
        self.suit = suit
        self.number = number

class CardDeck:
    def __init__(self, card_suits=None, card_numbers=None):
        self.cards = []
        if card_suits == None:
            card_suits = CARD_SUITS
        if card_numbers == None:
            card_numbers = CARD_NUMBERS
        self._build_deck(card_suits, card_numbers)
        
    def _build_deck(self, card_suits, card_numbers):
        for suit in card_suits:
            for number in card_numbers:
                self.cards.append(Card(suit=suit, number=number)) # array of cards to be dealt to players 
        
    def count_cards(self): 
        return len(self.cards)
    
    def add_card(self, card):
        """Add card to cards array - used in game setup"""
        self.cards.append(card)

    def shuffle_deck(self):
        """Shuffle the cards to a random order"""
        random.shuffle(self.cards)
    
    # WAR ONLY - 
    def deal_cards(self, player1, player2):
        """Deal the cards from the Deck.cards array to each Player.cards array, alternating each time"""
        
        # print(f"Starting Deck Count: {len(self.cards)}")
        while len(self.cards) > 0: 
            player1_card = self.cards.pop()
            player1.add_card(player1_card)

            player2_card = self.cards.pop()
            player2.add_card(player2_card)
        print("All cards dealt")
        print("")
        # print(f"Ending Deck Count: {len(self.cards)}")

class BlackJackDeck(CardDeck):
    def __init__(self, num_decks=6):
        self.cards = []
        self.num_decks = num_decks
        for _ in range(self.num_decks):
            self._build_deck(CARD_SUITS, CARD_NUMBERS)
    
    def deal_cards(self, player_array):
        pass