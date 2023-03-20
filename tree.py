#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:22:51 2023

@author: pedro
"""

import gameboard
import game


def boardGen(piece, board):
    
    new_boards = []
    
    possible_moves = gameboard.calculateValidMoves(piece,board)
    
    print("Old Board:")
    gameboard.display(board)
    
    
    for p_move in possible_moves:
        print(p_move)
        print("New board:")
        
        new_board = game.make_move(piece, p_move, board)

        new_boards.append(new_board)
        
    return new_boards
    


board = gameboard.create(4)


piece = (3,1)


boards = boardGen(piece, board)



print("Possible moves:")


for b in boards:
    gameboard.display(b)

