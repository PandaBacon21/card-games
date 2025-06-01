
# Add Menu - Will add multiple games, like War, Texas Hold'em, BlackJack

# def game_menu(stdscr): 
#     stdscr.clear()

def game_menu(name): 
    print(f"Welcome to Card Games, {name}!")
    print("Which game do you want to play?")
    game = input("(0) War, (1) Blackjack: ")
    return int(game) 