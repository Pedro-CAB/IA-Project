import gameboard
import utils

# value do board medido em funçao do numero de peças bloqueadas.

def getBlockedDirections(piece, board):
    
    count = 0;

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

    valid_moves = gameboard.calculateValidMoves(piece, board);
    filtered_moves = list(filter(lambda x : x not in surrounding_positions, valid_moves))


    for i in range(0, len(surrounding_positions)):
        (xf, yf) = surrounding_positions[i];
        if(board[yf][xf] == 'A' or board[yf][xf] == 'B'):
            print("\nvalid moves: "+str(valid_moves))
            print("\nsurrounding_positions: "+str(surrounding_positions))
            print("\nfiltered_moves: "+str(filtered_moves))
            print("\nblocked directions: "+str(count));
        
        if(board[yf][xf] != 'O'):
            count+=1;
    
    
    if(len(filtered_moves) == 0 and count < 4): count+=1;

    

    return count;

def getBoardValue(piece, board):
    player = board[piece[0]][piece[1]];

    opponent = ''
    if(player == 'A'):
        opponent = 'B'
    else: 
        opponent = 'A'

    # score_factor: 5, 10, 15, 20, 25
    # piece_value: 0*5, 1*10, 2*15, 3*20, 4*25 

    # opponent_board_value == valor das peças do oponente bloqueadas
    opponent_board_value = 0;
    # my_board_value == valor das minhas peças minhas bloqueadas
    my_board_value = 0;

    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if(board[col][row] == opponent):
                blocked_directions = getBlockedDirections((col,row), board);
                score_factor = (blocked_directions+1)*5;
                piece_value = blocked_directions*score_factor;
                opponent_board_value += piece_value;
            
            elif(board[col][row] == player):
                blocked_directions = getBlockedDirections((col,row), board);
                score_factor = (blocked_directions+1)*5;
                piece_value = blocked_directions*score_factor;
                my_board_value += piece_value;

    return (opponent_board_value, my_board_value);


# maximize_opponent_blocked_pieces == true --> se eu quiser maximizar valor das peças do oponente bloqueadas
# minimize_my_blocked_pieces == true --> se eu quiser minimizar valor das minhas peças minhas bloqueadas
# maximize_opponent_blocked_pieces == true && minimize_my_blocked_pieces == true --> se eu quiser as duas heuristicas, retorna um tuple (adversario, minhas)

# assumindo que board ainda tem a peça em old_pos.
def evaluate(piece, move, board, maximize_opponent_blocked_pieces, minimize_my_blocked_pieces):
    # old_pos = piece e new_pos = move

    opponent_old_board_value, my_old_board_value = getBoardValue(piece, board);

    copy_board = board.copy()
    gameboard.make_move(piece, move, board); # nao funciona direito
    
    opponent_new_board_value, my_new_board_value = getBoardValue(piece, copy_board);


    print("opponent_old_board_value: "+ str(opponent_old_board_value)+ "\nmy_old_board_value: "+str(my_old_board_value)+"\nopponent_new_board_value: "+str(opponent_new_board_value)+"\nmy_new_board_value: "+str(my_new_board_value))
    
    
    # retornar a diferença entre os dois tabuleiros (new - old).
    # assumindo que o objetivo é minimizar o nosso board_value e maximizar o board_value do oponente (board_value definido pelo valor das peças bloqueadas)

    if(maximize_opponent_blocked_pieces and not minimize_my_blocked_pieces): #se eu quiser maximizar as peças do adversario bloqueadas
        return opponent_new_board_value - opponent_old_board_value;
    
    elif(minimize_my_blocked_pieces and not maximize_opponent_blocked_pieces): #se eu quiser minimizar as minhas peças bloqueadas
        return my_new_board_value - my_old_board_value;
    
    else: #se eu quiser as duas heuristicas
        return (opponent_new_board_value - opponent_old_board_value, my_new_board_value - my_old_board_value)










# おっぱい ♥ ♡  -- Drop Em Out by Wheeler Walker Jr
