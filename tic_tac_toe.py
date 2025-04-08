#====================================TASK-2====================================
# TIC-TAC-TOE AI
import math
import time
import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("  0   1   2")
    for idx, row in enumerate(board):
        print(idx, " | ".join(row))  # Print row with separators
        if idx < 2:
            print("  " + "-" * 9)  # Print row divider

# Function to check if there are any moves left on the board
def is_moves_left(board):
    return any(" " in row for row in board)  # Return True if any empty space exists

# Function to evaluate the current board state
def evaluate(board):
    # Check all rows and columns for a win
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return 10 if board[i][0] == "X" else -10
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return 10 if board[0][i] == "X" else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "X" else -10

    return 0  # Return 0 if no winner

# Minimax algorithm with alpha-beta pruning to choose the best move
def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    # Return score if a terminal state is reached
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0  # Draw

    # Maximizing player's move (AI = 'X')
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = " "  # Undo move
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break  # Beta cutoff
        return best

    # Minimizing player's move (User = 'O')
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = " "  # Undo move
                    beta = min(beta, best)
                    if beta <= alpha:
                        break  # Alpha cutoff
        return best

# Random move for easy difficulty
def find_random_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

# Medium difficulty (mix of smart and random)
def find_medium_move(board):
    return find_best_move(board) if random.random() > 0.5 else find_random_move(board)

# Function to find the best possible move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    # Iterate through all cells to evaluate best move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"  # AI makes move
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "  # Undo move

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move  # Return coordinates of best move

# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize 3x3 board
    print("Welcome to Tic-Tac-Toe!")
    print("You will play as 'O', and I'll play as 'X'. Let's see if you can beat me!")

    # Choose difficulty
    difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()
    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid choice. Defaulting to hard.")
        difficulty = "hard"

    # Ask the user if they want to go first
    user_first = input("Do you want to go first? (y/n): ").strip().lower().startswith("y")
    print_board(board)

    while True:
        if user_first:
            # User's turn
            try:
                row, col = map(int, input("Your turn! Enter row and column (0-2): ").split())
                if board[row][col] != " ":
                    print("Oops! That spot is already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input! Enter numbers between 0 and 2.")
                continue

            board[row][col] = "O"
            print_board(board)

            if evaluate(board) == -10:
                print("🎉 Congratulations! You win!")
                break
            if not is_moves_left(board):
                print("🤝 It's a draw! Well played.")
                break

        # AI's turn
        print("AI is thinking...")
        time.sleep(1.5)

        if difficulty == "easy":
            ai_move = find_random_move(board)
        elif difficulty == "medium":
            ai_move = find_medium_move(board)
        else:  # hard
            ai_move = find_best_move(board)

        board[ai_move[0]][ai_move[1]] = "X"
        print("I made my move! Your turn now.")
        print_board(board)

        if evaluate(board) == 10:
            print("🤖 I win! Better luck next time!")
            break
        if not is_moves_left(board):
            print("🤝 It's a draw!")
            break

        user_first = True  # After first round, user always goes first

# Entry point of the program
if __name__ == "__main__":
    main()