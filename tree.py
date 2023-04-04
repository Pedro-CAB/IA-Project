#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gameboard
import game
import utils
import random

# Class Node of a Tree
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
        
    def allEdges(self):
        random.shuffle(self.edges)
        return self.edges
        
    def printEdges(self):
        for edge in self.edges:
            print((self.piece, edge.origin))
            print("Depth:")
            print(self.depth)
            gameboard.display(edge.node.board)
            print('-----------')
            
    def isEmpty(self):
        return len(self.edges) == 0
    
    def printBoard(self):
        return gameboard.display(self.board)
    
# Class Edge betweeen Nodes of a Tree
class Edge:

    def __init__(self, origin, node):
        self.origin = origin 
        self.node = node

# Class of a game Tree
class Tree:
    
   def __init__(self):
       self.nodes = []
       
   def addNode(self, node):
       self.nodes.append(node)
       
   def addEdge(self, s, d, piece):
       if s in self.nodes and d not in self.nodes:
            e = Edge(piece, d)
            d.set_depth(s.depth + 1)
            s.edges.append(e)
            self.nodes.append(d)
            return 0
       else:
            return -1
       
   def printAllEdges(self):
       for n in self.nodes:
           n.printEdges()
           
   def addTree(self, s1, s2):
       self.addEdge(s1, s2)

# This method will generate the possible boards for all possible moves of the
# pieces of the input player and stores them in a dictionary.
def nextPlayerBoardsGen(board, player):
    
    m = {}
    
    pieces = gameboard.getPieceCoords(board, player)
    
    for piece in pieces:
        
        new_boards = []
        
        possible_moves = gameboard.calculateValidMoves(piece, board)
        
        possible_moves = utils.removeDuplicates(possible_moves)
        
        move = ()
        
        for move in possible_moves:
            
            new_board = game.make_move(piece, move, board)
            
            new_boards.append(new_board)
            
        m[(piece, move)] = list(new_boards)
        
    return m

# This method will create the Game Tree, starting by the board stored in 
# the initial node Init and generate the possible moves with the help of 
# nextPlayerBoardsGen(board, player). For each move create there, it creates
# another tree recursively and alternating the player, in order to make the 
# Min and Max layers
def createGameTree(board, player, depth, tree, init):
    
    if (init is None):
   
        init = Node(1, board, None, 1)
    
        tree.addNode(init)
             
    index = 2    
    while (depth > 0):
                
        maps = nextPlayerBoardsGen(board, player)        
        new_boards = maps.values()
        
        for list_per_piece in new_boards:            
        
            (piece, move) = list(filter(lambda x: maps[x] == list_per_piece, maps))[0]
            
            random.shuffle(list_per_piece)
            
            for b in list_per_piece:                

                node = Node(index,b, move, init.get_depth() + 1)
                tree.addEdge(init, node, piece)
                
                if player == 1:
                    
                    tree = createGameTree(b, 2, depth - 1, tree, node)
                
                else:
                    
                    tree = createGameTree(b, 1, depth - 1, tree, node)
                
                depth -= 1
                
                index += 1
   
    return tree
