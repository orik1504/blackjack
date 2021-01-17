import random


class Player():

    def __init__(self, name,):
        print(f"Welcome {name}")
        self.cards = []
        self.sum = 0
        self.money = 1000
        self.offer = 0
        self.sum_bets = 0
        self.__start()

    def drew_card(self,):
        self.__card = random.randint(1, 13)
        self.__turn_13_to_10()
        self.__one_or_eleven()
        self.__sum_of_cards()

    def __one_or_eleven(self,):
        if self.__card == 1:
            print("Do you want that card will be 1 or 11?")
            self.__card = int(input())
        self.cards.append(self.__card)

    def __turn_13_to_10(self):
        if self.__card > 10:
            self.__card = 10

    def __start(self,):
        for i in range(2):
            self.drew_card()

    def __sum_of_cards(self,):
        while self.money > 0:
            self.sum += self.__card

    def bet(self, offer):
        if self.money > 0:
            self.money -= int(offer)
        print("You can't bet, you have 0 dollars")

    def sum_of_bets(self,):
        self.sum_bets += self.offer

    def choice(self,):
        print("What is your play: \n 1.drew card \n 2.bet \n 3.Nothing")
        self.user_input = input()
        if self.user_input == "1":
            self.drew_card()
        elif self.user_input == "2":
            offer = input("What is your offer?")
            self.bet(offer)
        else:
            None

    def print_all(self,):
        print(f"Your cards are:{self.cards}",
              f"Your sum of bets is:{self.sum_bets}", f"You have {self.money} dollars")
