# -*- coding: utf-8 -*-

import gameboard


#To be decided later
class Piece:

    def __init_(self, player):
        self.player = player #Can be 'A' for Player 1 or 'B' for Player 2
        self.id = 0
        self.x = 0
        self.y = 0
        self.blocked_directions = 0
        
    def set_player(self, c):
        self.player = c
        
    def set_coordinates(self, x,y):
        self.x = x
        self.y = y

class Node:
    
    def __init__(self, id, board, depth):
        self.id = id
        self.board = board
        self.visited = False
        self.depth = depth
        self.edges = []
        
    def set_depth(self, depth):
        self.depth = depth
        
    def get_depth(self):
        return self.depth

        
    def addEdge(self, dest):
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
       self.nodes = set()
       self.edges = []
       

   def addNode(self, node):
       self.nodes.add(node)
       
   def addEdge(self, s, d):
       if s in self.nodes and d in self.nodes:
           s.addEdge(d)
           return 0
       else:
           return -1
       
   def printAllEdges(self):
       for n in self.nodes:
           n.printEdges()
           
   def addTree(self, s1, s2):
       self.addEdge(s1, s2)   



def minimax(node, depth, alpha, beta, maximising, player, maxPlayer, eval_func):
    if depth == 0 or node.isEmpty():
        return eval_func(node) * (1 if player == 'A' else -1)
    
    if maximising:
        max_eval = float('-inf')
        for move in node.allEdges():
            new_node = 1 #TODO Usar o move (o outro nó)
            evaluate = minimax(new_node, depth-1, alpha, beta, False, player, eval_func)
            max_eval = max(alpha, evaluate)
            alpha = max(alpha, evaluate)
            if beta <= alpha:
                break
            return max_eval

    #Minimimsing (opponent's turn)
    else:
        min_eval = float('inf')
        for move in node.allEdges():
            new_node = 2 #TODO
            evaluate = minimax(new_node, depth-1, alpha, beta, True, player, eval_func)
            min_eval = min(beta, evaluate)
            beta = min(beta, evaluate)
            if beta <= alpha:
                break
            return min_eval
            
