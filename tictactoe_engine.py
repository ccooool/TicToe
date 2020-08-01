import random
import sys

# TODO
# Set the size of the tic tac toe board with two global variables
BOARD_WIDTH = 3
BOARD_HEIGHT = 3

# Dictionary mapping position numbers to board coordinates
coords = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1),9: (2, 2)}


def new_board() -> list:
    """
    [1,2,3,4]
    This function will create a new, blank, tic-tac-toe board, using
    a 2D array.
    """

    # TODO 
    # Create a tic-tac-toe board filled with empty spaces. Represent empty spaces with None. 
    # Hint: Use the global board size variable.
    #
    # None  |  None | None
    # ------------------------
    # None  |  None | None
    # ------------------------
    #  None |  None |  None

   ''' if BOARD_HEIGHT == 3 and if BOARD_WIDTH == 3: 
        board = [[None, None, None],[None, None ,None],[None, None, None]]

    if BOARD_HEIGHT == 4 and if BOARD_WIDTH == 4: 
        board = [[None, None, None, None],[None, None, None, None],[None, None, None, None],[None, None, None, None]]
    '''

    board = []
    for i in range(BOARD_HEIGHT):
        row = []
        for i in range(BOARD_WIDTH):
            row.append(None)
        board.append(row)
    return board


def get_winner(board: list) -> str:
    

    """
    This function will look at the board and check if a player has won. 
    If a player won, it returns the winning player's symbol. Otherwise, 
    it returns None.

    Args:
        board (list): The list that is the tic-tac-toe board
    """

     get_all_winning_lines()
    #  =  [[1,2,3], [3,5,7], [4,5,6], [2,5,8], ..... ]


    #  1 | 2 | 3
    #  ---------
    #  4 | 5 | 6
    #  ---------
    #  7 | 8 | 9

    for three_in_row in all_3_in_a_row:
        # example: three_in_row = [3,5,7]
        values = []
        for position in three_in_row:
            x = coords[position][0]
            y = coords[position][1]
            values.append(board[x][y])
        if set(values) == {"O"} or if set(values) == {"X"}:
            print(values[0] + "has won the game!")
            return values[0]
    print("no winner :C")
    return None
            






#yay me win ¯\_(ツ)_/¯
#               |
#               |
#              /\

    # TODO
    # Check if our board contains any lines of three X's in a row or three O's in a row. 
    # If it does, then return the winning symbol
    # by taking any position from the winning line.

    # Return None if no winner is found
    return None


def get_all_winning_lines() -> list:
    """
    This function will return all the combinatinos of positions on a tictactoe board
    that can make a player win, meaning all possible positions that make up a line of three
    filled boxes in a row.

    example: 
    For the below board, one such combination is [1,5,9], this makes up the diagonal 
    from top left to bottom right.

    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9 
    
    [[1,2,3], [3,5,7], [4,5,6], [2,5,8], ..... ]

    Returns:
        list: list of lists, where inner lists are a possible combination.
    """
    
    rows = [[1,2,3], [4,5,6], [7,8,9]]
    cols = [[1,4,7], [2,5,8], [3,6,9]]
    diagonals = [[1,5,9], [7,5,3]]

    return rows + cols + diagonals
    






def render(board):
    """
    This function takes in the current board, and prints it to the command line so
    we can see it. It does not return anything.

    Args:
        board (list): The current tic tac toe board
    """
    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)
    
    row_num = 0
    # print( '  0 1 2 ')
    print ('  ------')
    for row in rows:
        output_row = ''
        for sq in row:
            if sq is None:
                output_row += ' '
            else:
                output_row += sq
        print (" |%s |" % (' '.join(output_row)))
        row_num += 1
    print ('  ------')



def make_move(symbol, board, move_co_ords):
    """
    Places the symbol at the specified coordinates on the board.

    Args:
        symbol (str): [description]
        board (list): [description]
        move_co_ords (tuple): [description]
    """
    valid_move = False
    while not valid_move:
        # TODO
        # Use an if statement to check if the position is valid.
        pass

def make_move_pos(symbol, board, position_num):
    """
    Places the symbol at the specified position on the board
    
    Args:
        symbol (str): [description]
        board (list): [description]
        move_co_ords (tuple): [description]
    """
    
    valid_move = False
    while not valid_move:
        # TODO
        # Use an if statement to check if the position is valid.
        pass





def is_board_full(board):
    """
    Checks if the board is completely full and if there are no more free spaces.

    Args:
        board (list): The current board

    Returns:
        True if the board is full, False otherwise


    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9


    """
    # Checking the board 
    # look through every row
    for row in board:
        # look through every position
        for position in row:
            # If I find one empty space, return false because it is not full
            if position = None:
                return False
    # I already looked through all spaces. So return True
    return True            
         





def get_move(board, current_player_symbol, current_player_name):
    """
    Get the move from the player

    Args:
        board ([type]): [description]
        player_symbol ([type]): [description]
    """
    valid_move = False
    while not valid_move:
        try:
            position = int(input(current_player_name + "'s turn. Choose a position to place a '" + current_player_symbol + "'"))
            if board[coords[position][0]][coords[position][1]] != None:
                print("That space isn't free")
                continue
            if position:
                return coords[position]
        except KeyboardInterrupt:
            print ("\nBye")
            sys.exit()
        except:
            print("The entered position must be a number between 1 and 9")
            


def play(p1_name, p2_name):
    """
    This function triggers the game play.

    Args:
        p1_name ([type]): [description]
        p2_name ([type]): [description] 
    """

    # Declare the two players of the game
    players = [
        ('X', p1_name),
        ('O', p2_name),
    ]

    # Start a fresh game at 0 turns so far, and a new board
    turn_number = 0
    board = new_board()

    # our board looks like this, with these labels for the spaces

    #   1 | 2 | 3
    #   ---------
    #   4 | 5 | 6
    #   ---------
    #   7 | 8 | 9

    # Continue the game until a winner is found
    while True:
        
        # Choose the player who is taking the turn
        current_player_symbol, current_player_name = players[turn_number % 2]
        render(board)

        # Take the move position from the player and mark it on the baord
        move_position = get_move(board, current_player_symbol, current_player_name)
        make_move(current_player_symbol, board, move_position)

        # Check if there is a winner
        winner = get_winner(board)

        if winner is not None:
            render(board)
            print ("THE WINNER IS %s!" % winner)
            break

        if is_board_full(board):
            render(board)
            print ("IT'S A DRAW!")
            break

        turn_number += 1





"""
How can we optimize our usage of get_all_winning_lines?

- Every single time we make a move, we calculate all possible 3 in a row
- How can we avoid this?
- Where can we store it so we don't have to calculate it so many times?
- 

"""