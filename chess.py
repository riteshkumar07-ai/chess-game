import pygame
import sys

# -----------------------------
# INITIALIZATION
# -----------------------------

pygame.init()

WIDTH = 800
HEIGHT = 800

ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess Game")

# Colors
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
GREEN = (100, 150, 100)
YELLOW = (255, 255, 100)
RED = (220, 80, 80)
BLACK = (20, 20, 20)

font = pygame.font.Font(None, 70)
small_font = pygame.font.Font(None, 35)


# -----------------------------
# PIECES
# -----------------------------

pieces = {
    "r": "♜",
    "n": "♞",
    "b": "♝",
    "q": "♛",
    "k": "♚",
    "p": "♟",

    "R": "♖",
    "N": "♘",
    "B": "♗",
    "Q": "♕",
    "K": "♔",
    "P": "♙"
}


# -----------------------------
# INITIAL BOARD
# -----------------------------

board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


# -----------------------------
# GAME VARIABLES
# -----------------------------

turn = "white"

selected = None

game_over = False

message = ""


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def is_white(piece):
    return piece.isupper()


def is_black(piece):
    return piece.islower()


def same_color(piece1, piece2):
    if piece1 == " " or piece2 == " ":
        return False

    return is_white(piece1) == is_white(piece2)


def inside_board(row, col):
    return 0 <= row < 8 and 0 <= col < 8


# -----------------------------
# DRAW BOARD
# -----------------------------

def draw_board():

    for row in range(8):
        for col in range(8):

            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BROWN

            pygame.draw.rect(
                screen,
                color,
                (
                    col * SQUARE_SIZE,
                    row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE
                )
            )


# -----------------------------
# DRAW PIECES
# -----------------------------

def draw_pieces():

    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece != " ":

                text = pieces[piece]

                # Different color for white and black pieces
                if piece.isupper():
                    piece_color = (255, 255, 255)
                else:
                    piece_color = (20, 20, 20)

                piece_font = pygame.font.SysFont(
                    "segoeuisymbol",
                    70
                )

                piece_text = piece_font.render(
                    text,
                    True,
                    piece_color
                )

                x = col * SQUARE_SIZE + 10
                y = row * SQUARE_SIZE - 2

                screen.blit(
                    piece_text,
                    (x, y)
                )


# -----------------------------
# HIGHLIGHT SELECTED PIECE
# -----------------------------

def highlight_square():

    if selected is not None:

        row, col = selected

        pygame.draw.rect(
            screen,
            YELLOW,
            (
                col * SQUARE_SIZE,
                row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE
            ),
            5
        )


# -----------------------------
# PAWN MOVES
# -----------------------------

def pawn_moves(row, col, moves, piece):

    direction = -1 if piece.isupper() else 1

    start_row = 6 if piece.isupper() else 1

    # One square forward
    new_row = row + direction

    if inside_board(new_row, col):

        if board[new_row][col] == " ":

            moves.append((new_row, col))

            # Two squares from starting position
            if row == start_row:

                new_row2 = row + 2 * direction

                if board[new_row2][col] == " ":
                    moves.append((new_row2, col))

    # Capture diagonally
    for dc in [-1, 1]:

        new_row = row + direction
        new_col = col + dc

        if inside_board(new_row, new_col):

            target = board[new_row][new_col]

            if target != " " and not same_color(piece, target):

                moves.append((new_row, new_col))


# -----------------------------
# KNIGHT MOVES
# -----------------------------

def knight_moves(row, col, moves, piece):

    directions = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1)
    ]

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if inside_board(new_row, new_col):

            target = board[new_row][new_col]

            if target == " " or not same_color(piece, target):

                moves.append((new_row, new_col))


# -----------------------------
# KING MOVES
# -----------------------------

def king_moves(row, col, moves, piece):

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if inside_board(new_row, new_col):

            target = board[new_row][new_col]

            if target == " " or not same_color(piece, target):

                moves.append((new_row, new_col))


# -----------------------------
# SLIDING PIECES
# -----------------------------

def sliding_moves(row, col, moves, piece, directions):

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        while inside_board(new_row, new_col):

            target = board[new_row][new_col]

            if target == " ":

                moves.append((new_row, new_col))

            else:

                if not same_color(piece, target):

                    moves.append((new_row, new_col))

                break

            new_row += dr
            new_col += dc


# -----------------------------
# GET LEGAL MOVES
# -----------------------------

def get_moves(row, col):

    piece = board[row][col]

    moves = []

    if piece == " ":
        return moves

    piece_type = piece.lower()

    # Pawn
    if piece_type == "p":

        pawn_moves(
            row,
            col,
            moves,
            piece
        )

    # Knight
    elif piece_type == "n":

        knight_moves(
            row,
            col,
            moves,
            piece
        )

    # Bishop
    elif piece_type == "b":

        directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        sliding_moves(
            row,
            col,
            moves,
            piece,
            directions
        )

    # Rook
    elif piece_type == "r":

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        sliding_moves(
            row,
            col,
            moves,
            piece,
            directions
        )

    # Queen
    elif piece_type == "q":

        directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        sliding_moves(
            row,
            col,
            moves,
            piece,
            directions
        )

    # King
    elif piece_type == "k":

        king_moves(
            row,
            col,
            moves,
            piece
        )

    return moves


# -----------------------------
# MOVE PIECE
# -----------------------------

def move_piece(start, end):

    global turn
    global selected
    global game_over
    global message

    sr, sc = start
    er, ec = end

    piece = board[sr][sc]

    # Move piece
    board[er][ec] = piece
    board[sr][sc] = " "

    # Check if king captured
    if board[er][ec].lower() == "k":

        game_over = True

        if turn == "white":
            message = "White Wins!"
        else:
            message = "Black Wins!"

    # Change turn
    if turn == "white":
        turn = "black"
    else:
        turn = "white"

    selected = None


# -----------------------------
# DRAW GAME STATUS
# -----------------------------

def draw_status():

    if game_over:

        text = font.render(
            message,
            True,
            RED
        )

        screen.blit(
            text,
            (250, 360)
        )

    else:

        text = small_font.render(
            "Turn: " + turn.capitalize(),
            True,
            BLACK
        )

        screen.blit(
            text,
            (10, 10)
        )


# -----------------------------
# RESET GAME
# -----------------------------

def reset_game():

    global board
    global turn
    global selected
    global game_over
    global message

    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]

    turn = "white"

    selected = None

    game_over = False

    message = ""


# -----------------------------
# MAIN GAME LOOP
# -----------------------------

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:

            running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_over:
                continue

            mouse_x, mouse_y = pygame.mouse.get_pos()

            col = mouse_x // SQUARE_SIZE
            row = mouse_y // SQUARE_SIZE

            # First click
            if selected is None:

                piece = board[row][col]

                if piece != " ":

                    # Check turn
                    if (
                        turn == "white"
                        and piece.isupper()
                    ) or (
                        turn == "black"
                        and piece.islower()
                    ):

                        selected = (row, col)

            # Second click
            else:

                moves = get_moves(
                    selected[0],
                    selected[1]
                )

                if (row, col) in moves:

                    move_piece(
                        selected,
                        (row, col)
                    )

                else:

                    selected = None

    # Draw everything
    draw_board()

    highlight_square()

    draw_pieces()

    draw_status()

    pygame.display.update()

    clock.tick(60)


pygame.quit()
sys.exit()
