import random
from main_game import Game


class Dealer(Game):  # a computer that doing random stuff

    cards = []
    sum = 0

    @classmethod
    def drew_card(cls,):
        card = random.randint(1, 13)
        if card > 10:
            card = 10
        cls.cards.append(card)
        cls.sum_of_cards(card)

    @classmethod
    def sum_of_cards(cls, card):
        cls.sum += card
