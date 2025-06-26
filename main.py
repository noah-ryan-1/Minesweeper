from board_creation import create_mine_board
from interactive_board import create_game_board
from process_input import process_input
from reveal_neighbors import reveal_zeros 

def main():
    # Standard game settings:
    SIZE = 5
    current_pos = (0,0)
    visited = {current_pos}
    flagged = set()
    current_pos = (0,0)
    
    # Creation of the board in system:
    hidden_board = create_mine_board(SIZE)

    # Process the players input 
    def player_input(board, current_pos):
        return process_input(board, current_pos, 
                      input('Move (up to 2 WASD steps, optionally ending in 'F' to flag): '))
    
    # Print the board pertaining to the move 
    def printing(game_board):
        print('\n')
        for row in game_board:
            for entry in row:
                print(f'{entry}  ', end='')
            print('\n')


    # Game Loop:
    game_over = False 
    while not game_over:

        # Display the board
        visited = reveal_zeros(hidden_board, visited, current_pos)
        board = create_game_board(hidden_board, visited, current_pos, flagged)
        printing(board)

        if hidden_board[current_pos[0]][current_pos[1]] == -1:
            print("BOOM! You stepped on a mine! GAME OVER!")
            game_over = True
            return
            
        
        elif tuple((current_pos[0], current_pos[1])) == tuple((SIZE - 1, SIZE - 1)):
            print("Congratulations! YOU WIN! You made it through the minefield!")
            game_over = True
            return
            
        
        # Get player input 
        new_x, new_y, flag = player_input(board, current_pos)
        
        if flag:
            flagged.add(tuple((new_x, new_y)))
        else:
            current_pos = tuple((new_x, new_y))

        

        # Check win condition 
        pass
if __name__ == '__main__':
    main()