import random
class Dealer():

    cards = []
    sum = 0
 
    @classmethod
    def drew_card(cls,):
        card = random.randint(1,13)
        cls.cards.append(card)
    
    @classmethod
    def sum_of_cards(cls):
        for item in cls.cards:
            cls.sum += item
    
    @classmethod
    def drew_and_sum(cls,):
        cls.drew_card()
        cls.sum_of_cards()
    
    
    
    