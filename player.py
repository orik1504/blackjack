import random
class Player():
    
    def __init__(self, name,):
        welcome = ("Welcome {}")
        print (welcome.format(name))
        self.cards = []
        self.__start()
        self.sum = 0
        self.sum_of_cards()
        self.money = 1000
        self.offer = 0
        self.sum_bets = 0

    
    def drew_card(self,):
        self.__card = random.randint(1,13)
        if self.__card == 1:
            print ("Do you want that card will be 1 or 11?")
            self.__card = int(input())
        self.cards.append(self.__card)
    
    def __start (self,):
        for i in range(2):
            self.drew_card()
    
    def sum_of_cards(self,):
        for item in self.cards:
            self.sum+=item

    def bet (self, offer):
        self.money -= offer

    def sum_of_bets(self,):
        self.sum_bets += self.offer
    
    


    

    