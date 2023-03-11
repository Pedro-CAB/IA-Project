# -*- coding: utf-8 -*-
def createBoard(piecesPerPlayer):
    #Assume-se que o piecesPerPlayer já foi verificado e é par e >= 4
    upperLine =     ['/','A','O','A','\\']
    midLineTop =    ['O','A','O','A','O']
    midLine =       ['O','O','O','O','O']
    midLineBottom = ['O','B','O','B','O']
    lowerLine =     ['\\','B','O','B','/']
    board = [upperLine,midLineTop,midLine,midLineBottom,lowerLine]
    piecesPerPlayer = int(piecesPerPlayer) - 4
    while(piecesPerPlayer > 0):
        board = extendBoard(board)
        piecesPerPlayer -= 2
    return board

def extendBoard(board):
    circles = (len(board) // 2)
    firstLine = (circles * ['/']) + ['A','O','A'] + (circles * ['\\'])
    lastLine = (circles * ['\\']) + ['B','O','B'] + (circles * ['/'])
    for line in board:
        line.insert(0,line[0])
        line.append(line[len(line)-1])
    board.insert(0,firstLine)
    board.append(lastLine)
    return board

def displayBoard(board):
    side = len(board)
    header = [str(x) for x in range(side + 1)]
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
    displayBoard(board)
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
        choose_piece(player, board)

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
    