# from curses import wrapper
from core.utils.menu import game_menu
from games import war, blackjack


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
        # wrapper(game_menu)
        PLAYING = True
        name = input("Enter your name: ")
        while PLAYING == True: 
                game = game_menu(name)
                if game == 0:
                    war.play_game(name)
                elif game == 1:
                    blackjack.play_game(name)
                PLAYING = keep_playing()
                print('')

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt")

if __name__=="__main__":
    main()