# -- IMPORTS -- #
from player import Player
from dealer import Dealer

# -- VARIABLES -- #
run = True
temp = input("Enter your name")
name = Player(temp)

name.print_all()

while run:
    answer = name.choice()
    while not answer:
        name.print_all()
        answer = name.choice()
    exit()
