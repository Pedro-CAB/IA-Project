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
        choose_size()
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
    print("Select how many pieces each player will with.\n")
    print("Please choose an even number equal to or bigger than 4.\n")
    option = input()
    if (option.isdigit()):
        if(int(option) % 2 != 0 and int(option) >= 4):
            choose_mode(option)
        else:
            print("Size should be an even number equal to or bigger than 4. Try again\n")
            choose_size()
    else:
        print("Please insert a number.\n")
        choose_size()
        
def choose_mode(boardSize):
    print("--- Game Mode ---\n")
    print("Which difficulty do you want to play in?\n")
    print("A)Player vs Player\nB)Player vs PC\n")
    option = input()
    if(option == "A"):
        game.play_pvp(boardSize)
    elif(option == "B"):
        choose_difficulty(boardSize)
    else:
        print("Invalid Input. Try Again.\n")
        choose_mode()
    
def choose_difficulty(boardSize):
    print("--- Set Difficulty ---\n")
    print("Which difficulty do you want to play in?\n")
    print("A)Easy\nB)Medium\nC)Hard\n")
    option = input()
    if(option == "A"):
        game.start_pve(boardSize,1)
    elif(option == "B"):
        game.start_pve(boardSize,2)
    elif(option == "C"):
        game.start_pve(boardSize,3)
    else:
        print("Invalid Input. Try Again.\n")
        choose_difficulty(boardSize)
        
def rules():
    print("-------Wana-Rules-------")
    print("Your objective in Wana is\nto make your opponent start\nhis/her turn with a stuck\npiece, making him/her lose\nif that happens. Pieces can\nmove as much as they want\nfollowing a line and you\ncan move one piece per turn\n")
    option = input("\n\n<Press any key to Return to Menu>\n")
    main_menu()