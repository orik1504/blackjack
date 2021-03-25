import random


class Card():
    VALID_SUITS = ("hearts",
                   "clubs",
                   "diamonds",
                   "spades", )

    def get_random_card(self,):
        """ Creates a random card object"""
        self.__check_valid_number(random.randint(1, 13))
        self.__check_valid_suit(random.choice(self.VALID_SUITS))
        return self.number, self.suit

    def set_card(self, number: int, suit: str):
        """ Sets a card object """
        self.__check_valid_number(number)
        self.__check_valid_suit(suit)
        return self.number, self.suit

