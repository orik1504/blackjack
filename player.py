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

    def __one_or_eleven(self, card):
        ''' player has the option to choose if the Ace that he got will be a "1" or "11" '''
        if card == 1:
            player_answer = int(
                input("Do you want that the ace will be 1 or 11?"))
            if player_answer == 1 or player_answer == 11:
                return player_answer
            else:
                raise ValueError("The value must be 1 or 11!")
        else:
            return card

    def __convert_to_ten(self, card):
        ''' Player can't have a card that is more than 13 so every time he gets above 10 the card must convert itself to 10, That is just for getting in statistics'''
        if card > 10:
            return 10
        else:
            return card

    def sum_cards(self, card):
        ''' adds the current card to the sum of the player cards ''' 
        self.sum += card

    def split(self, player_cards: list):
        ''' if the player got the same card value at the start of the round he has the option to split the cards for 2 spareted piles of cards '''
        if self.cards[0] == self.cards[1]:
            player_answer = input(
                "If you want to split the cards for 2 sprate piles?")
            if player_answer == "yes":
                pass
            else:
                pass
