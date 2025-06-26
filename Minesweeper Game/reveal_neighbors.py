def reveal_zeros(mine_board, visited, current_pos):
    '''
    Returns all cascaded 0s due to adjacency with the player's 
    current position and sorrounding non-zero cells. 
    '''
    
    # Imports
    from itertools import product

    # Variables:
    visited_update = visited.copy()
    
    def cascade_search(row, col, visited_update):
        '''
        Takes a position represented as row, col and the updated 
        position board and searches for adjacent 0s to return all 
        adjacent 0s accessible to the player. 
        '''

        def find_adjacents(row, col, target=0):
            '''
            Returns the coordinates of the positions around the current
            if they are equal to the player's desired number 0 or non
            zero.
            '''
            
            # Searchable containers: Defines 9 total positions
            rows = [row - 1, row, row + 1]
            cols = [col - 1, col, col + 1]

            # If the algorithim is supposed to search for 0s for the
            # cascading effect.
            if not target:
                adjacents = list(product(rows, [col])) + \
                    list(product([row], cols))
                # We only focus on vertical and horizontal neighbours
            
            # If we are searching for non-zeros
            else:
                adjacents = list(product(rows, cols))
                # The set contains all possible 8 sorrounding cells as in 
                # Task 1 

            # Filtering for board range
            adjacents = [pos for pos in adjacents 
                if max(pos) < len(mine_board) and min(pos) > -1]
 
            # Filter for desired entry (target)
            return [(row, col) for row, col in adjacents 
                if mine_board[row][col] == target]

        # Filter coordinate by coordinate for positions that meet our search
        # criteria and are not already in visisted updated. The 
        # find_adjacents() is called here on row and col 
        # from the cascade_search() arguments.
        for row, col in list(set(find_adjacents(row, col)) - visited_update):
            
            # Updating visisted positions for realised 0s:
            visited_update = visited_update.union([(row, col)])

            # For each zero found we check using find_adjacents() if 
            # sorrounding cells are non-zero and should be thus 
            # added to visited_update
            for non_zero in range(1, 8):
                visited_update = visited_update.union(find_adjacents(row, 
                    col, non_zero))
            

            # We now use Recursion on all discovered adjacent 0s by passing 
            # their position's as argument in cascade_search() repeating the 
            # algorithim as a cascade reaction!
            visited_update = visited_update.union(cascade_search(row, 
                col, visited_update))
            

        return visited_update

    # 1. Check if Current cell is a 0
    if not mine_board[current_pos[0]][current_pos[1]]:
        return cascade_search(current_pos[0], current_pos[1], visited_update)
    
    # Otherwise visited + current positions are returned
    else:
        return visited.union([current_pos])



    