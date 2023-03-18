# -*- coding: utf-8 -*-
import gameboard
import evaluate

def start_pvp(boardSize):
    board = createBoard(boardSize)
    play_pvp(board)
    
def play_pvp(board):
    print("Player 1 Turn!\n")
    displayBoard(board)
    board = turn(1,board)
    if(hasLost(2,board)):
        victory(1)
    else:
        print("Player 2 Turn!\n")
        displayBoard(board)
        board = turn(2,board)
        if(hasLost(1, board)):
            victory(2)
        else:
            play_pvp(board)

def createBoard(piecesPerPlayer):
    board = gameboard.create(piecesPerPlayer)
    return board

def displayBoard(board):
    gameboard.display(board)
    return
            
def turn(player,board):
    piece = choose_piece(player,board)
    move = choose_move(player, piece,board)
    board = make_move(piece, move, board)
    return board

def choose_piece(player, board):
    print("Which piece do you want to move?\n")
    x = int(input("X:"))
    print("\n")
    y = int(input("Y:"))
    print("\n")
    piece = (x,y)
    if isPlayerPiece(player,board,piece):
        return piece
    else:
        print("That is not a piece of yours! Try again.\n")
        choose_piece(player, board)

def choose_move(player, piece, board):
    markedBoard = gameboard.markSpots(board, calculateValidMoves(piece, board))
    displayBoard(markedBoard)
    print("Where do you want to move it?\n")
    x = int(input("X:"))
    print("\n")
    y = int(input("Y:"))
    print("\n")
    move = (x,y)
    if isValidMove(piece,move,board):
        return move
    else:
        print("That is not a valid move! Try again.\n")
        choose_piece(player, board)
        
def make_move(piece,move,board):
    #Assumindo que o move é válido
    print("\n\n ---------- EVALUATION FUNCTION ----------\n")
    (val1, val2) = evaluate.evaluate(piece, move, board, True, True) # avaliar board novo sabendo que esta peca moveu-se 👍 

    print("\n(val1, val2) = "+str(val1)+", "+str(val2)+"\n\n\n\n")

    board = gameboard.make_move(piece, move, board)
    return board
    
def isValidMove(piece,move,board):
    return (move in calculateValidMoves(piece, board))
    
def calculateValidMoves(piece,board):
    moves = gameboard.calculateValidMoves(piece, board)
    return moves

def isPlayerPiece(player,board,piece):
    if (int(player) == 1):
        return (board[piece[1]][piece[0]] == 'A')
    elif (player == 2):
        return (board[piece[1]][piece[0]] == 'B')

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

def victory(player):
    print("Player " + str(player) + "wins!\n")
    print("Returning to menu")

def start_pve(boardSize,difficulty):
    print("<Note: Right now, difficulty modes are not implemented>\n")
    