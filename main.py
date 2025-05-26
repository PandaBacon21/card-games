from curses import wrapper
from utils.cards import CardDeck
from utils.players import Player
from games import war

# Add Menu - Will add multiple games, like War, Texas Hold'em, BlackJack
def game_menu(stdscr): 
    stdscr.clear()

def keep_playing():
    while True: 
        play_again = input("Do you want to play again? (1) for Yes, (0) for No: ")

        if play_again == '0':
            return False
        elif play_again == '1':
            return True
        else:
            print("Not a valid input.")
            
def main():
    try:
        wrapper(game_menu)

        PLAYING = True
        name = input("Enter your name: ")
        while PLAYING == True: 
                HumanPlayer = Player(name)
                ComputerPlayer = Player("Computer")
                Deck = CardDeck()

                print('Shuffling Deck')
                Deck.shuffle_deck()
                Deck.shuffle_deck()

                print("Dealing cards to players")
                Deck.deal_cards(HumanPlayer, ComputerPlayer)
                war.play_game(HumanPlayer, ComputerPlayer)

                PLAYING = keep_playing()

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt")

if __name__=="__main__":
    main()