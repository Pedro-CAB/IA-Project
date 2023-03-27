#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gameboard
import game

import minimax


def boardGen(piece, board):
    
    new_boards = []
    
    possible_moves = gameboard.calculateValidMoves(piece,board)
    
    for p_move in possible_moves:
        
        new_board = game.make_move(piece, p_move, board)

        new_boards.append(new_board)
        
    return new_boards


def createGameTree(piece, board):
    
    game_tree = minimax.Tree()
   
    init = minimax.Node(1, board)
    
    game_tree.addNode(init)
    
    new_boards = boardGen(piece, board)
    
    for b in new_boards:
        
        node = minimax.Node(new_boards.index(b)+2, b)
        
        game_tree.addNode(node)
        
        game_tree.addEdge(init, node)       
   
    return game_tree
       
board = gameboard.create(4)

piece = (3,1)

game_tree = createGameTree(piece, board)

game_tree.printAllEdges()
