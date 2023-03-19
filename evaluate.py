import gameboard
import copy

# testada e a funcionar como pretendido
def getBlockedDirections(piece, board):
    
    count = 4;

    (xi, yi) = piece;
    
    surrounding_positions = list();

    if(xi != 0):
        surrounding_positions.append((xi-1, yi))
    else:
        surrounding_positions.append((len(board)-1, yi))

    if(yi != 0):
        surrounding_positions.append((xi, yi-1))
    else:
        surrounding_positions.append((xi, len(board)-1))

    if(xi != (len(board)-1)):
        surrounding_positions.append((xi+1, yi))
    else:
        surrounding_positions.append((0, yi))

    if(yi != (len(board)-1)):
        surrounding_positions.append((xi, yi+1))
    else:
        surrounding_positions.append((xi, 0))


    for i in range(0, len(surrounding_positions)):
        (x,y) = surrounding_positions[i];
        if(board[y][x] == '/' or board[y][x] == '\\'):
            surrounding_positions[i] = (yi,xi)
    

    for i in range(0, len(surrounding_positions)):
        (xf, yf) = surrounding_positions[i];

        if(board[yf][xf] == 'O'):
            count-=1;
    

    return count;


# testada e a funcionar como pretendido

def getBoardValue(piece, board):
    player = board[piece[1]][piece[0]];

    # score_factor: 5, 10, 15, 20, 25
    # piece_value: 0*5, 1*10, 2*15, 3*20, 4*25

    a_board_value = 0;
    b_board_value = 0;

    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if(board[row][col] == 'A'):
                blocked_directions = getBlockedDirections((col,row), board);
                score_factor = (blocked_directions+1)*5;
                piece_value = blocked_directions*score_factor;
                a_board_value += piece_value;
            
            elif(board[row][col] == 'B'):
                blocked_directions = getBlockedDirections((col,row), board);
                score_factor = (blocked_directions+1)*5;
                piece_value = blocked_directions*score_factor;
                b_board_value += piece_value;

    if(player == 'A'):
        # opponent_board_value vem em primeiro lugar sempre
        return (b_board_value, a_board_value);
    
    elif(player == 'B'):
        return (a_board_value, b_board_value)
    




# testada e a funcionar como pretendido
# old_pos = piece e new_pos = move

def evaluate(piece, move, board): #, maximize_opponent_blocked_pieces, minimize_my_blocked_pieces):

    opponent_old_board_value, my_old_board_value = getBoardValue(piece, board);

    board = gameboard.make_move(piece, move, board);

    opponent_new_board_value, my_new_board_value = getBoardValue(move, board);


    print("\nopponent_old_board_value: "+ str(opponent_old_board_value)+ "\nmy_old_board_value: "+str(my_old_board_value)+"\nopponent_new_board_value: "+str(opponent_new_board_value)+"\nmy_new_board_value: "+str(my_new_board_value))
    
    return opponent_new_board_value - opponent_old_board_value;

    # maximize_opponent_blocked_pieces == true --> se eu quiser maximizar valor das peças do oponente bloqueadas
    # minimize_my_blocked_pieces == true --> se eu quiser minimizar valor das minhas peças minhas bloqueadas
    # maximize_opponent_blocked_pieces == true && minimize_my_blocked_pieces == true --> se eu quiser as duas heuristicas, retorna um tuple (adversario, minhas)

    # assumindo que board ainda tem a peça em old_pos.
    
    # retornar a diferença entre os dois tabuleiros (new - old).
    # assumindo que o objetivo é minimizar o nosso board_value e maximizar o board_value do oponente (board_value definido pelo valor das peças bloqueadas)

    #if(maximize_opponent_blocked_pieces and not minimize_my_blocked_pieces): #se eu quiser maximizar as peças do adversario bloqueadas
    #    return opponent_new_board_value - opponent_old_board_value;
    
    #elif(minimize_my_blocked_pieces and not maximize_opponent_blocked_pieces): #se eu quiser minimizar as minhas peças bloqueadas
    #    return my_new_board_value - my_old_board_value;
    
    #else: #se eu quiser as duas heuristicas
    #    return (opponent_new_board_value - opponent_old_board_value, my_new_board_value - my_old_board_value)











# おっぱい ♥ ♡  -- Drop Em Out by Wheeler Walker Jr

# peças bloqueadas em 0 direçoes = 0
# pecas bloqueadas em 1 direçao = 2
# pecas bloqueadas em 2 direçoes = 6
