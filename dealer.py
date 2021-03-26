import random
from main_game import Game


class Dealer(Game):  # a computer that doing random stuff

    def __init__(self,):
        self.cards = []  # the dealer cards
        self.sum_of_cards = 0  # the sum of the dealers cards
        self.name = "dealer"

    def draw_card(self):
        """ dealer can  draw a card while his pile sum is not above 17 """
        if self.sum_of_cards <= 17:
            card = Card()
            # want to get only the number
            random_card = card.get_random_card()[0]

            # converts the card to 10 if above 10
            random_card = super()._convert_to_ten(random_card)

            # if the card is an Ace the player has the option to change it to 1 or 11
            random_card = self._one_or_eleven(random_card)

            self.cards.append(random_card)
            self.sum(random_card)

    def sum(self, card_number):
        """ calculates the sum of the dealer cards """
        self.sum_of_cards += card_number

    @staticmethod
    def _one_or_eleven(card):
        choices = (1, 11)
        if card == 1:
            return random.choice(choices)
        return card
