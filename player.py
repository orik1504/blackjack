import random


class Player():

    def __init__(self, name,):
        welcome = ("Welcome {}")
        print(welcome.format(name))
        self.cards = []
        self.sum = 0
        self.money = 1000
        self.offer = 0
        self.sum_bets = 0
        self.__start()

    def drew_card(self,):
        self.__card = random.randint(1, 13)
        self.turn_13_to_10()
        self.one_or_eleven()
        self.sum_of_cards()

    def one_or_eleven(self,):
        if self.__card == 1:
            print("Do you want that card will be 1 or 11?")
            self.__card = int(input())
        self.cards.append(self.__card)

    def turn_13_to_10(self):
        if self.__card > 10:
            self.__card = 10

    def __start(self,):
        for i in range(2):
            self.drew_card()

    def sum_of_cards(self,):
        self.sum += self.__card

    def bet(self, offer):
        self.money -= int(offer)

    def sum_of_bets(self,):
        self.sum_bets += self.offer

    def choice(self,):
        print("What is your play: \n 1.drew card \n 2.bet")
        self.user_input = input()
        if self.user_input == "1":
            self.drew_card()
        else:
            offer = input("What is your offer?")
            self.bet(offer)
