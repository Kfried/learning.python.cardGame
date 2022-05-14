import random
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(cards)


def draw_cards(number):
    cards_drawn = []
    for draw in range(0, number):
        cards_drawn.append(draw_card())
    return cards_drawn


def deal():
    players = {}
    players["dealer"] = draw_cards(2)
    players["player"] = draw_cards(2)
    return players


def hit(current_set):
    return current_set.append(draw_card())


def current_score(cards_to_score):
    return sum(cards_to_score)


def bust_check(cards):
    if (current_score(cards) > 21):
        return True


def dealer_hit_check(players):
    dealer_value = sum(players['dealer'])
    player_value = sum(players['player'])
    print(f'Dealer has {dealer_value} Player has {player_value}')
    if (dealer_value <= 17):
        return True
    else:
        return False


def dealer_sequence(players):
    if dealer_hit_check(players):
        players['dealer'].append(draw_card())
    return players


def display_cards(players, reveal):
    dealer_displays = " Dealer has :"
    player_displays = " Player has :"
    if (reveal):
        for card in players["dealer"]:
            dealer_displays += f" {card}"
    else:
        dealer_displays += f" {players['dealer'][0]}"
    for card in players['player']:
        player_displays += f" {card}"

    print(f"Cards are : \n{dealer_displays}\n{player_displays}")


def player_wins(players):
    if sum(players['dealer']) >= sum(players['player']):
        return False
    else:
        return True


def got_new_card(old_count, cards):
    if len(cards) > old_count:
        return True
    else:
        return False


def main():
    players = deal()
    display_cards(players, False)
    player_choice = ""
    while True:
        while player_choice.lower() != ('h') and player_choice.lower() != ('s'):
            player_choice = input("Options are to (H)it or (S)tand :")

        if player_choice == 'h':
            print('Hit!')
            players['player'].append(draw_card())
            display_cards(players, False)
            if bust_check(players['player']):
                print(f"You go bust with {sum(players['player'])}")
                break
        else:
            print("Stand")
            dealer_card_count = len(players['dealer'])
            players = dealer_sequence(players)
            while got_new_card(dealer_card_count, players['dealer']):
                print('Dealer Hits')
                if bust_check(players['dealer']):
                    print('Dealer BUSTS')
                    break
                dealer_card_count = len(players['dealer'])
                players = dealer_sequence(players)

            break
        player_choice = ""

    display_cards(players, True)
    did_player_win = player_wins(players) and not bust_check(players['player'])
    if (did_player_win or bust_check(players['dealer'])):
        print("You Win")
    else:
        print("you no win")


main()