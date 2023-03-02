# -*- coding: utf-8 -*-
def createBoard(side):
    #Assume-se que o side já foi verificado e é >= 9
    additional = side - 9 + 1
    additional_copy = additional
    add_col = []
    while (additional > 0):
        additional += - 1
        add_col = add_col + ['O']
    top_medium_line = ['O','O','O','A'] + add_col + ['A','O','O','O']
    top_line = ['/','/','/','A'] + add_col + ['A','\\', '\\', '\\']
    bottom_line = ['\\','\\','\\','B'] + add_col + ['B','/', '/', '/']
    bottom_medium_line = ['O','O','O','B'] + add_col + ['B','O','O','O']
    medium_line = ['O','O','O','O'] + add_col + ['O','O','O','O']
    board = [top_line,top_line,top_line,top_medium_line]
    additional = additional_copy
    medium_lines = []
    while (additional > 0):
        medium_lines.append(medium_line)
        additional += -1
    board += medium_lines
    board += [bottom_medium_line, bottom_line, bottom_line, bottom_line]
    return board

def displayBoard(board):
    side = len(board)
    header = [str(x) for x in range(11)]
    header.remove("0")
    h_str = "    " + ' '.join(header)
    print(h_str)
    i = 1
    for line in board:
        space = (4 - len(str(i))) * " "
        l = str(i) + space + ' '.join(line)
        print(l)
        i += 1
    return

def start_pvp(boardSize):
    board = createBoard(boardSize)
    play_pvp(board)
    
def play_pvp(board):
    print("Player 1 Turn!\n")
    turn(1,board)
    if(hasLost(2,board)):
        victory(1)
    else:
        print("Player 2 Turn!\n")
        turn(2,board)
        if(hasLost(1, board)):
            victory(2)
        else:
            play_pvp()
            
def turn(player,board):
    piece = choose_piece(player,board)
    move = choose_move(piece,board)
    make_move(piece, move, board)

def choose_piece(player, board):
    print("Which piece do you want to move?\n")
    x = input("X:")
    print("\n")
    y = input("Y:")
    print("\n")
    piece = (x,y)
    if isPlayerPiece(player,board,piece):
        return piece
    else:
        print("That is not a piece of yours! Try again.\n")
        choose_piece()

def choose_move(piece, board):
    print("Where do you want to move it?\n")
    x = input("X:")
    print("\n")
    y = input("Y:")
    print("\n")
    move = (x,y)
    if isValidMove(piece,move,board):
        return move
    else:
        print("That is not a valid move! Try again.\n")
        choose_piece()
        
def make_move(piece,move,board):
    #Assumindo que o move é válido
    pieceChar = board[piece[1]-1][piece[0]-1]
    board[piece[1]-1][piece[0]-1] = "O"
    board[move[1]-1][move[0]-1] = pieceChar
    return board
    
def hasLost(player):
    print("POR IMPLEMENTAR hasLost")
    
def isValidMove(piece,move,board):
    print("POR IMPLEMENTAR isValidMove")

def isPlayerPiece(player,board,piece):
    print("POR IMPLEMENTAR isPlayerPiece")

def victory(player):
    print("POR IMPLEMENTAR victory")
    
    

def start_pve(boardSize,difficulty):
    print("<Note: Right now, difficulty modes are not implemented>\n")
    