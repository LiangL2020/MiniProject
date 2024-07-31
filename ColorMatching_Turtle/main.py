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

def check_triples(board, score): 
    triples = [] 
    if board[0][0] == board[1][1] == board[2][2]: 
        score += 3 
        triples.append(((0, 0), (1, 1), (2, 2)))
    if board[0][2] == board[1][1] == board[2][0]: 
        score += 3 
        triples.append(((0, 2), (1, 1), (2, 0)))
    for i in range(ROWS): 
        if board[i][0] == board[i][1] == board[i][2]: 
            score += 3 
            triples.append(((i, 0), (i, 1), (i, 2)))
        if board[0][i] == board[1][i] == board[2][i]: 
            score += 3  
            triples.append(((0, i), (1, i), (2, i)))
    return triples 

def contains_pair(pairs, target_pair):
    reversed_pair = (target_pair[1], target_pair[0])
    return target_pair in pairs or reversed_pair in pairs

def check_pairs(board, score): 
    pairs = []
    included_coords = set()
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
    return pairs


def check_empty(board, score): 
    for row in range(ROWS):
        for col in range(COLS): 
            if board[row][col] != None: 
                return False 
    return True  

def check_board(board, score): 
    triples = check_triples(board, score)
    pairs = check_pairs(board, score) 
    merge_list = triples + pairs 
    print(merge_list)
    check_empty(board, score) 

    # 考虑优先级，积分可调 
    # 1. 清空 +5 
    # 2. 三连 +3 
    # 3. 隐藏 +2 
    # 4. 许愿色 + 1 
    # 5. 对对碰 + 1  

    # print('in check_board') 
    # board[0][0] = None 

if __name__ == "__main__": 
    running = True 
    block_size = 25 
    num_turtle = 15 
    score = 0 
    check_interval = 2000  # ms
    # last_check_time = pygame.time.get_ticks()

    while running: 
        # current_time = pygame.time.get_ticks()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.MOUSEBUTTONUP: 
                x, y = event.pos 
                # score = score - 1 
            button.check_click(event)

        # if current_time - last_check_time >= check_interval:
        #     pairs = check_matching_pairs()
        #     last_check_time = current_time  # Reset the last check time

        
        button.draw(screen)
        update_board(block_size)
        check_board(board, score) if board_full(board) else None 
        pygame.display.flip() 

    pygame.quit() 