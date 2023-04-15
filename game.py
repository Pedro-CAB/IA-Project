# -*- coding: utf-8 -*-
import gameboard
import tree
import minimax
import evaluate
import time
import menu


# This method will start a Player vs Player match, according to the given 
# BoardSize.
def start_pvp(boardSize):
    board = createBoard(boardSize)
    play_pvp(board)
  
# This method will assure the game flow of a Player vs Player match, according
# to the state of a given Board.
def play_pvp(board):
    print("Player 1 Turn!\n")
    displayBoard(board)
    board = turn(1,board)
    if(hasLost(2,board)):
        victory(1)
        menu.main_menu()
    else:
        print("Player 2 Turn!\n")
        displayBoard(board)
        board = turn(2,board)
        if(hasLost(1, board)):
            victory(2)
            menu.main_menu()
        else:
            play_pvp(board)

# This method will create a board according to the number of pieces per player.
def createBoard(piecesPerPlayer):
    board = gameboard.create(piecesPerPlayer)
    return board

# This method will display the given board on the terminal.
def displayBoard(board):
    gameboard.display(board)
    return
            
# This method will ensure the choice and movement of a piece according to
# the player who is playing in a given board, and change the player's turn.
def turn(player,board):
    piece = (-1,-1)
    while (piece == (-1,-1)):
        piece = choose_piece(player,board)
    move = (-1,-1)
    while (move == (-1, -1)):
        move = choose_move(player, piece,board)
    board = make_move(piece, move, board)
    return board

# This method will ensure the choice of a piece in according the current player
# in the limits of a given board.
def choose_piece(player, board):
    print("\nWhich piece do you want to move?\n")
    x = int(input("X:"))
    print("\n")
    y = int(input("Y:"))
    print("\n")
    piece = (x,y)
    if (x < 0 or x >= len(board) or y < 0 or y >= len(board)):
        print("Invalid board position! Try again.\n")
        return (-1,-1)
    elif isPlayerPiece(player,board,piece):
        return piece
    else:
        print("That is not a piece of yours! Try again.\n")
        return (-1,-1)

# This method will ensure the final position after the movement of the
# chosen piece by the current player in the limits of a given board.
def choose_move(player, piece, board):
    markedBoard = gameboard.markSpots(board, calculateValidMoves(piece, board))
    displayBoard(markedBoard)
    print("Where do you want to move it?\n")
    x = int(input("X:"))
    print("\n")
    y = int(input("Y:"))
    print("\n")
    move = (x,y)
    if (x < 0 or x >= len(board) or y < 0 or y >= len(board)):
        print("Invalid board position! Try again.\n")
        return (-1,-1)
    elif isValidMove(piece,move,board):
        return move
    else:
        print("That is not a valid move! Try again.\n")
        return (-1,-1)
        
# This method will make the move of a piece according to the given move in the
# input board.
def make_move(piece,move,board):
    #Assuming that the move is valid.
    board = gameboard.make_move(piece, move, board)
    return board
    
# This method will ensure that a move belongs to the valid ones of a given piece
# in the input board.
def isValidMove(piece,move,board):
    return (move in calculateValidMoves(piece, board))
    
# This method determines the valid moves a piece in the given board.
def calculateValidMoves(piece,board):
    moves = gameboard.calculateValidMoves(piece, board)
    return moves

# This method checks if a piece in the given board belongs to the input player.
def isPlayerPiece(player,board,piece):
    if (int(player) == 1):
        return (board[piece[1]][piece[0]] == 'A')
    elif (player == 2):
        return (board[piece[1]][piece[0]] == 'B')

# This method checks if a player has lost, according to the state of the board.
def hasLost(player,board):
    if (player == 1):
        char = 'A'
    else:
        char = 'B'
    x = y = 0
    for line in board:
        for spot in line:
            if(spot == char):
                if(len(calculateValidMoves((x,y), board)) == 0):
                    return True
            x += 1
        x = 0
        y += 1
    return False

# This method displays the victory message to the winner.
def victory(player):
    print("Player " + str(player) + " wins!\n")
    print("Returning to menu")

# This method ensures the game logic of the game in Player vs PC mode, given a 
# board and the tree depth of the decision game tree of the PC, which is defined
# by its difficulty.
def play_pve(board, treeDepth, heuristic):
    print("Player 1 Turn!\n")
    displayBoard(board)
    board = turn(1,board)
    if(hasLost(2,board)):
        displayBoard(board)
        victory(1)
        menu.main_menu()
    else:
        print("Computer's Turn!\n")
        displayBoard(board)
        t = tree.Tree()
        game_tree = tree.createGameTree(board, 2, treeDepth, t, None)
        res_minimax = minimax.minimax(None, treeDepth, float('-inf'), float('inf'), True, 2, game_tree.nodes[0], board, evaluate.evaluate, heuristic)

        board = res_minimax[1]
        
        print('\n\nComputer chose piece '+str(res_minimax[2])+' and moved it to position '+ str(res_minimax[3])+'\n\n')

        if(hasLost(1, board)):
            displayBoard(board)
            victory(2)
            menu.main_menu()
        else:
            play_pve(board, treeDepth, heuristic)

# This method ensures the game logic of the game in PC vs PC mode, given a 
# board and the tree depth of the decision game tree of both PC's, which are defined
# by their difficulty.
def play_eve(board, treeDepth_A, treeDepth_B, heuristic):
    print("Computer 1 Turn!\n")
    displayBoard(board)
    t = tree.Tree()
    game_tree = tree.createGameTree(board, 1, treeDepth_A, t, None)
    res_minimax = minimax.minimax(None, treeDepth_A, float('-inf'), float('inf'), True, 1, game_tree.nodes[0], board, evaluate.evaluate, heuristic)


    board = res_minimax[1]
    time.sleep(1)
    print('\n\nComputer 1 chose piece '+str(res_minimax[2])+' and moved it to position '+ str(res_minimax[3])+'\n\n')
    
    displayBoard(board)
    time.sleep(1)
    if(hasLost(2,board)):
        displayBoard(board)
        victory(1)
        menu.main_menu()
        
    else:
        print("Computer 2 Turn!\n")
        time.sleep(1)
        t = tree.Tree()
        game_tree = tree.createGameTree(board, 2, treeDepth_B, t, None)
        res_minimax = minimax.minimax(None, treeDepth_B, float('-inf'), float('inf'), True, 2, game_tree.nodes[0], board, evaluate.evaluate, heuristic)

        board = res_minimax[1]
        
        print('\n\nComputer 2 chose piece '+str(res_minimax[2])+' and moved it to position '+ str(res_minimax[3])+'\n\n')
        

        if(hasLost(1, board)):
            displayBoard(board)
            victory(2)
            menu.main_menu()
        else:
            displayBoard(board)
            time.sleep(1)
            play_eve(board, treeDepth_A, treeDepth_B, heuristic)
        
# This method will start a Player vs PC match, according to the chosen difficulty
# and boardSize.
def start_pve(boardSize,difficulty, eval_func):

    board = createBoard(boardSize)
    depth = 0
    if(difficulty == 1):
        depth = 2
    elif(difficulty == 2):
        depth = 4
    else:
        depth = 6

    play_pve(board, depth, eval_func)
    
# This method will start a PC vs PC match, according to the chosen PC's' difficulty
# and boardSize.  
def start_eve(boardSize, dif_A, dif_B, eval_func):
    board =createBoard(boardSize)
    depth_A = 0
    if(dif_A == 1):
        depth_A = 2
    elif(dif_A == 2):
        depth_A = 4
    else:
        depth_A = 6
        
    depth_B = 0
    if(dif_B == 1):
        depth_B = 2
    elif(dif_B == 2):
        depth_B = 4
    else:
        depth_B = 6
    
    play_eve(board, depth_A, depth_B, eval_func)
    
    
    