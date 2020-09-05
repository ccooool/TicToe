import copy
import tictactoe_engine as ttt

"""
checks if X won or not
"""
def check_if_won(board, winner, to_optimize):
    if winner is not None:
        if winner == to_optimize:
            return True
        else:
            return False
    # If there is no winner at all
    return None

def get_all_valid_moves(board):
    valid_moves = []
    # look through every row
    for row in range(ttt.BOARD_HEIGHT):
        # look through every position
        for position in range(ttt.BOARD_WIDTH):
            # If I find one empty space, return false because it is not full
            if board[row][position] == None:
                valid_moves.append((row, position))
    return valid_moves  


def make_move2(board, who_am_i):
    """
    This function figures out what the bset move is to take given a tic tac toe board.

    """
    best_move = None
    best_score = None

    for move in get_all_valid_moves(board):
        copy_board = copy.deepcopy(board)
        ttt.make_move(who_am_i, copy_board, move)
        if who_am_i == 'O':
            opposite_player = 'X'
        else:
            opposite_player = 'O'
        # use minimax to score "copy_board"
        score = ai_stuff(copy_board, opposite_player, who_am_i)
        if best_score < score or best_score == None:
            best_score = score
            best_move = move

    return best_move
 


def ai_stuff(board, ai_player, player_to_optimize):
    """
    This function computes the best score using minimax for any given board, and any player in tic tac toe
    
    """
    if ttt.is_board_full(board):
        return 0
    winner = ttt.get_winner(board)
    if check_if_won(board, winner, player_to_optimize) == True:
        return 1
    if check_if_won(board, winner, player_to_optimize) == False:
        return -1
    
    valid_moves = get_all_valid_moves(board)

    scores = []

    for pos in valid_moves:
        copy_board = copy.deepcopy(board)
        ttt.make_move(ai_player, pos, board)
        # opposite player is the opponent of ai_player
        if ai_player == 'O':
            opposite_player = 'X'
        else:
            opposite_player = 'O'
        
        opponent_score = ai_stuff(copy_board, opposite_player, player_to_optimize)
        scores.append(opponent_score)

    # if the other person is playing, minimize the score. If it is the AI, maximize the score.
    if ai_player == player_to_optimize:
        return max(scores)
    else:
        return min(scores)


















































































# # RECURSIVE FUNCTION TO FIND VALUE IN A TREE

# # target is the number we're trying to find
# # node is a tree node holding a integer value, which we can get with node.value

# """
#          3
#         / \
#        2    4
#            /  \
#           5     9 

# """
# class Node:
#     def __init__(self, value, child_left, child_right)

# def Find_Value_in_Tree(node, target):
#     if node is None: return False
#     if node.value == target:
#         print("found target ate banana") 
#            return True
#     if node.child_left == None and node.child_right == None:
#         print("no children no banana")
#         return False
#     # recursive case: node has children, we want to check the children 
#     else:
#        return Find_Value_in_Tree(node.child_left,target) or Find_Value_in_Tree(node.child_right,target)

        
        


    