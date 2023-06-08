"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def custom_state():
    return [[EMPTY, X, O],
            [O, X, EMPTY],
            [X, EMPTY, O]]

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x=o=0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == X): x+=1
            elif (board[i][j] == O): o+=1
    if (x>o):return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                ans.append((i, j))
    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """ 
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move

    return new_board

def win_check(board, move):
    ##check horizontal
    for i in range(3):
        check = True
        for j in range(3):
            if board[i][j] != move: check = False
        if (check == True): return True

    ##check vertical
    for j in range(3):
        check = True
        for i in range(3):
            if board[i][j] != move: check = False
        if (check == True): return True
    
    ##check diaganol
    l = 0
    r = 2
    left_cross = True
    right_cross = True
    for i in range(3):
        if board[i][l] != move: left_cross = False
        if board[i][r] != move: right_cross = False
        l+=1
        r-=1
    if left_cross == True or right_cross == True: return True

    return False



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if win_check(board, X): return X
    if win_check(board, O): return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None: return True
    
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY): return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X): return 1
    if (winner(board) == O): return -1
    return 0


def max_value(board):
    if (terminal(board) == True): return utility(board)
    set_of_actions = actions(board)

    ans=-1000000000
    
    for (i, j) in set_of_actions:
        ans = max(ans, min_value(result(board, (i, j))))
        if (ans == -1): return -1
    return ans

def min_value(board):

    if (terminal(board) == True): return utility(board)
    set_of_actions = actions(board)

    ans=1000000000
    
    for (i, j) in set_of_actions:
        ans = min(ans, max_value(result(board, (i, j))))
        if (ans == 1): return 1
    return ans

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board) == True): return (None, None)

    if (player(board) == X): 
        set_of_actions = actions(board)

        ans=-1000000000
        x=None
        y=None
        
        for (i, j) in set_of_actions:
            new_board = result(board, (i, j))
            value = min_value(new_board)
            if (value > ans):
                ans = value
                x = i
                y = j
        return (x, y)
    else:
        set_of_actions = actions(board)

        ans=1000000000
        x=None
        y=None
        
        for (i, j) in set_of_actions:
            new_board = result(board, (i, j))
            value = max_value(new_board)
            if (value < ans):
                ans = value
                x = i
                y = j
        return (x, y)

