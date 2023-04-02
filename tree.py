#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gameboard
import game
import utils

class Node:
    
    def __init__(self, board, piece, depth):
        #self.id = id
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
            gameboard.display(edge.board)
        #     print((self.id, edge.id))
        #     edge.printBoard()
            
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
        
        for i in possible_moves:
            print(i)
        
        possible_moves = utils.removeDuplicates(possible_moves)
        
        for move in possible_moves:
            
            new_board = game.make_move(piece, move, board)
            
            new_boards.append(new_board)
            
        m[piece] = list(new_boards)
        
    return m


def createGameTree(board, player, depth, tree, init):
    
    if (init is None):
   
        init = Node(board, None, 1)
    
        tree.addNode(init)
        
    while (depth > 0):
                
        maps = nextPlayerBoardsGen(board, player)        
        new_boards = maps.values()                
        
        for list_per_piece in new_boards:
            
            piece = list(filter(lambda x: maps[x] == list_per_piece, maps))[0]
            
            for b in list_per_piece:                
                #new_boards.index(b)+2
                
                #maps[new_boards.index(b)]
                node = Node(b, piece, init.get_depth() + 1)
                tree.addEdge(init, node)
                
                if player == 1:
                    
                    tree = createGameTree(b, 2, depth - 1, tree, node)
                
                else:
                    
                    tree = createGameTree(b, 1, depth - 1, tree, node)
                
                depth -= 1
   
    return tree


