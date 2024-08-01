import pygame
from button import Button
from scene_menu import Menu
from scene_game import Game 
import lib 

# initialize pygame 
pygame.init() 

# constants & colors 
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GRAY = (158, 158, 158)
BLACK = (0, 0, 0)
COLORS = [(198, 138, 138), (150, 84, 84), (198, 149, 117), (188, 165, 117), (217, 209, 156), (150, 185, 153), (128, 137, 122), (155, 174, 218), (108, 126, 166), (127, 115, 132), (201, 192, 211)]
#          dark pink,       red,           orange,          orange yellow,   yellow,          light green,     dark green,      light blue,      dark blue,       purple,          light purple 

# create screen and initialization 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TURTLE Color Matching')
# add_tur = Button(600, 100, 100, 50, WHITE, GRAY, 'add turtle', BLACK, button_turtle)
start_game = Button(550, 150, 100, 40, WHITE, GRAY, "START", BLACK, button_start)

# Scene management
scene_manager = "MENU"
color_wish = BLACK

def game_scene(scene):
    global scene_manager
    scene_manager = "GAME"
    screen.fill(BLACK)

if __name__ == "__main__":
    running = True
    block_size = 25
    check_interval = 500  # ms

    screen.fill(BLACK)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if scene_manager == "MENU":
                    scene_menu.handle_color_wish(x, y, 75)
            add_tur.check_click(event)
            start_game.check_click(event)

        if scene_manager == "GAME":
            scene_game.scene_game(screen, add_tur, block_size, check_interval)
        elif scene_manager == "MENU":
            scene_menu.scene_menu(screen, start_game)
        elif scene_manager == "LOSE":
            pass
        elif scene_manager == "WIN":
            pass
        else:
            if scene_manager != "MENU":
                print("INVALID SCENE")
            scene_menu.scene_menu(screen, start_game)

    pygame.quit()
