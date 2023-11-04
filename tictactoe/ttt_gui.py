import pygame
import sys
from tictactoe import *
from constants import *

pygame.init()
# First argument is the width and the second is the
# height of the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
chip_font = pygame.font.Font(None, CHIP_FONT)
game_over_font = pygame.font.Font(None, GAME_OVER_FONT)

# initalized the game state
board = initialize_board()
player = 1
chip = 'X'
game_over = 0
winner = 0



def draw_grid():
    for i in range(1, BOARD_ROWS):
        # Draws horizontal lines
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),  # Cordinates of first point
            (WIDTH, i * SQUARE_SIZE),  # Cordinates of second point
            LINE_WIDTH,
        )

    for i in range(1, BOARD_COLS):
        # Draws vertical lines
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH,
        )


def draw_chips():
    # (type of text, default 0, color)
    chip_x_surf = chip_font.render("X", 0, CROSS_COLOR)
    chip_o_surf = chip_font.render("O", 0, CIRCLE_COLOR)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "X":
                chip_x_rect = chip_x_surf.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][col] == 'O':
                chip_o_rect = chip_o_surf.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                # Draws surface on pygame window. (surface, rectangle above the location of the surface)
                screen.blit(chip_o_surf, chip_o_rect)

def draw_game_over(winner):
    screen.fill(BG_COLOR)
    if winner:
        end_text = f"Player {winner} wins!"
    else:
        end_text = "No one wins!"
    end_surf = game_over_font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_surf, end_rect)

    restart_text = "Press r to play game again..."
    restart_surf = game_over_font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))
    screen.blit(restart_surf, restart_rect)


screen.fill(BG_COLOR)
draw_grid()

while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            print(row, col)
            if available_square(board, row, col):
                # Updates 2D Array representing grid 
                mark_square(board, row, col, chip)
                if check_if_winner(board, chip):
                    game_over = 1
                    winner = player
                else:
                    if board_is_full(board):
                        game_over = 1
                        winner = 0 # Indicate tie
                
                # alternate the players and corresponding chips/marks "X" or "O"
                player = 2 if player == 1 else 1
                chip = 'O' if chip == 'X' else 'X'

                draw_chips()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Restart game
                screen.fill(BG_COLOR)
                draw_grid()
                board = initialize_board()
                player = 1
                chip = 'X'
                game_over = 0
                winner = 0

    if game_over:
        pygame.display.update()
        pygame.time.delay(1000)
        draw_game_over(winner)

    pygame.display.update()
