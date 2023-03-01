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
        

def play(difficulty):
    print("<Note: Right now, difficulty modes are not implemented>\n")
    