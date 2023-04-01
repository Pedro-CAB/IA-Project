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


def minimax(node, depth, alpha, beta, maximising, player, eval_func):
    if depth == 0 or node.isEmpty():
        return eval_func(node) * (1 if player == 'A' else -1)
    
    if maximising:
        max_eval = float('-inf')
        for move in node.allEdges():
            evaluate = minimax(move, depth-1, alpha, beta, False, player, eval_func)
            max_eval = max(alpha, evaluate)
            alpha = max(alpha, evaluate)
            if beta <= alpha:
                break
            return max_eval

    #Minimimsing (opponent's turn)
    else:
        min_eval = float('inf')
        for move in node.allEdges():
            evaluate = minimax(move, depth-1, alpha, beta, True, player, eval_func)
            min_eval = min(beta, evaluate)
            beta = min(beta, evaluate)
            if alpha <= beta:
                break
            return min_eval
            
