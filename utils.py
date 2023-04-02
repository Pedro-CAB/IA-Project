# -*- coding: utf-8 -*-
def removeDuplicates(lst):
    newList = []
    for item in lst:
        if item not in newList:
            newList.append(item)
    return newList

def discardBlockedMoves(moves):
    validMoves = []
    for move in moves:
        if move[2] == 'O':
            validMoves.append((move[0],move[1]))
        else:
            break
    return validMoves

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