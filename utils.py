# -*- coding: utf-8 -*-

# This method will remove the duplicates in a list. 
def removeDuplicates(lst):
    newList = []
    for item in lst:
        if item not in newList:
            newList.append(item)
    return newList

# This method will discard the moves that can't be made and only add the valid
# ones.
def discardBlockedMoves(moves):
    validMoves = []
    for move in moves:
        if move[2] == 'O':
            validMoves.append((move[0],move[1]))
        else:
            break
    return validMoves

# This method will extract a line of a given board.
def extractLin(board,lin):
    line = board[lin]
    lineList = []
    x = 0
    y = lin
    for spot in line:
        if(spot != '\\' and spot != '/'):
            lineList.append((x,y,spot))
        x += 1
    return list(lineList)

# This method will extract a column of a given board.
def extractCol(board,col):
    x = y = 0
    column = []
    for line in board:
        for spot in line:
            if(x == col and spot != '/' and spot != '\\'):
                column.append((x,y,spot))
            x += 1
        y += 1
        x = 0
    return list(column)