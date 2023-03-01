# -*- coding: utf-8 -*-
import game

def main_menu():
    print("--- Welcome to Wana! ---\n")
    print("Select an option below:\n")
    print("A)Play Game\n")
    print("B)Rules\n")
    print("C)Exit\n")
    option = input()
    if(option == "A"):
        set_difficulty()
    elif(option == "B"):
        rules()
    elif(option == "C"):
        print("Thank you for playing!\n")
        print("Program will now finish.\n")
        return None
    else:
        print("Invalid Option Selected. Try Again\n")
        main_menu()
        
def set_difficulty():
    print("--- Set Difficulty ---\n")
    print("Which difficulty do you want to play in?\n")
    print("A)Easy\nB)Medium\nC)Hard\n")
    option = input()
    if(option == "A"):
        game.play(1)
    elif(option == "B"):
        game.play(2)
    elif(option == "C"):
        game.play(3)
    else:
        print("Invalid Input. Try Again.\n")
        set_difficulty()
        
def rules():
    print("-------Wana-Rules-------")
    print("Your objective in Wana is\nto make your opponent start\nhis/her turn with a stuck\npiece, making him/her lose\nif that happens. Pieces can\nmove as much as they want\nfollowing a line and you\ncan move one piece per turn\n")
    option = input("\n\n<Press any key to Return to Menu>\n")
    main_menu()