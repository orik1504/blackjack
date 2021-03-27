import random
from main_game import Game
from card import *


class Player(Game):

    def __init__(self, name):
        self.cards = list()  # the player cards
        self.money = 1000  # the start cash value for the player
        self.name = name

    def draw_card(self):
        ''' The player add a card to his pile '''
        card = CardManager.random_card()
        self.cards.append(BlackJackCard(card))

    def bet(self, offer):
        ''' Player can make an offer and bet that he will win for doubling his offer back '''
        if self.money >= offer:
            self.money -= offer
        else:
            print(f" you dont have {offer}$ ")

    def get_sum(self,):

        return sum([
            card.card_value
            for card in self.cards
        ])
