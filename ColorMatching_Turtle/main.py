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
#            pink,            red,           orange,        yellow,          green,        turqoise,      blue,           purple 
COLORS_B = [(255, 153, 204), (153, 51, 51), (255, 153, 0), (255, 255, 128), (51, 102, 0), (0, 153, 153), (51, 102, 153), (204, 102, 255)]
#            dark pink,       red,           orange,          orange yellow,   yellow,          light green,     dark green,      light blue,      dark blue,       purple,          light purple 
COLORS = [(198, 138, 138), (150, 84, 84), (198, 149, 117), (188, 165, 117), (217, 209, 156), (150, 185, 153), (128, 137, 122), (155, 174, 218), (108, 126, 166), (127, 115, 132), (201, 192, 211)]
# display the colors 
def display_board(block_size): 
    col_pos = 490 

    # TODO 
    font = pygame.font.SysFont('sfnsmono', 5)
    text = font.render("hello world", True, BLACK)
    textRect = text.get_rect() 
    textRect.center = (550,600)
    screen.blit(text,textRect)

    for i, color in enumerate(COLORS): 
        pygame.draw.rect(screen, color, (col_pos + block_size + i*block_size, block_size, block_size, block_size))

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
button = Button(600, 100, 100, 50, WHITE, GRAY, 'add turtle', BLACK, button_turtle)

def board_full(board): 
    for row in range(ROWS):
        for col in range(COLS): 
            if board[row][col] == None: 
                return False 
    return True 

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
    pygame.display.flip() 
    
def contains_pair(pairs, target_pair):
    reversed_pair = (target_pair[1], target_pair[0])
    return target_pair in pairs or reversed_pair in pairs

def check_duplicates(board, score): 
    triples = [] 
    pairs = []
    included_coords = set()

    # triples 
    if board[0][0] == board[1][1] == board[2][2]: 
        score += 3 
        included_coords.add((0, 0))
        included_coords.add((1, 1))
        included_coords.add((2, 2))
        triples.append(((0, 0), (1, 1), (2, 2)))
    if board[0][2] == board[1][1] == board[2][0]: 
        score += 3 
        included_coords.add((0, 2))
        included_coords.add((1, 1))
        included_coords.add((2, 0))
        triples.append(((0, 2), (1, 1), (2, 0)))
    for i in range(ROWS): 
        if board[i][0] == board[i][1] == board[i][2]: 
            score += 3 
            included_coords.add((i, 0))
            included_coords.add((i, 1))
            included_coords.add((i, 2))
            triples.append(((i, 0), (i, 1), (i, 2)))
        if board[0][i] == board[1][i] == board[2][i]: 
            score += 3  
            included_coords.add((0, i))
            included_coords.add((1, i))
            included_coords.add((2, i))
            triples.append(((0, i), (1, i), (2, i)))
    
    # pairs 
    for row in range(ROWS): 
        for col in range(COLS): 
            color = board[row][col] 
            if color is not None: 
                for row_match in range(ROWS): 
                    for col_match in range(COLS): 
                        if board[row_match][col_match] == color and not (row == row_match and col == col_match): 
                            new_pair = ((row, col), (row_match, col_match))
                            if not contains_pair(pairs, new_pair):
                                if (row, col) not in included_coords and (row_match, col_match) not in included_coords:
                                    pairs.append(new_pair)
                                    included_coords.add((row, col))
                                    included_coords.add((row_match, col_match))
    return triples, pairs

def wait(wait_ms):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < wait_ms:
        # handle events to keep the application responsive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def check_empty(board, score): 
    for row in range(ROWS):
        for col in range(COLS): 
            if board[row][col] != None: 
                return False 
    return True  

def check_board(board, score, block_size, check_interval): 
    # 考虑优先级，积分可调 
    # 1. 清空 +5 
    # 2. 三连 +3 
    # 3. 隐藏 +2 
    # 4. 许愿色 + 1 
    # 5. 对对碰 + 1  

    triples, pairs = check_duplicates(board, score)

    while triples: 
        for r, c in triples[0]: 
            board[r][c] = None
        score += 3 
        update_board(block_size)
        wait(check_interval)
        triples = triples[1:]

    while pairs: 
        for r, c in pairs[0]: 
            board[r][c] = None
        score += 1 
        update_board(block_size)
        wait(check_interval)
        pairs = pairs[1:]

    if check_empty(board, score): 
        score += 5 

    # print('in check_board') 
    # board[0][0] = None 

if __name__ == "__main__": 
    running = True 
    block_size = 25 
    num_turtle = 15 
    score = 0 
    check_interval = 500  # ms

    display_board(block_size)

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
        if board_full(board): 
            wait(check_interval)
            check_board(board, score, block_size, check_interval) 

    pygame.quit() 