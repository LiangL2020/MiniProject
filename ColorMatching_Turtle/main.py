# import pygame
# import random

# # initialize Pygame
# pygame.init()
# pygame.font.init() 

# # constants 
# WIDTH, HEIGHT = 800, 600
# ROWS, COLS = 3, 3
# SQUARE_SIZE = WIDTH // (COLS+2)

# # colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# COLORS = [(234, 208, 209), (150, 84, 84), (216, 202, 175), (123, 139, 111), (134, 150, 167), (201, 192, 211), (101, 101, 101)]

# # create screen and initialization 
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('TURTLE Color Matching')
# board = [[None for _ in range(COLS)] for _ in range(ROWS)]

# # display the colors 
# def display_board(block_size): 
#     col_pos = 525 

#     # TODO 
#     font = pygame.font.SysFont('sfnsmono', 5)
#     text = font.render("hello world", True, BLACK)
#     textRect = text.get_rect() 
#     textRect.center = (550,600)
#     screen.blit(text,textRect)

#     for i, color in enumerate(COLORS): 
#         pygame.draw.rect(screen, color, (col_pos + block_size + i*block_size, block_size, block_size, block_size))


# # draw the board
# def update_board(block_size):
#     for row in range(ROWS):
#         for col in range(COLS):
#             color = board[row][col] if board[row][col] else WHITE
#             pygame.draw.rect(screen, color, (col * SQUARE_SIZE + block_size, row * SQUARE_SIZE + block_size, SQUARE_SIZE, SQUARE_SIZE))
#     for col in range(COLS + 1):
#         pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + block_size, block_size), (col * SQUARE_SIZE + block_size, 3 * SQUARE_SIZE + block_size))
#     for row in range(ROWS + 1):
#         pygame.draw.line(screen, BLACK, (block_size, row * SQUARE_SIZE + block_size), (3 * SQUARE_SIZE + block_size, row * SQUARE_SIZE + block_size))

# # handle clicks
# def handle_click(x, y, block_size):
#     col = (x - block_size) // SQUARE_SIZE
#     row = (y - block_size) // SQUARE_SIZE
#     if 0 <= row < ROWS and 0 <= col < COLS:
#         board[row][col] = random.choice(COLORS)

# def is_board_full(board):
#     for row in range(ROWS):
#         for col in range(COLS):
#             if board[row][col] is None:
#                 return False
#     return True

# # handle rules and points 
# def check_board(board, score): 
#     for row in range(ROWS): 
#         for col in range(COLS):
#             # 考虑优先级，积分可调 
#             # 1. 清空 +5 
#             # 2. 三连 +3 
#             # 3. 隐藏 +2 
#             # 4. 许愿色 + 1 
#             # 5. 对对碰 + 1 
#             if is_board_full(board) or score == 0: 
                
#                 pass  

# # Main game loop
# if __name__ == "__main__":
#     running = True
#     block_size = 25
#     score = 15

#     # initialize board 
#     screen.fill(WHITE)
#     display_board(block_size)

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 handle_click(x, y, block_size)
#                 score = score - 1
#                 print("score" + score)

#         # Draw everything
#         update_board(block_size)
#         check_board(board)
#         pygame.display.flip()

#     pygame.quit()
