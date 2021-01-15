import random
class Player():
    
    def __init__(self, name,):
        welcome = ("Welcome {}")
        print (welcome.format(name))
        self.player_cards = []
        self.__start()
        self.__sum = 0
        self.__sum_of_cards()
        self.money = 1000
        self.offer = 0
        self.sum_bets = 0

    
    def drew_card(self,):
        self.card = random.randint(1,13)
        if self.card == 1:
            print ("Do you want that card will be 1 or 11?")
            self.card = input()
        self.player_cards.append(self.card)
    
    def __start (self,):
        for i in range(2):
            self.drew_card()
    
    def __sum_of_cards(self,):
        for item in self.player_cards:
            self.__sum+=item

    def bet (self, offer):
        self.money -= offer

    def sum_of_bets(self,):
        self.sum_bets += self.offer

    

    