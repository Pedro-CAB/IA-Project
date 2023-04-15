# -*- coding: utf-8 -*-
import game
import evaluate

# This method will display the main menu on the terminal
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


# This method will allow user to choose the board's size.
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
   

# This method will allow user choose the game mode (Player vs Player, Player vs PC, PC vs PC),
# according to the given boardSize
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
        

# This method will allow user choose the difficulty of both PC's in the last 
# game mode (PC vs PC).
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
        choose_difficulty_c(boardSize)
        
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
        
    game.start_eve(boardSize, dif_A, dif_B, evaluate.getBoardValue)
    

# This method will allow user choose the difficulty of the PC in the second
# game mode (Player vs PC). 
def choose_difficulty(boardSize):
    print("--- Set Difficulty ---\n")
    print("Which difficulty do you want to play in?\n")
    print("A)Easy\nB)Medium\nC)Hard\n")
    option = input()
    difficulty = 0
    if(option == "A"):
        difficulty = 1
    elif(option == "B"):
        difficulty = 2
    elif(option == "C"):
        difficulty = 3
    else:
        print("Invalid Input. Try Again.\n")
        choose_difficulty(boardSize)
        
    choose_eval(boardSize, difficulty)
        
        
def choose_eval(boardSize, difficulty):
    print("--- Set Evaluation function ---\n")      
    print("Which evaluation function do you want to use?\n")
    print("A)With Points\nB)Alternative (just privilege max number of block directions)?\n")
    option = input()
    if(option == "A"):
        game.start_pve(boardSize,difficulty, evaluate.getBoardValue)
    elif(option == "B"):
        game.start_pve(boardSize,difficulty, evaluate.getAlternativeBoardValue)
    else:
        print("Invalid Input. Try Again.\n")
        choose_eval(boardSize, difficulty)  
        
        
        
# This method will present the game's rules.
def rules():
    print("-------Wana-Rules-------")
    print("Your objective in Wana is\nto make your opponent start\nhis/her turn with a stuck\npiece, making him/her lose\nif that happens. Pieces can\nmove as much as they want\nfollowing a line and you\ncan move one piece per turn\n")
    input("\n\n<Press any key to Return to Menu>\n")
    main_menu()