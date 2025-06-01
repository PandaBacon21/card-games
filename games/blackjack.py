from core.players import Player, Dealer
from core.cards import BlackJackDeck

def play_game(name): 
    HumanPlayer = Player(name)
    DealerPlayer = Dealer()
    # num_decks = input("How many decks to play with? Standard is 6: ")
    Deck = BlackJackDeck()
    # print(Deck.count_cards())
    Deck.shuffle_deck()
    for card in Deck.cards:
        print(f"{card.name}")


