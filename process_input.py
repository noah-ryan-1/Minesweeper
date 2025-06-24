def process_input(mine_board, current_pos, move_str):
    '''
    Returns the player's new position given the move and 
    a boolean flag variable which indicates whether the move 
    is a flag move or physical.
    '''
    
    # Constant Variables:
    KEYS = "wasdf"
    move = [letter for letter in move_str[:3].lower()]
    # Taking a list of the individual letters in move_str 
    
    # 1. Processing move_str:
    # Removing alphanumeric characters that are not part of KEYS
    move = [key for key in move if key in KEYS]

    # Removing f values that are not at the end 
    move[:-1] = [key for key in move[:-1] if key != 'f']

    # The only permissible 3rd element is a flag
    if len(move) == 3 and move[-1] != 'f':
        move.pop()
    
    # 2. Applying the move from the position: 
    def get_position(pos, keys, flag=False): 
        '''
        Returns the adapted position based on transformations
        made to positions (pos) by the keys in keys. Flag's 
        value determine whether it is a flag move (True) or 
        otherwise (False)
        '''   
        # Each key corresponds to a move as follows
        for key in keys:
            if key == "w":
                pos[0] -= 1
            elif key == "a":
                pos[1] -= 1 
            elif key == "s":
                pos[0] += 1
            else:
                pos[1] += 1
        

        # Range of values check
        if min(pos) < 0 or max(pos) > len(mine_board) - 1:
            pos = current_pos
            # Flag should not be carried out if move is not valid
            if flag:
                flag = not flag 
        
        # Invalidate flag move if top left or bottom right square
        elif flag and pos == [0, 0] or pos == [len(mine_board) - 1, 
            len(mine_board) - 1]:
            pos = current_pos

        
        return pos, flag
    
    new_position = list((current_pos[0], current_pos[1]))
    
    # Check empty list or just flag
    if not move or move[0] == 'f':
        return tuple((new_position[0], new_position[1], False))
    
    # Flag move
    elif move[-1] == 'f':  
        flag = True
        new_position, flag = get_position(new_position, move[:-1], flag)

    # Directional Move
    else:
        new_position, flag = get_position(new_position, move)
            
    return tuple((new_position[0], new_position[1], flag))