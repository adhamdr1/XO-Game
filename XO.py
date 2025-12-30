import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    """Prints the board in a readable 3x3 grid."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Returns True if the specified player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    """Returns True if the board is full and no one has won."""
    return EMPTY not in board

def minimax(board, depth, is_maximizing):
    """
    The Minimax Algorithm.
    Recursively checks all future moves to return a score for the current board state.
    """
    
    if check_winner(board, AI):
        return 10
    if check_winner(board, HUMAN):
        return -10
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY 
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY 
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    """Finds the best move for the AI using Minimax."""
    best_score = -math.inf
    move = -1
    
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = EMPTY
            
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe!")
    print("1. Player vs Player")
    print("2. Player vs AI (Unbeatable)")
    
    choice = input("Select mode (1 or 2): ")
    
    current_player = HUMAN
    game_running = True

    while game_running:
        print_board(board)
        
        if current_player == HUMAN:
            print(f"Player {HUMAN}'s turn.")
            try:
                move = int(input("Enter position (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != EMPTY:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a number.")
                continue
        else:
            if choice == '2':
                print("AI is thinking...")
                move = get_best_move(board)
            else:
                print(f"Player {AI}'s turn.")
                try:
                    move = int(input("Enter position (1-9): ")) - 1
                    if move < 0 or move > 8 or board[move] != EMPTY:
                        print("Invalid move. Try again.")
                        continue
                except ValueError:
                    print("Please enter a number.")
                    continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if choice == '2' and current_player == AI:
                print("The AI wins! Better luck next time.")
            else:
                print(f"Player {current_player} wins!")
            game_running = False
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_running = False
        else:
            current_player = AI if current_player == HUMAN else HUMAN

if __name__ == "__main__":
    play_game()