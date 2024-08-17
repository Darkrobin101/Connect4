import numpy as np
import random, math
PLAYER = 0
AI = 1
PLAYR_PCE = 1
AI_PCE = 2
NUM_ROW = 6
NUM_COL = 7


def create_board():
    board = np.zeros((NUM_ROW,NUM_COL))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board,col):
    for i in range(NUM_ROW):
        if board[i][col] == 0:
            return i
        
def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    # Horizontal check
    for c in range(NUM_COL-3):
        for r in range(NUM_ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Vertical check
    for c in range(NUM_COL):
        for r in range(NUM_ROW-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Positive diagonal check
    for c in range(NUM_COL-3):
        for r in range(NUM_ROW-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Negative diagonal check
    for c in range(NUM_COL-3):
        for r in range(3, NUM_ROW):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def eval_window(window,piece):
    score = 0
    opp_pce = PLAYR_PCE
    if piece == PLAYR_PCE:
        opp_pce = AI_PCE


    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score+=10  
    elif window.count(piece) == 2 and window.count(0) == 2:
        score+=5

    if window.count(opp_pce) == 3 and window.count(0) == 1:
        score-=80

    return score

def score_position(board, piece):
    score = 0
    
    center_arr = [int(i) for i in list(board[:,NUM_COL//2])]
    center_count = center_arr.count(piece)
    score+= center_count*6



    #Horizontal Scores
    
    for r in range (NUM_ROW):
        row_arr = [int(i) for i in list(board[r,:])]
        for c in range(NUM_COL - 3):
            window = row_arr[c:c+4] 
            score+= eval_window(window,piece)

    #Vertical Scores
    for c in range (NUM_COL):
        col_arr = [int(i) for i in list (board[:,c])]
        for r in range (NUM_ROW-3):
            window = col_arr[r:r+4]
            score+= eval_window(window,piece)


    #Positive Diagonal
    for r in range(NUM_ROW-3):
        for c in range(NUM_COL-3):
            window = [board[r+i][c+i] for i in range(4)]
            score+= eval_window(window,piece)
    
    #Negative Slope
    for r in range(NUM_ROW-3):
        for c in range(NUM_COL-3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score+= eval_window(window,piece)
                

    return score

def get_valid_locations(board):
    valid_locations = []
    for c in range (NUM_COL):
        if is_valid_location(board,c):
            valid_locations.append(c)
    return valid_locations


def pick_best_move(board, piece):
    valid_locations = get_valid_locations(board)
    best_score = 0
    best_col = random.choice(valid_locations)
    for c in valid_locations:
        row = get_next_open_row(board,c)
        temp = board.copy()
        drop_piece(temp,row,c,piece)
        score = score_position(temp,piece)
        if score > best_score:
            best_score = score
            best_col = c
    return best_col

def is_terminal_node(board):
    return winning_move(board,PLAYR_PCE) or winning_move(board,AI_PCE) or len(get_valid_locations(board)) == 0



def minimax_algo(board,depth,alpha,beta,max_player):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PCE):
                return (None,10000000000000000)
            elif winning_move(board,PLAYR_PCE):
                return (None,-10000000000000000)
            else:
                return (None,0)
        else:
            return (None,score_position(board,AI_PCE))
    if max_player:
        value = -math.inf
        col = random.choice(valid_locations)
        for c in valid_locations:
            r = get_next_open_row(board,c)
            temp = board.copy()
            drop_piece(temp,r,c,AI_PCE)
            score = minimax_algo(temp,depth-1,alpha,beta,False)[1]
            if score > value:
                value = score
                col = c
        return col,value
    else:
        value = math.inf
        col = random.choice(valid_locations)
        for c in valid_locations:
            r = get_next_open_row(board,c)
            temp = board.copy()
            drop_piece(temp,r,c,PLAYR_PCE)
            score = minimax_algo(temp,depth-1,alpha,beta,True)[1]
            if score < value:
                value = score
                col = c
        return col,value






def init_game():
    board = create_board()
    game_over = False
    turn = 0
    return board, game_over, turn


