# -*- coding: utf-8 -*-

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
    
    def __init__(self, id, value, depth):
        self.id = id
        self.value = value
        self.visited = False
        self.depth = depth
        self.edges = []
        
    def set_depth(self, depth):
        self.depth = depth
        
    def set_value(self, value):
        self.value = value
        
    def addEdge(self, edge):
        self.edges.add(edge)
        
    def printEdges(self):
        for edge in self.edges:
            print(edge)
            
    def isEmpty(self):
        return len(self.edges) == 0
        
    

class Tree:
    
   def __init__(self):
       self.nodes = {}
       self.edges = []
       

   def addNode(self, node):
       self.nodes.add(node)


def minimax(node, depth, maxPlayer):
    if depth == 0 or node.isEmpty():
        return node.value



