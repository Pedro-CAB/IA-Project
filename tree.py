#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gameboard
import game
import utils

class Node:
    
    def __init__(self, id, board, piece, depth):
        self.id = id
        self.board = board
        self.piece = piece
        self.visited = False
        self.depth = depth
        self.edges = []
        
    def set_depth(self, depth):
        self.depth = depth
        
    def get_depth(self):
        return self.depth
        
    def addEdge(self, dest):
        if dest not in self.edges:
            dest.set_depth(self.depth + 1)
            self.edges.append(dest)
        
    def allEdges(self):
        return self.edges
        
    def printEdges(self):
        for edge in self.edges:
            print((self.id, edge.id))
            gameboard.display(edge.board)
            print('-----------')
            
    def isEmpty(self):
        return len(self.edges) == 0
    
    def printBoard(self):
        return gameboard.display(self.board)

class Tree:
    
   def __init__(self):
       self.nodes = []
       
   def addNode(self, node):
       self.nodes.append(node)
       
   def addEdge(self, s, d):
       if s in self.nodes and d not in self.nodes:
           self.addNode(d)
           s.addEdge(d)
           return 0
       else:
           return -1
       
   def printAllEdges(self):
       for n in self.nodes:
           n.printEdges()
           
   def addTree(self, s1, s2):
       self.addEdge(s1, s2)


def nextPlayerBoardsGen(board, player):
    
    m = {}
    
    pieces = gameboard.getPieceCoords(board, player)
    
    for piece in pieces:
        
        new_boards = []
        
        possible_moves = gameboard.calculateValidMoves(piece, board)
        
        possible_moves = utils.removeDuplicates(possible_moves)
        
        for move in possible_moves:
            
            new_board = game.make_move(piece, move, board)
            
            new_boards.append(new_board)
            
        m[piece] = list(new_boards)
        
    return m


def createGameTree(board, player, depth, tree, init):
    
    if (init is None):
   
        init = Node(1, board, None, 1)
    
        tree.addNode(init)
        
        
    index = 2    
    while (depth > 0):
                
        maps = nextPlayerBoardsGen(board, player)        
        new_boards = maps.values()                
        
        for list_per_piece in new_boards:
            
            piece = list(filter(lambda x: maps[x] == list_per_piece, maps))[0]
            
            
            
            for b in list_per_piece:                

                node = Node(index,b, piece, init.get_depth() + 1)
                tree.addEdge(init, node)
                
                if player == 1:
                    
                    tree = createGameTree(b, 2, depth - 1, tree, node)
                
                else:
                    
                    tree = createGameTree(b, 1, depth - 1, tree, node)
                
                depth -= 1
                
                index += 1
   
    return tree
