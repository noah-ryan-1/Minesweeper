def create_game_board(
    mine_board, 
    visited, 
    current_pos, 
    flagged, 
    show_all=False
):
    '''Returns a visual game board with all the relevant information
    passed into the function in order.'''
    

    # Generation of the printing board:
    game_board = []
    def board_print(show_all, flag=True):
        '''Adds the correct representation of each position
        based on the current position and visited positions. If show_all
        is True, all positions are revealed.'''

        for row in range(len(mine_board)):
            # A list for the row is appended
            game_board.append([])
            for column in range(len(mine_board)):
                # Last cell (always visible)
                if tuple((row, column)) == (len(mine_board) - 1, 
                    len(mine_board) - 1):
                    game_board[row].append(' E ')
               
                # Checks for revealable positions
                elif show_all or (row, column) in \
                    visited.union(flagged.union([current_pos])):
               
                    # Flags are only added if not not show_all
                    if flag and tuple((row, column)) in flagged:
                        game_board[row].append(' F ')
                
                    else:
                        if mine_board[row][column] == -1:
                            game_board[row].append(' * ')
                        else:
                            game_board[row].append(
                                f' {mine_board[row][column]} ')
            
                else:
                    # not show_all
                    game_board[row].append(' . ')
                
                # Added square bracket for current pos
                if tuple((row, column)) == current_pos:
                    game_board[row][column] = \
                        f'[{game_board[row][column].strip()}]'
    
    # Check for show_all: Checking if player on E or a mine
    if current_pos == (len(mine_board) - 1, len(mine_board) - 1) or\
        not mine_board[current_pos[0]][current_pos[1]] + 1:
        show_all = True
        board_print(show_all, False) 
    
    else:
        board_print(False)

    
    return game_board




    

