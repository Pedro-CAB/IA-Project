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

def nextPlayerBoardsGen(board, player):
    
    boards = []
    
    pieces = gameboard.getPieceCoords(board, player)    
    for piece in pieces:
        
        next_p_boards = boardGen(piece, board)
        
        boards.extend(next_p_boards)
    
    return boards


def createGameTree(board, player, depth, tree, init):
    
    if (init is None):
   
        init = minimax.Node(1, board, 1)
    
        tree.addNode(init)  
    
    while (depth > 0):
        
        new_boards = nextPlayerBoardsGen(board, player)

        for b in new_boards:
            
            node = minimax.Node(new_boards.index(b)+2, b, init.get_depth() + 1)
            
            tree.addNode(node)
            
            tree.addEdge(init, node)
            
            if player == 1:
                
                tree = createGameTree(b, 2, depth - 1, tree, node)
            
            else:
                
                tree = createGameTree(b, 2, depth - 1, tree, node)
            
            depth -= 1
   
    return tree
       
board = gameboard.create(4)

gameboard.display(board)

t = minimax.Tree()

game_tree = createGameTree(board, 1,5, t, None)

game_tree.printAllEdges()

print(len(game_tree.nodes))
