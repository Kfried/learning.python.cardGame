from art import logo
from player import Player

import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal(players):
    for deal_card in range(2):
        player_card = random.choice(cards)
        dealer_card = random.choice(cards)
        print(f'Dealer draws {dealer_card} Player draws {player_card}')
        players['player'].add_card_to_hand(player_card)
        players['dealer'].add_card_to_hand(dealer_card)
    return players

def get_input(message, validation):
    from_user = ''
    while not [element for element in validation if(element in from_user)]:
        from_user = input(message).lower()


def main():
    player = Player('player', False)
    dealer = Player('dealer', True)

    table = {"player": player,
             "dealer": dealer}
    deal(table)

    #hit or stand
    user_choice = get_input("(H)it  or  (S)tand", ['h','s'])
    print(user_choice)

    #dealer sequence

    #who won


    for k in table:
        table[k].display_cards(False)

main()