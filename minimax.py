# -*- coding: utf-8 -*-

import copy
import random

def minimax(node, depth, alpha, beta, maximising, player, prev_move, chosen_board, eval_func):
  
    if (node != None) and (depth == 0 or node.isEmpty()):
     
        value = eval_func(prev_move.piece, node.piece, prev_move.board)[0][1] * (1 if player == 1 else -1)
        board = eval_func(prev_move.piece, node.piece, prev_move.board)[1]
        return (value, board, prev_move.piece, node.piece)
    
    if maximising:
        max_eval = float('-inf')
        node = prev_move
        random.shuffle(prev_move.edges)
        for move in prev_move.allEdges():
            node.piece = move.origin
            evaluate = minimax(move.node, depth-1, alpha, beta, False, player, node, chosen_board, eval_func)
            max_eval = max(alpha, evaluate[0])
            if max_eval == evaluate[0]:
                chosen_board = copy.deepcopy(evaluate[1])
            alpha = max(alpha, evaluate[0])
            if beta <= alpha:
                break
        return (max_eval, chosen_board, move.origin, move.node.piece)

    #Minimising (opponent's turn)
    else:
        min_eval = float('inf')
        node = prev_move
        random.shuffle(prev_move.edges)
        for move in prev_move.allEdges():
            node.piece = move.origin
            evaluate = minimax(move.node, depth-1, alpha, beta, True, player, node, chosen_board, eval_func)
            min_eval = min(beta, evaluate[0])
            if min_eval == evaluate[0]:
                chosen_board= copy.deepcopy(evaluate[1])
            beta = min(beta, evaluate[0])
            if alpha <= beta:
                break
        return (min_eval, chosen_board, move.origin, move.node.piece)
            
