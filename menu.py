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
        main_menu()
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
    print("Select how many pieces each player will play with.\n")
    print("Please choose an even number greater than or equal to 4.\n")
    option = input()
    if (option.isdigit()):
        if(int(option) % 2 == 0 and int(option) >= 4):
            choose_mode(option)
        else:
            print("Size should be an even number greater than or equal to 4. Try again\n")
            choose_size()
    else:
        print("Please insert a number.\n")
        choose_size()
        
def choose_mode(boardSize):
    print("--- Game Mode ---\n")
    print("Which difficulty do you want to play in?\n")
    print("A)Player vs Player\nB)Player vs PC\nC)PC vs PC")
    option = input()
    if(option == "A"):
        game.start_pvp(boardSize)
        main_menu()
    elif(option == "B"):
        choose_difficulty(boardSize)
    elif(option == "C"):
        choose_difficulty_c(boardSize)
    else:
        print("Invalid Input. Try Again.\n")
        choose_mode()
        
def choose_difficulty_c(boardSize):
    print("--- Set Difficulty ---\n")
    print("Which difficulty do you want for PC 1?\n")
    print("A)Easy\nB)Medium\nC)Hard\n")
    option1 = input()
    dif_A = 0   
    
    if(option1 == "A"):
        dif_A = 1
    elif(option1 == "B"):
        dif_A = 2
    elif(option1 == "C"):
        dif_A = 3
    else:
        print("Invalid Input. Try Again.\n")
        choose_difficulty(boardSize)
        
    print("Which difficulty do you want for PC 2?\n")
    print("A)Easy\nB)Medium\nC)Hard\n")
    option1 = input()
    dif_B = 0   
    
    if(option1 == "A"):
        dif_B = 1
    elif(option1 == "B"):
        dif_B = 2
    elif(option1 == "C"):
        dif_B = 3
    else:
        print("Invalid Input. Try Again.\n")
        choose_difficulty_c(boardSize)
        
    game.start_eve(boardSize, dif_A, dif_B)
    

    
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