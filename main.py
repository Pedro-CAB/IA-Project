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
        choose_mode()
    elif(option == "B"):
        rules()
    elif(option == "C"):
        print("Thank you for playing!\n")
        print("Program will now finish.\n")
        return None
    else:
        print("Invalid Option Selected. Try Again\n")
        main_menu()
        
def choose_size():
    print("--- Board Size ---\n")
    print("Select the size of the board\n")
    print("Please choose a number equal to or bigger than 9.\n")
    print("POR IMPLEMENTAR CHOOSE_SIZE")
        
def choose_mode():
    print("--- Game Mode ---\n")
    print("Which difficulty do you want to play in?\n")
    print("A)Player vs Player\nB)Player vs PC\n")
    option = input()
    if(option == "A"):
        game.play_pvp()
    elif(option == "B"):
        choose_difficulty(2)
    else:
        print("Invalid Input. Try Again.\n")
        choose_mode()
        
def choose_difficulty(mode):
    print("--- Set Difficulty ---\n")
    print("Which difficulty do you want to play in?\n")
    print("A)Easy\nB)Medium\nC)Hard\n")
    option = input()
    if(option == "A"):
        game.start_pve(1)
    elif(option == "B"):
        game.start_pve(2)
    elif(option == "C"):
        game.start_pve(3)
    else:
        print("Invalid Input. Try Again.\n")
        choose_difficulty()
        
def rules():
    print("-------Wana-Rules-------")
    print("Your objective in Wana is\nto make your opponent start\nhis/her turn with a stuck\npiece, making him/her lose\nif that happens. Pieces can\nmove as much as they want\nfollowing a line and you\ncan move one piece per turn\n")
    option = input("\n\n<Press any key to Return to Menu>\n")
    main_menu()