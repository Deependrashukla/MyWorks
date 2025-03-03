#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

/* 
 it creates and set m x n board which is initially have value = empty spaces (' ').
 parameters:
   - m: The number of rows in the board.
   - n: The number of columns in the board.
 Returns:
   - A dynamically allocated 2D array representing the game board.
*/
char** initialize_board(int m, int n) {
    assert(m > 0 && n > 0); // Ensure the board dimensions are positive

    // Allocate memory for the board (an array of pointers to rows)
    char** board = (char**)malloc(m * sizeof(char*));
    assert(board != NULL); // Ensure memory allocation was successful

    for (int i = 0; i < m; i++) {
        // Allocate memory for each row
        board[i] = (char*)malloc(n * sizeof(char));
        assert(board[i] != NULL); // Ensure memory allocation was successful

        for (int j = 0; j < n; j++) {
            // Fill each cell with an empty space
            board[i][j] = ' ';
        }
    }
    return board;
}

/* 
 Checks if a move is valid for the given column.
 A move is valid if the column is within bounds and not already full.
 parameters:
   - board: The game board (a 2D array).
   - m: The number of rows in the board.
   - n: The number of columns in the board.
   - col: The column to check for a valid move.
 Returns:
   - true if the move is valid, false otherwise.
*/
bool is_valid_move(char** board, int m, int n, int col) {
    assert(board != NULL); // Ensure the board is not NULL
    assert(m > 0 && n > 0); // Ensure the board dimensions are positive

    // Check if the column is within bounds and the top cell is empty
    return (col >= 0 && col < n && board[0][col] == ' ');
}

/* 
 Drops a player's piece into the specified column.
 The piece falls to the lowest available row in the column.
 parameters:
   - board: The game board (a 2D array).
   - m: The number of rows in the board.
   - n: The number of columns in the board.
   - col: The column where the piece is to be placed.
   - player: The player's symbol ('R' or 'Y') to place on the board.
*/
void make_move(char** board, int m, int n, int col, char player) {
    assert(board != NULL); // Ensure the board is not NULL
    assert(m > 0 && n > 0); // Ensure the board dimensions are positive
    assert(col >= 0 && col < n); // Ensure the column is within bounds
    assert(player == 'R' || player == 'Y'); // Ensure the player symbol is valid

    // Start from the bottom row and move upwards
    for (int i = m - 1; i >= 0; i--) {
        if (board[i][col] == ' ') {
            // Place the player's piece in the first empty cell
            board[i][col] = player;
            break;
        }
    }
}

/* 
 Checks if the current move results in a win for the player.
 A win is determined by having p consecutive pieces in a row, column, or diagonal.
 parameters:
   - board: The game board (a 2D array).
   - m: The number of rows in the board.
   - n: The number of columns in the board.
   - p: The number of consecutive pieces required to win.
   - player: The player's symbol ('R' or 'Y') to check for a win.
 Returns:
   - true if the player has won, false otherwise.
*/
bool check_win(char** board, int m, int n, int p, char player) {
    assert(board != NULL); // Ensure the board is not NULL
    assert(m > 0 && n > 0 && p > 0); // Ensure the board dimensions and p are positive
    assert(player == 'R' || player == 'Y'); // Ensure the player symbol is valid

    // Go through each cell in the board
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == player) {
                // Check for a horizontal win
                if (j <= n - p) {
                    bool win = true;
                    for (int k = 0; k < p; k++) {
                        if (board[i][j + k] != player) {
                            win = false;
                            break;
                        }
                    }
                    if (win) return true;
                }
                // Check for a vertical win
                if (i <= m - p) {
                    bool win = true;
                    for (int k = 0; k < p; k++) {
                        if (board[i + k][j] != player) {
                            win = false;
                            break;
                        }
                    }
                    if (win) return true;
                }
                // Check for a diagonal win (top-left to bottom-right)
                if (i <= m - p && j <= n - p) {
                    bool win = true;
                    for (int k = 0; k < p; k++) {
                        if (board[i + k][j + k] != player) {
                            win = false;
                            break;
                        }
                    }
                    if (win) return true;
                }
                // Check for a diagonal win (bottom-left to top-right)
                if (i >= p - 1 && j <= n - p) {
                    bool win = true;
                    for (int k = 0; k < p; k++) {
                        if (board[i - k][j + k] != player) {
                            win = false;
                            break;
                        }
                    }
                    if (win) return true;
                }
            }
        }
e    }
    return false;
}

/*
 Frees the dynamically allocated memory for the game board.
 parameters:
   - board: The game board (a 2D array).
   - m: The number of rows in the board.
*/
void free_board(char** board, int m) {
    assert(board != NULL); // Ensure the board is not NUL
    assert(m > 0); // Ensure the number of rows is positive

    // Free each row
    for (int i = 0; i < m; i++) {
        free(board[i]);
    }
    // Free the array of pointers
    free(board);
}

/*
 Runs unit tests to verify the correctness of the game logic.
 Tests include board initialization, move validation, move placement, and win detection.
*/
void test_game_logic() {
    printf("Running unit tests...\n");

    int m = 6, n = 7, p = 4;
    char** board = initialize_board(m, n);

    // Test: An empty board should allow valid moves in all columns
    for (int col = 0; col < n; col++) {
        if (!is_valid_move(board, m, n, col)) {
            printf("Test failed: Column %d should be valid initially.\n", col);
            free_board(board, m);
            return;
        }
    }

    // Test: Placing a move should correctly occupy a cell
    make_move(board, m, n, 3, 'R');
    if (board[m - 1][3] != 'R') {
        printf("Test failed: Move not placed correctly.\n");
        free_board(board, m);
        return;
    }

    // Test: Win detection for a vertical win
    make_move(board, m, n, 0, 'R');
    make_move(board, m, n, 0, 'R');
    make_move(board, m, n, 0, 'R');
    make_move(board, m, n, 0, 'R');
    if (!check_win(board, m, n, p, 'R')) {
        printf("Test failed: Vertical win not detected.\n");
        free_board(board, m);
        return;
    }

    printf("All tests passed!\n");
    free_board(board, m);
}

/*
 The main function to run the game.
 It initializes the board, processes moves, checks for wins, and handles game termination.
 parameters:
   - argc: The number of command-line arguments.
   - argv: An array of command-line arguments.
 Returns:
   - 0 on successful execution, 1 on error.
*/
int main(int argc, char* argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s m n p < input_file\n", argv[0]);
        return 1;
    }

    test_game_logic(); // Run unit tests before starting the game

    int m = atoi(argv[1]); // Number of rows
    int n = atoi(argv[2]); // Number of columns
    int p = atoi(argv[3]); // Number of consecutive pieces required to win

    assert(m > 0 && n > 0 && p > 0); // Ensure the board dimensions and p are positive

    // Set up the game board
    char** board = initialize_board(m, n);

    int move_num = 0;  // Keeps track of the number of moves made
    int col;  // Column input for each move

    // Read moves from standard input (stdin)
    while (scanf("%d", &col) == 1) {
        move_num++;

        // Check if the move is valid
        if (!is_valid_move(board, m, n, col)) {
            printf("%dX\n", move_num);  // Invalid move, print move number followed by 'X'
            free_board(board, m);
            return 0;
        }

        // Determine the current player's symbol (alternating between 'R' and 'Y')
        char player = (move_num % 2 == 1) ? 'R' : 'Y';

        // Place the player's move on the board
        make_move(board, m, n, col, player);

        // Check if the move results in a win
        if (check_win(board, m, n, p, player)) {
            printf("%d%c\n", move_num, player);  // Print move number followed by the winning player
            free_board(board, m);
            return 0;
        }
    }

    // If all moves are played and there's no winner, declare a draw
    printf("%dD\n", move_num);

    // Free the allocated memory for the board
    free_board(board, m);

    return 0;
}