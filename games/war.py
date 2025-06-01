from core.players import Player
from core.cards import CardDeck

# What happens if the players last card is A? It can only be beat by WAR but it doesn't have enough cards to keep playing...


def resolve_war(Player1, Player2, card_pot): 
        print("STARTING WAR")
        input("Press Enter to flip your card: ")
        print('')
        player1_burn = Player1.play_card()
        player1_card = Player1.play_card()
        player2_burn = Player2.play_card()
        player2_card = Player2.play_card()
        current_card_pot = [player1_burn, player2_burn, player2_card, player1_card] + card_pot
        print('')
        print(f"card pot in the war: {len(current_card_pot)}")
        print('')
        print(f"{Player1.name}'s card: {player1_card.name}")
        print(f"{Player2.name}'s card: {player2_card.name}")

        if player1_card.number > player2_card.number: 
            print(f"{Player1.name} WINS the hand and wins {len(current_card_pot)} cards")
            Player1.cards = current_card_pot + Player1.cards
            Player1.increment_hands_won()
            print('')
        elif player1_card.number < player2_card.number: 
            print(f"{Player2.name} WINS the hand and wins {len(current_card_pot)} cards")
            Player2.cards = current_card_pot + Player2.cards
            Player2.increment_hands_won()
            print('')
        else: 
            print("Number are the same, go to WAR!")
            print('')
            resolve_war(Player1, Player2, card_pot=current_card_pot)

        # Need to handle this 
        
def play_game(name):
    Player1 = Player(name)
    Player2 = Player("Computer")
    Deck = CardDeck()
    print('')
    print(f"Starting deck size: {Deck.count_cards()} cards")

    print("Shuffling Deck")
    Deck.shuffle_deck()
    Deck.shuffle_deck()

    print("Dealing cards to players")
    Deck.deal_cards(Player1, Player2)
    print(f"Ending deck size: {Deck.count_cards()} cards")
    print('')
    total_hands = 0
    try: 
        while (len(Player1.cards) > 0) or (len(Player2.cards) > 0):
            print("NEW HAND: ")
            input("Press Enter to flip your card: ")
            print('')
            

            player1_card = Player1.play_card()
            player2_card = Player2.play_card()
            current_card_pot = [player1_card, player2_card]
            print(f"card pot size: {len(current_card_pot)}")
            print('')

            print(f"{Player1.name}'s card: {player1_card.name}")
            print(f"{Player2.name}'s card: {player2_card.name}")
            if player1_card.number > player2_card.number: 
                print(f"{Player1.name} WINS the hand and wins {len(current_card_pot)} cards")
                Player1.cards = current_card_pot + Player1.cards
                Player1.increment_hands_won()
                print('')
                if ((len(Player1.cards) == 52) or (len(Player2.cards) == 0)) or ((len(Player2.cards) == 52) or (len(Player1.cards) == 0)):
                    break
            elif player1_card.number < player2_card.number: 
                print(f"{Player2.name} WINS the hand and wins {len(current_card_pot)} cards")
                Player2.cards = current_card_pot + Player2.cards
                Player2.increment_hands_won()
                print('')
                if ((len(Player1.cards) == 52) or (len(Player2.cards) == 0)) or ((len(Player2.cards) == 52) or (len(Player1.cards) == 0)):
                    break
            else: 
                print("Number are the same, go to WAR!")
                print('')
                try: 
                    resolve_war(Player1, Player2, card_pot=current_card_pot)
                except IndexError:
                    if len(Player1.cards) <= 1: 
                        print(f"{Player1.name} ran out of cards during the war, since they can't keep playing, they lose.")
                        break
                    elif len(Player2.cards) <= 1:
                        print(f"{Player2.name} ran out of cards during the war, since they can't keep playing, they lose.")
                        break

            total_hands += 1
            print(f"{Player1.name} has {len(Player1.cards)} cards")
            print(f"{Player2.name} has {len(Player2.cards)} cards")

        if (len(Player1.cards) == 52) or (len(Player2.cards) <= 1):
            print(f"{Player1.name} wins the game!")
        elif (len(Player2.cards) == 52) or (len(Player1.cards) <= 1):
            print(f"{Player2.name} wins the game!")
        else: 
            print("something broke the game loop before a winner")

        print(f"{Player1.name} hands won: {Player1.hands_won}")
        print(f"{Player2.name} hands won: {Player2.hands_won}")
        print(f"Total Hands: {total_hands}")
        print('')

    except KeyboardInterrupt: 
            print("\nKeyboard Interrupt")
            print("Game Ended Manually")
