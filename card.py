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


class BlackJackCard():

    def __init__(self, card: Card):
        self.card = card
        self.card_value = self.__generate_card_value(card)

    @staticmethod
    def __generate_card_value(card: Card) -> int:
        """ Recives a card instance and returns its value. """

        if card.number > 10:
            return 10

        if card.number == 1:
            return BlackJackCard.__ace_card_value()

        return card.number

    @staticmethod
    def __ace_card_value():
        VALID_ANSWERS = (1, 11)
        player_input = input("What do you want the card to be, 1 or 11")
        if player_input not in VALID_ANSWERS:
            raise ValueError(
                f" Value can't be {player_input}, must be 1 or 11")
        return player_input


def main():
    x = CardManager.random_card()
    x.suit = "bolbol"
    print(x)


if __name__ == "__main__":
    main()
