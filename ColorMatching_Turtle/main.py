import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // (COLS+2)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
COLORS = [(234, 208, 209), (150, 84, 84), (216, 202, 175), (123, 139, 111), (134, 150, 167), (201, 192, 211), (101, 101, 101)]

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TURTLE Color Matching')

# Board
board = [[None for _ in range(COLS)] for _ in range(ROWS)]

# Function to display the colors 
def display_colors(block_size): 
    for i, color in enumerate(COLORS): 
        pygame.draw.rect(screen, color, (550 + i*block_size, 20, block_size, block_size))

# Function to draw the board
def update_board(block_size):
    for row in range(ROWS):
        for col in range(COLS):
            color = board[row][col] if board[row][col] else WHITE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE + block_size, row * SQUARE_SIZE + block_size, SQUARE_SIZE, SQUARE_SIZE))
    for col in range(COLS + 1):
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + block_size, block_size), (col * SQUARE_SIZE + block_size, 3 * SQUARE_SIZE + block_size))
    for row in range(ROWS + 1):
        pygame.draw.line(screen, BLACK, (block_size, row * SQUARE_SIZE + block_size), (3 * SQUARE_SIZE + block_size, row * SQUARE_SIZE + block_size))

# Function to handle clicks
def handle_click(x, y, block_size):
    col = (x - block_size) // SQUARE_SIZE
    row = (y - block_size) // SQUARE_SIZE
    if 0 <= row < ROWS and 0 <= col < COLS:
        board[row][col] = random.choice(COLORS)

# Main game loop
if __name__ == "__main__":
    running = True
    block_size = 25

    # initialize board 
    screen.fill(WHITE)
    display_colors(block_size)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                handle_click(x, y, block_size)

        # Draw everything
        update_board(block_size)
        pygame.display.flip()

    pygame.quit()
