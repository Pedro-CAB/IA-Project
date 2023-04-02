#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tree
import minimax
import gameboard
import evaluate

def test_tree():
    board = gameboard.create(4)
    
    gameboard.display(board)

    t = tree.Tree()
    
    game_tree = tree.createGameTree(board, 1, 1, t, None)
    
    print(len(game_tree.nodes))
    
    return len(game_tree.nodes) == 17 
    
    
    
    
print(test_tree())



def test_minimax():
    
    board = gameboard.create(4)
    
    gameboard.display(board)

    t = tree.Tree()
    
    game_tree = tree.createGameTree(board, 1, 5, t, None)
    
    game_tree.printAllEdges()
    
    res_minimax = minimax.minimax(game_tree.nodes[0], 5, float('-inf'), float('inf'), True, 1, game_tree.nodes[0], evaluate.evaluate)
    
    return res_minimax

