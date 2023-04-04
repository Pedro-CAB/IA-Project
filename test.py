#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tree
import minimax
import gameboard
import evaluate
import utils

#Test functions file

def test_tree():
    board = gameboard.create(4)
    
    gameboard.display(board)

    t = tree.Tree()
    
    game_tree = tree.createGameTree(board, 1, 1, t, None)
    
    game_tree.printAllEdges()
    
    print(len(game_tree.nodes))
    
    return len(game_tree.nodes) == 17

# print(test_tree())

def test_utils():
    
    return len(utils.removeDuplicates([['1','2','3','4'], ['1','2','3','4'], ['3','4','5','6']])) == 2

def test_minimax():
    
    board = gameboard.create(4)
    
    gameboard.display(board)

    t = tree.Tree()
    
    game_tree = tree.createGameTree(board, 1, 5, t, None)
    
    chosen_board = []
    
    res_minimax = minimax.minimax(None, 5, float('-inf'), float('inf'), True, 2, game_tree.nodes[0], chosen_board, evaluate.evaluate)
    
    return res_minimax

print(test_minimax())