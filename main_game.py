# -- IMPORTS -- #
from player import Player
from dealer import Dealer

    def _convert_to_ten(self, card):
        ''' Player can't have a card that is more than 13 so every time he gets above 10 the card must convert itself to 10, That is just for getting in statistics'''
        if card > 10:
            return 10
        else:
            return card

name.print_all()

while run:
    answer = name.choice()
    while not answer:
        name.print_all()
        answer = name.choice()
    exit()
