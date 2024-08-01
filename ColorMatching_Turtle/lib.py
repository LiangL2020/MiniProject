import pygame 

# def init():
#     global color_wish, turtle_left, score 
#     scene_manager = "MENU" 
#     color_wish = BLACK 
#     turtle_left = 15 
#     score = 0 

# constants and colors 
WIDTH, HEIGHT = 800, 600 
WHITE = (255, 255, 255)
GRAY = (158, 158, 158)
BLACK = (0, 0, 0)
COLORS = [(198, 138, 138), (150, 84, 84), (198, 149, 117), (188, 165, 117), (217, 209, 156), (150, 185, 153), (128, 137, 122), (155, 174, 218), (108, 126, 166), (127, 115, 132), (201, 192, 211)]
#          dark pink,       red,           orange,          orange yellow,   yellow,          light green,     dark green,      light blue,      dark blue,       purple,          light purple 

check_interval = 500  # ms
color_wish = BLACK
scene_manager = "MENU" 

# initialize pygame 
pygame.init() 

# create screen and initialization 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TURTLE Color Matching')


def wait(wait_ms):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < wait_ms:
        # handle events to keep the application responsive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()