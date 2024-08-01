import pygame 
import lib 
from button import Button 

class Menu: 
    def __init__(self): 
        self.start_game = Button(550, 150, 100, 40, lib.WHITE, lib.GRAY, "START", lib.BLACK, self.button_start)

    def button_start(self): 
        lib.scene_manager = "GAME"
        lib.screen.fill(lib.BLACK)

    def menu_scene(self): 
        self.start_game.draw(lib.screen) 
        self.display_color_for_wish(75)
        pygame.display.flip() 

    # display available colors to make color wish 
    def display_color_for_wish(self, block_size): 
        col_pos = 95 

        font_l = pygame.font.SysFont('sfnsmono', 20) 
        text_wish_dis = font_l.render("Make a color wish!", True, lib.WHITE)
        text_rect_wish_dis = text_wish_dis.get_rect() 
        text_rect_wish_dis.center = (400, 300)
        lib.screen.blit(text_wish_dis, text_rect_wish_dis)

        font_s = pygame.font.SysFont('sfnsmono', 16) 
        text_wish = font_s.render("Color Wished: ", True, lib.WHITE)
        text_rect_wish = text_wish.get_rect() 
        text_rect_wish.center = (200, 160)
        lib.screen.blit(text_wish, text_rect_wish)
        pygame.draw.rect(lib.screen, lib.color_wish, (275, 140, block_size, block_size))

        for i, color in enumerate(lib.COLORS): 
            if i < 5:
                pygame.draw.rect(lib.screen, color, (col_pos + block_size + block_size/2 + i*block_size, block_size + col_pos*3, block_size, block_size))
            else: 
                pygame.draw.rect(lib.screen, color, (col_pos + block_size + (i-5)*block_size, block_size*2 + col_pos*3, block_size, block_size))

        pygame.display.flip() 

    def handle_color_wish(self, x, y, block_size):
        col_pos = 95 
        index = -99 

        if block_size + col_pos*3 <= y <= block_size*2 + col_pos*3: 
            index = (x - col_pos - block_size - block_size/2) // block_size 
            index = int(index) if 0.0 <= index <= 4.0 else -99
            if 0 <= index <= 4: 
                lib.color_wish = lib.COLORS[index]
        elif block_size*2 + col_pos*3 <= y <= block_size*3 + col_pos*3: 
            index = 3 + (x - col_pos + block_size) // block_size
            index = int(index) if 5.0 <= index <= 10.0 else -99
            if 5 <= index <= 10: 
                lib.color_wish = lib.COLORS[index]
    