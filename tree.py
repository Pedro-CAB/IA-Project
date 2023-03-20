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
    
    old_board = board
    
    possible_moves = gameboard.calculateValidMoves(piece,board)
    
    print("Old Board:")
    gameboard.display(old_board)
    
    
    
    for p_move in possible_moves:
        print(p_move)
        print("New board:")
        game.make_move(piece, p_move, board)
        
        #gameboard.display(new_board)
        gameboard.display(board)
        gameboard.display(old_board)
        
        #new_boards.append(new_board)
        
    print("After Loop:")
    gameboard.display(old_board)
    return new_boards
    


board = gameboard.create(4)


piece = (3,1)


boards = boardGen(piece, board)


print("Initial Board:")
gameboard.display(board)


# print("Possible moves:")


# for b in boards:
#     gameboard.display(b)

