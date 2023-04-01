#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gameboard
import game

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
            edge.printBoard()
            
    def isEmpty(self):
        return len(self.edges) == 0
    
    def printBoard(self):
        return gameboard.display(self.board)

class Tree:
    
   def __init__(self):
       self.nodes = []
       
   def addNode(self, node):
       if node not in self.nodes:
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

def boardGen(piece, board):
    
    new_boards = []
    
    possible_moves = gameboard.calculateValidMoves(piece,board)
    
    for p_move in possible_moves:
        
        new_board = game.make_move(piece, p_move, board)

        new_boards.append(new_board)
        
    return new_boards

def nextPlayerBoardsGen(board, player, m):
    
    boards = []
    
    pieces= gameboard.getPieceCoords(board, player)

    for piece in pieces:
        
        next_p_boards = boardGen(piece, board)
        
        boards.extend(next_p_boards)
        
        m[len(boards)] = piece
    
    return boards


def createGameTree(board, player, depth, tree, init):
    
    if (init is None):
   
        init = Node(1, board, None, 1)
    
        tree.addNode(init)  
        
    maps = {}
    
    while (depth > 0):
                
        new_boards = nextPlayerBoardsGen(board, player, maps)
        
        for b in new_boards:
            
            key = list(filter(lambda x: maps[x] == b, maps))[0]
            
            node = Node(new_boards.index(b)+2, new_boards[key], init.get_depth() + 1)
            tree.addEdge(init, node)
            
            if player == 1:
                
                tree = createGameTree(b, 2, depth - 1, tree, node)
            
            else:
                
                tree = createGameTree(b, 1, depth - 1, tree, node)
            
            depth -= 1
   
    return tree
