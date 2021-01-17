# -- IMPORTS -- #
from player import Player
from dealer import Dealer

# -- VARIABLES -- #
run = True
temp = input("Enter your name")
name = Player(temp)

while run:
    name.print_all()
    name.choice()
    name.print_all()
