# -*- coding: utf-8 -*-

import copy
import random


# This method will ensure that the computers use the minimax algorithm in the
# PC modes. Given a node and its depth, it will calculate the value of the
# possible plays below (according to the input player) and evaluates each play
# with the help of eval_func and its perspective- whether it is supposed to
# maximise or minimise the play's value.
# In the prev_move it will be stored the move/board that originated the chosen
# and in the chosen_board will be the board of the chosen play.
# The alpha and beta variables will ensure the game tree pruning.
def minimax(node, depth, alpha, beta, maximising, player, prev_move, chosen_board, eval_func, heuristic):
  
    if (node != None) and (depth == 0 or node.isEmpty()):
     
        value = eval_func(prev_move.piece, node.piece, prev_move.board, heuristic)[0][1] * (1 if player == 1 else -1)
        board = eval_func(prev_move.piece, node.piece, prev_move.board, heuristic)[1]
        return (value, board, prev_move.piece, node.piece)
    
    if maximising:
        max_eval = float('-inf')
        node = prev_move
        random.shuffle(prev_move.edges)
        for move in prev_move.allEdges():
            node.piece = move.origin
            evaluate = minimax(move.node, depth-1, alpha, beta, False, player, node, chosen_board, eval_func, heuristic)
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
            evaluate = minimax(move.node, depth-1, alpha, beta, True, player, node, chosen_board, eval_func, heuristic)
            min_eval = min(beta, evaluate[0])
            if min_eval == evaluate[0]:
                chosen_board= copy.deepcopy(evaluate[1])
            beta = min(beta, evaluate[0])
            if alpha <= beta:
                break
        return (min_eval, chosen_board, move.origin, move.node.piece)
            
