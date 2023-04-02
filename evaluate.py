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

    #print("\npiece: "+str(piece))
    #print("\nsurrounding_positions before alteration: "+str(surrounding_positions))

    for i in range(0, len(surrounding_positions)):
        (x,y) = surrounding_positions[i];
        if(board[y][x] == '/'):
            surrounding_positions[i] = (yi,xi)

        elif(board[y][x] == '\\'):
            width_of_slash_section = int((len(board)-3)/2)
            if(xi>((len(board)-1)/2) and xi<len(board) and yi>=0 and yi < ((len(board)-1)/2)): # está no 1 quadrante
                if(xi >= (len(board)-width_of_slash_section) and xi < (len(board))): # está numa linha do 1 Quadrante
                    distance_to_first_slash = xi - (len(board)-width_of_slash_section-1)
                    surrounding_positions[i] = (xi-distance_to_first_slash, yi-distance_to_first_slash)
                elif(xi < (len(board)-width_of_slash_section)): # está numa coluna do 1 Quadrante
                    distance_to_first_slash = width_of_slash_section - yi
                    surrounding_positions[i] = (xi+distance_to_first_slash, yi+distance_to_first_slash)

            
            elif(yi>((len(board)-1)/2) and yi<len(board) and xi>=0 and xi < ((len(board)-1)/2)): # está no 3 quadrante
                if(xi>=0 and xi < width_of_slash_section):  # está numa linha do 3 Quadrante
                    distance_to_first_slash = width_of_slash_section - xi
                    surrounding_positions[i] = (xi+distance_to_first_slash, yi+distance_to_first_slash)
                elif(xi>=width_of_slash_section): # está numa coluna do 3 Quadrante
                    distance_to_first_slash = yi-(len(board)-width_of_slash_section-1)
                    surrounding_positions[i] = (xi-distance_to_first_slash, yi-distance_to_first_slash)



    for i in range(0, len(surrounding_positions)):
        (xf, yf) = surrounding_positions[i];

        if(board[yf][xf] == 'O'):
            count-=1;
    
    #print("\nsurrounding_positions after alteration: "+str(surrounding_positions))
    # print("\nblocked directions: "+str(count));
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

def evaluate(piece, move, board):

    # for row in range(0, len(board)):
    #         for col in range(0, len(board[row])):
    #             if(board[row][col] == 'A' or board[row][col] == 'B'):
    #                 getBlockedDirections((col,row), board)
    
    print("Prev:")
    print(piece)
    print("After")
    print(move)
    
    opponent_old_board_value, my_old_board_value = getBoardValue(piece, board);
    
    board = gameboard.make_move(piece, move, board);

    # print("\n\n-----------------\nA MOVE WAS MADE\n-----------------\n\n")
    
    opponent_new_board_value, my_new_board_value = getBoardValue(move, board);

    # print("\nopponent_old_board_value: "+ str(opponent_old_board_value)+ "\nmy_old_board_value: "+str(my_old_board_value)+"\nopponent_new_board_value: "+str(opponent_new_board_value)+"\nmy_new_board_value: "+str(my_new_board_value))
    
    return (opponent_new_board_value - opponent_old_board_value , my_new_board_value - my_old_board_value);






# おっぱい ♥ ♡  -- Drop Em Out by Wheeler Walker Jr
