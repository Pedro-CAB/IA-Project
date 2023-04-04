# -*- coding: utf-8 -*-
import utils
import copy

# This method will create a board according to the number of pieces per player.
def create(piecesPerPlayer):
    #Assume-se que o piecesPerPlayer já foi verificado e é par e >= 4
    upperLine =     ['/','A','O','A','\\']
    midLineTop =    ['O','A','O','A','O']
    midLine =       ['O','O','O','O','O']
    midLineBottom = ['O','B','O','B','O']
    lowerLine =     ['\\','B','O','B','/']
    board = [upperLine,midLineTop,midLine,midLineBottom,lowerLine]
    piecesPerPlayer = int(piecesPerPlayer) - 4
    while(piecesPerPlayer > 0):
        board = extend(board)
        piecesPerPlayer -= 2
    return board

# This method will create the circle lines of the given board.
def extend(board):
    circles = (len(board) // 2)
    firstLine = (circles * ['/']) + ['A','O','A'] + (circles * ['\\'])
    lastLine = (circles * ['\\']) + ['B','O','B'] + (circles * ['/'])
    for line in board:
        line.insert(0,line[0])
        line.append(line[len(line)-1])
    board.insert(0,firstLine)
    board.append(lastLine)
    return board

# This method will ensure the display of the given board on the terminal.
def display(board):
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

# This method will show the valid positions a piece can move in a given board.
def displayMarked(piece,board):
    display(markSpots(board, calculateValidMoves(piece, board)))
    return

# This method will mark the valid position in a board.
def markSpots(board,spots):
    x = y = 0
    markedBoard = []
    for line in board:
        newLine = []
        for spot in line:
            if (x,y) in spots:
                spot = 'X'
            newLine.append(spot)
            x += 1
        markedBoard.append(newLine)
        x = 0
        y += 1
    return markedBoard

# This method will ensure a piece will move to the final position in
# move variable, in a given board.
def make_move(piece,move,board):
    #Assumindo que o move é válido
    new_board = copy.deepcopy(board)
    xi = piece[0]
    yi = piece[1]
    xf = move[0]
    yf = move[1]
    pieceChar = new_board[yi][xi]
    spotChar = new_board[yf][xf]
    new_board[yi][xi] = spotChar
    new_board[yf][xf] = pieceChar
    return new_board

# This method will determine the valid final positions a piece can move in a
# given board.
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
            if (board[y][newX] == 'O' and not((newX,y) in moves)):
                newMoves.append((newX,y))
            else:
                moveLeft = False
        if (moveRight):
            newX = adjustCoordToSize(x + depth, board)
            if (board[y][newX] == 'O' and not((newX,y) in moves)):
                newMoves.append((newX,y))
            else:
                moveRight = False
        if (moveUp):
            newY = adjustCoordToSize(y - depth, board)
            if (board[newY][x] == 'O' and not((x,newY) in moves)):
                newMoves.append((x,newY))
            else:
                moveUp = False
        if (moveDown):
            newY = adjustCoordToSize(y + depth, board)
            if (board[newY][x] == 'O' and not((x,newY) in moves)):
                newMoves.append((x,newY))
            else:
                moveDown = False
        depth += 1
        increment = len(newMoves)
        moves += newMoves
    moves += calculateCircleMoves(piece,board)
    utils.removeDuplicates(moves)
    return moves

# This method will determine the moves a piece can make through the circle lines
# in a given board.
def calculateCircleMoves(piece,board):
    side = len(board)
    moves = []
    clockwise = []
    reverse = []
    x = piece[0]
    y = piece[1]
    currentLine = utils.extractLin(board, y)
    currentCol = utils.extractCol(board, x)
    middle = middleOfSide(len(board)) - 1
    if identifySector(piece, board) == 1:
        if (x == middle):
            clockwise += [(x+1,y,board[y][x+1])]
            final = [(x-1,y,board[y][x-1])]
        elif (x == middle - 1):
            clockwise += [(x+1,y,board[y][x+1]),(x+2,y,board[y][x+2])]
            final = []
        elif (x == middle + 1):
            final = [(x-2,y,board[y][x-2]),(x-1,y,board[y][x-1])]
        upperLine = leftCol = y
        lowerLine = rightCol = side - 1 - upperLine
        clockwise += utils.extractCol(board, rightCol)
        a = utils.extractLin(board, lowerLine)
        a.reverse()
        clockwise += a
        b = utils.extractCol(board, leftCol)
        b.reverse()
        clockwise += b
    elif identifySector(piece, board) == 2:
        if (y == middle):
            clockwise += [(x,y+1,board[y+1][x])]
            final = [(x,y-1,board[y-1][x])]
        elif (y == middle - 1):
            final = [(x,y+2,board[y+2][x]),(x,y+1,board[y+1][x])]
        elif (y == middle + 1):
            clockwise += [(x,y-1,board[y-1][x]),(x,y-2,board[y-2][x])]
            final = []
        leftCol = upperLine = piece[0]
        rightCol = lowerLine = side - 1 - leftCol
        a = utils.extractLin(board, lowerLine)
        a.reverse()
        clockwise += utils.extractLin(board, upperLine) + utils.extractCol(board, rightCol) + a
    elif identifySector(piece, board) == 4:
        if (y == middle):
            final = [(x,y+1,board[y+1][x])]
            clockwise += [(x,y-1,board[y-1][x])]
        elif (y == middle - 1):
            clockwise += [(x,y+1,board[y+1][x]),(x,y+2,board[y+2][x])]
            final = []
        elif (y == middle + 1):
            final = [(x,y-2,board[y-2][x]),(x,y-1,board[y-1][x])]
        rightCol = lowerLine = piece[0]
        leftCol = upperLine = side - 1 - rightCol
        a = utils.extractLin(board, lowerLine)
        a.reverse()
        b = utils.extractCol(board, leftCol)
        b.reverse()
        clockwise += a + b + utils.extractLin(board, upperLine)
    elif identifySector(piece, board) == 5:
        if (x == middle):
            final = [(x+1,y,board[y][x+1])]
            clockwise += [(x-1,y,board[y][x-1])]
        elif (x == middle - 1):
            final = [(x+2,y,board[y][x+2]),(x+1,y,board[y][x+1])]
        elif (x == middle + 1):
            clockwise += [(x-1,y,board[y][x-1]),(x-2,y,board[y][x-2])]
            final = []
        lowerLine = rightCol = piece[1]
        upperLine = leftCol = side - 1 - lowerLine
        a = utils.extractCol(board, leftCol)
        a.reverse()
        clockwise += a + utils.extractLin(board, upperLine) + utils.extractCol(board, rightCol)
    else:
        return moves
    clockwise += final
    reverse += clockwise
    reverse.reverse()
    return utils.discardBlockedMoves(clockwise) + utils.discardBlockedMoves(reverse)

# This method will separate the board in Sectors and calculate the sector of the
# given board where the piece is.
def identifySector(piece,board):
    side = len(board)
    middle = middleOfSide(side)
    isLeftX = piece[0] < middle - 2
    isMiddleX = piece[0] >= middle - 2 and piece[0] <= middle
    isRightX = piece[0] > middle
    isUpperY = piece[1] < middle - 2
    isMiddleY = piece[1] >= middle - 2 and piece[1] <= middle
    isLowerY = piece[1] > middle
    if(isMiddleX):
        if(isUpperY): return 1
        elif(isLowerY): return 5
        elif (isMiddleY): return 3
    elif(isLeftX):
        if(isMiddleY): return 2
        else: return 0
    elif(isRightX):
        if(isMiddleY): return 4
        else: return 0
    else: return 0

# This method will recalculate the coordinates, according to the size of the
# given board.
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
    
# This methos will determine the middle of the board, according to its size.
def middleOfSide(side):
    decimal = side / 2
    integer = side // 2
    if (decimal - integer >= 0.5):
        return integer + 1
    else:
        return integer
    
# This method will get the coordinates of all pieces in the board.
def getAllPieceCoords(board):
    return getPieceCoords(board,1) + getPieceCoords(board,2)
    
# This method will return the coordinates of the pieces of a player, in a given
# board.
def getPieceCoords(board, player):
    coords = []
    if player == 1:
        char = 'A'
    elif player == 2:
        char = 'B'
    else:
        return []
    x = y = 0
    for line in board:
        for spot in line:
            if spot == char:
                coords.append((x,y))
            x += 1
        x = 0
        y += 1
    return coords
        