# -*- coding: utf-8 -*-

class Node:
    
    def __init__(self, id):
        self.id = id
        self.visited = False

class Tree:
    
   def __init__(self):
       self.nodes = {}
       self.edges = []
       

   def addNode(self, node):
       self.nodes.add(node)


   def addEdge(self, parent, dest):
       #if parent not in self.nodes or dest not in self.nodes:
           #return False
       self.edges.append((parent.id, dest.id))
       
       #return True
        
       
   def printEdges(self):
       for edge in self.edges:
           print(edge)
       
    
a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)


t = Tree()

t.addEdge(a, b)
t.addEdge(c, d)
t.addEdge(a, d)