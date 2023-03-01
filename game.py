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
    for line in board:
        l = ' '.join(line)
        print(l)
    return
        

def play(difficulty):
    print("<Note: Right now, difficulty modes are not implemented>\n")
    