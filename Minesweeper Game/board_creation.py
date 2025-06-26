def create_mine_board(grid_size):
    '''
    Returns a Minescaper board of dimensions grid_size x grid_size with 
    mines at the coordinates on the board given by mine_positions. The 
    rest of the cells are numbers indicating how many sorrounding mines 
    there are to its own cell. The function assumes grid_size >= 3 and 
    the board is square.
    '''
    # Imports:
    from itertools import product
    import random 
    
    # Generate psuedo-random mineboard locations:
    all_positions = [(i, j) 
                     for i in range(grid_size) 
                     for j in range(grid_size)
                     if (i, j) != (0, 0) and (i, j) != (grid_size - 1, grid_size -1)] 
    
    # Create mine positions
    mine_positions = random.sample(all_positions, random.randint(grid_size - 1, grid_size))
    
    
    # Checks:
    # Checks positions are within board specifications
    if max(max(mine_positions)) <= grid_size - 1 or \
        min(min(mine_positions)) >= 0:
        # Checks there are no mines at the beginning and end
        if max(mine_positions) < tuple((grid_size -1, 
            grid_size -1)) and min(mine_positions) > (0, 0):
            pass
        else:
            return
    else:
        return 
    
    
    # 1. Generating the board:
    board = []
    for row in range(grid_size):
        board.append([0] * grid_size)
    # We first set every item in the board to be a 0 to then modify 
    # them with their correct values. 
    
    # 2. Inputting the -1s at the mine locations:
    for row, column in mine_positions:
        board[row][column] = -1
    
    # 3. Algorithim for assigning numbers:
    def get_number(row, column):
        '''
        Take a 0 from the board and assings it it the value 
        from 0 to 8 dependning on the sorrounding number of mines  
        '''
        
        # We take all the possible row and column values of distance max 1 from
        # the inputted position. This set of combinations accounts for all 
        # possible sorrounding 8 cells' coordinates
        
        possible_rows = [row -1, row, row +1]
        possible_cols = [column -1, column, column +1]

        to_check = list(product(possible_rows, possible_cols))

        for row_c, column_c in to_check:
            # Ensures that numbers are within the establish range
            if min(row_c, column_c) < 0 or max(row_c, 
                column_c) > grid_size -1:
                pass
            # Otherwise they are passed into the board
            else:
                if board[row_c][column_c] == -1:
                    board[row][column] += 1


    # 4. The assignment of numbers from (3)
    # for row in board:
    for row in range(grid_size):
        for column in range(grid_size):
            if not board[row][column]:
                get_number(row, column)
    
    return board
