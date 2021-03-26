class Game():
    def __init__(self):
        pass

    def _convert_to_ten(self, card):
        ''' Player can't have a card that is more than 13 so every time he gets above 10 the card must convert itself to 10, That is just for getting in statistics'''
        if card > 10:
            return 10
        else:
            return card

    def _one_or_eleven(self, card):
        ''' Player has the option to choose if an Ace that he got will be a "1" or "11" '''
        if card == 1:
            player_answer = int(
                input("Do you want that the ace will be 1 or 11?"))
            if player_answer == 1 or player_answer == 11:
                return player_answer
            else:
                raise ValueError("The value must be 1 or 11!")
        else:
            return card

    def __check_if_21(self, player) -> bool:
        """ if the player got 21 he won automaticly """
        if player.sum_of_cards == 21:
            return True
        return False

