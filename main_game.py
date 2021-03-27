class Game():

    winner = None

    def __init__(self):
        pass

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

    def _split(self, player_start_cards):
        """ if the player got 2 of the same card (card number) he can split the piles
        to 2 separated piles """
        pass

    def __check_if_21(self, player) -> bool:
        """ if the player got 21 he won automaticly """
        if player.sum_of_cards == 21:
            return True
        return False

    def __higher(self, player, dealer):
        """ checks who got the higher score """
        # TODO: want to get instance of those classes
        if player.sum_of_cards > dealer.sum_of_cards:
            return player.name

        elif player.sum_of_cards < dealer.sum_of_cards:
            return dealer.name

        else:
            return "draw"

    def check_winner(self, player, dealer):
        """ returns the winner of the round """
        if self.__check_if_21(player):
            self.winner = player.name

        if self.__check_if_21(dealer):
            self.winner = dealer.name

        self.winner = self.__higher(player, dealer)

    def is_winner(self):
        """ checks if there is a winner """
        if self.winner is not None:
            return True
        return False
