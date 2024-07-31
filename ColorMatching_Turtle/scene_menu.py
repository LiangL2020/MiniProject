import pygame
from button import Button
import random
import lib 

# Constants
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // (COLS + 2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(198, 138, 138), (150, 84, 84), (198, 149, 117), (188, 165, 117), (217, 209, 156), (150, 185, 153), (128, 137, 122), (155, 174, 218), (108, 126, 166), (127, 115, 132), (201, 192, 211)]

color_wish = BLACK

def display_color_for_wish(screen, block_size):
    global color_wish
    col_pos = 95

    font_l = pygame.font.SysFont('sfnsmono', 20)
    text_wish_dis = font_l.render("Make a color wish!", True, WHITE)
    text_rect_wish_dis = text_wish_dis.get_rect()
    text_rect_wish_dis.center = (400, 300)
    screen.blit(text_wish_dis, text_rect_wish_dis)

    font_s = pygame.font.SysFont('sfnsmono', 16)
    text_wish = font_s.render("Color Wished: ", True, WHITE)
    text_rect_wish = text_wish.get_rect()
    text_rect_wish.center = (200, 160)
    screen.blit(text_wish, text_rect_wish)
    pygame.draw.rect(screen, color_wish, (275, 140, block_size, block_size))

    for i, color in enumerate(COLORS):
        if i < 5:
            pygame.draw.rect(screen, color, (col_pos + block_size + block_size / 2 + i * block_size, block_size + col_pos * 3, block_size, block_size))
        else:
            pygame.draw.rect(screen, color, (col_pos + block_size + (i - 5) * block_size, block_size * 2 + col_pos * 3, block_size, block_size))

    pygame.display.flip()

def handle_color_wish(x, y, block_size):
    global color_wish

    col_pos = 95
    index = -99
    if block_size + col_pos * 3 <= y <= block_size * 2 + col_pos * 3:
        index = (x - col_pos - block_size - block_size / 2) // block_size
        index = int(index) if 0.0 <= index <= 4.0 else -99
        if 0 <= index <= 4:
            color_wish = COLORS[index]
    elif block_size * 2 + col_pos * 3 <= y <= block_size * 3 + col_pos * 3:
        index = 3 + (x - col_pos + block_size) // block_size
        index = int(index) if 5.0 <= index <= 10.0 else -99
        if 5 <= index <= 10:
            color_wish = COLORS[index]

def scene_menu(screen, start_game):
    start_game.draw(screen)
    display_color_for_wish(screen, 75)
    pygame.display.flip()
