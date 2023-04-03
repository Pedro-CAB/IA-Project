#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tree
import minimax
import gameboard
import evaluate
import utils

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
    
    game_tree = tree.createGameTree(board, 1, 12, t, None)
    
    game_tree.printAllEdges()
    
    res_minimax = minimax.minimax(None, 12, float('-inf'), float('inf'), True, 1, game_tree.nodes[0], evaluate.evaluate)
    
    return res_minimax

test_minimax()