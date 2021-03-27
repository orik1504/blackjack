import random


class Card():

    VALID_SUITS = (
        "hearts",
        "clubs",
        "diamonds",
        "spades",
    )

    __number, __suit = None, None

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):

        if not isinstance(number, int):
            raise TypeError(
                f"Card number must be an integer (not {type(number)})")

        if number > 13 and number > 0:
            raise ValueError(
                f"value can't be {number}, must be between 1 to 13")

        self.__number = number

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, suit):
        if suit not in self.VALID_SUITS:
            raise ValueError("Suit is not valid")

        self.__suit = suit

    def __str__(self,):
        return f"Card({self.number} - {self.suit})"


class CardManager:

    @staticmethod
    def random_card() -> Card:
        number = random.randint(1, 13)
        suit = random.choice(Card.VALID_SUITS)
        return Card(number, suit)


def main():
    x = CardManager.random_card()
    x.suit = "bolbol"
    print(x)


if __name__ == "__main__":
    main()
