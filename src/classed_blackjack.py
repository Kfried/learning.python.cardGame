from art import logo
from player import Player

import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal(players):
    """deal(dictionary players) adds initial cards to the
    players supplied"""
    for deal_card in range(2):
        player_card = random.choice(cards)
        dealer_card = random.choice(cards)
        players['player'].add_card_to_hand(player_card)
        players['dealer'].add_card_to_hand(dealer_card)
    print (f'The game starts with')
    players['player'].display_cards(True)
    players['dealer'].display_cards(False)
    return players

def get_input(message, validation):
    """get_input(string input_message, list [valid_inputs] asks for inputs with validation values. Returns input"""
    from_user = ''
    while not [element for element in validation if(element in from_user)]:
        from_user = input(message).lower()
    return from_user


def main():
    player = Player('player', False)
    dealer = Player('dealer', True)

    table = {"player": player,
             "dealer": dealer}
    deal(table)



    #hit or stand
    while True:
        user_choice = get_input("(H)it  or  (S)tand :", ['h','s'])
        if user_choice.lower() == 'h':
            print('Hit')
            new_card = random.choice(cards)
            print(f"Player draws {new_card}")
            player.add_card_to_hand(new_card)
            player.display_cards(True)
            if player.bust:
                print(f"You bust with {player.card_total}")
                break
        elif user_choice.lower() == 's':
            print("Player stands.")
            player.display_cards(True)
            break

    #dealer sequence
    while dealer.card_total < 17:
        new_card = random.choice(cards)
        print(f'Dealer draws {new_card}')
        dealer.add_card_to_hand(new_card)
        dealer.display_cards(True)
        if dealer.bust:
            print (f'Dealer went bust with {dealer.card_total}')

    #who won
    player.display_cards(True)
    dealer.display_cards(True)
    if dealer.bust or dealer.card_total < player.card_total:
        print ('You Won ')
    elif player.bust or dealer.card_total >= player.card_total:
        print ('dealer Wins')

main()