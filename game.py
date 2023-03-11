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
    header = [str(x) for x in range(side)]
    h_str = "    " + ' '.join(header)
    print(h_str)
    i = 0
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
        choose_piece(player, board, piece)
        
def make_move(piece,move,board):
    #Assumindo que o move é válido
    xi = piece[0]
    yi = piece[1]
    xf = move[0]
    yf = move[1]
    pieceChar = board[yi][xi]
    spotChar = board[yf][xf]
    board[yi][xi] = spotChar
    board[yf][xf] = pieceChar
    return board
    
def isValidMove(piece,move,board):
    return (move in calculateValidMoves(piece, board))
    
def calculateValidMoves(piece,board):
    moves = []
    increment = 1
    depth = 1
    moveLeft = moveRight = moveUp = moveDown = True
    x = int(piece[0])
    y = int(piece[1])
    while (increment > 0):
        increment = 0
        newMoves = []
        if (moveLeft):
            newX = adjustCoordToSize(x - depth, board)
            if (board[newX][y] == 'O' and not((newX,y) in moves)):
                newMoves.append((newX,y))
            else:
                moveLeft = False
        if (moveRight):
            newX = adjustCoordToSize(x + depth, board)
            if (board[newX][y] == 'O' and not((newX,y) in moves)):
                newMoves.append((newX,y))
            else:
                moveRight = False
        if (moveUp):
            newY = adjustCoordToSize(y - depth, board)
            if (board[x][newY] == 'O' and not((x,newY) in moves)):
                newMoves.append((x,newY))
            else:
                moveUp = False
        if (moveDown):
            newY = adjustCoordToSize(y + depth, board)
            if (board[x][newY] == 'O' and not((x,newY) in moves)):
                newMoves.append((x,newY))
            else:
                moveDown = False
        depth += 1
        increment = len(newMoves)
        moves += newMoves
    return moves
                
        
def adjustCoordToSize(coord, board):
    size = len(board)
    if (coord < 0):
        while (coord < 0):
            coord = coord + size
        return coord
    elif (coord >= size):
        while (coord >= size):
            coord = coord - size
        return coord
    else:
        return coord

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
    print("POR IMPLEMENTAR victory")
    
    

def start_pve(boardSize,difficulty):
    print("<Note: Right now, difficulty modes are not implemented>\n")
    