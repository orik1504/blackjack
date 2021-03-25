import random


class Player():

    def __init__(self,):
        ''' creating new player start funcs '''
        self.cards = []  # the player cards
        self.money = 1000  # the start cash value for the player
        self.sum = 0  # the player sum of cards

    def drew_card(self):
        ''' The player add a card to his pile '''
        card = Card()
        random_card = card.get_random_card()[0]  # want to get only the number

        # converts the card to 10 if above 10
        random_card = super()._convert_to_ten(random_card)

        # if the card is an Ace the player has the option to change it to 1 or 11
        random_card = super()._one_or_eleven(random_card)

        self.cards.append(random_card)
        self.sum(random_card)

    def bet(self, offer):
        ''' player can make an offer and bet that he will win for doubling his offer back '''
        if self.money >= offer:
            self.money -= offer
        else:
            print(f" you dont have {offer}$ ")

