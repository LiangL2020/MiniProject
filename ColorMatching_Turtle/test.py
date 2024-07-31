import pygame
import random
from button import Button

# initialize pygame 
pygame.init() 

# constants 
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // (COLS+2) 

# colors 
WHITE = (255, 255, 255)
GRAY = (158, 158, 158)
BLACK = (0, 0, 0)
COLORS = [(234, 208, 209), (150, 84, 84), (216, 202, 175), (123, 139, 111), (134, 150, 167), (201, 192, 211), (101, 101, 101)]

# button to add turtle 
def button_turtle(): 
    color = random.choice(COLORS) 
    action_done = False
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] is None:
                board[row][col] = color
                action_done = True
                break
        if action_done:
            break

# create screen and initialization 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TURTLE Color Matching')
board = [[None for _ in range(COLS)] for _ in range(ROWS)] 
button = Button(525, 500, 100, 50, WHITE, GRAY, 'add turtle', BLACK, button_turtle)

# update board 
def update_board(block_size):
    for row in range(ROWS):
        for col in range(COLS):
            color = board[row][col] if board[row][col] else WHITE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE + block_size, row * SQUARE_SIZE + block_size, SQUARE_SIZE, SQUARE_SIZE))
    for col in range(COLS + 1):
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + block_size, block_size), (col * SQUARE_SIZE + block_size, 3 * SQUARE_SIZE + block_size))
    for row in range(ROWS + 1):
        pygame.draw.line(screen, BLACK, (block_size, row * SQUARE_SIZE + block_size), (3 * SQUARE_SIZE + block_size, row * SQUARE_SIZE + block_size))

def check_board(board, score): 
    for row in range(ROWS):
        for col in range(COLS):
            # 考虑优先级，积分可调 
            # 1. 清空 +5 
            # 2. 三连 +3 
            # 3. 隐藏 +2 
            # 4. 许愿色 + 1 
            # 5. 对对碰 + 1  
            

if __name__ == "__main__": 
    running = True 
    block_size = 25 
    score = 15 

    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.MOUSEBUTTONUP: 
                x, y = event.pos 
                # score = score - 1 
            button.check_click(event)
        
        button.draw(screen)
        update_board(block_size)
        pygame.display.flip() 

    pygame.quit() 