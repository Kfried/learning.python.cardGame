class Player:

    def __init__(self, name, dealer):
        self.name = name
        self.dealer = dealer
        self.card_total = 0
        self.bust = False
        self.cards = []


    def add_card_to_hand(self, card):
        print(f'adding {card} to {self.cards} for {self.name}') #todo remove
        self.cards.append(card)
        self.add_up_cards()
        self.bust_check()
        if self.bust:
            self.switch_ace()


    def add_up_cards(self):
        self.card_total = sum(self.cards)

    def bust_check(self):
        if self.card_total>21:
            self.bust = True
        else:
            self.bust = False

    def switch_ace(self):
        if 11 in self.cards:
            index = self.cards.index(11)
            self.cards[index] = 1
            self.add_up_cards()
            self.bust_check()

    def display_cards(self, show):
        message = f'{self.name} : '
        for card in self.cards:
            message += f" {card}"
        print(message)