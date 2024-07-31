import pygame
import sys

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scene Switcher")
clock = pygame.time.Clock()

# Scene classes
class Scene:
    def __init__(self):
        self.next_scene = self

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

class SceneManager:
    def __init__(self, start_scene):
        self.current_scene = start_scene

    def switch_to(self, scene):
        self.current_scene = scene

    def handle_events(self, events):
        self.current_scene.handle_events(events)

    def update(self):
        self.current_scene.update()

    def draw(self, screen):
        self.current_scene.draw(screen)

# Define specific scenes
class MenuScene(Scene):
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.next_scene = GameScene()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Menu Scene", True, (255, 255, 255))
        screen.blit(text, (250, 250))

class GameScene(Scene):
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.next_scene = MenuScene()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 255))
        font = pygame.font.Font(None, 74)
        text = font.render("Game Scene", True, (255, 255, 255))
        screen.blit(text, (250, 250))

# Initialize scenes
menu_scene = MenuScene()
scene_manager = SceneManager(menu_scene)

# Main game loop
while True:
    events = pygame.event.get()
    scene_manager.handle_events(events)
    scene_manager.update()
    scene_manager.draw(screen)
    
    # Check if scene switch is needed
    if scene_manager.current_scene.next_scene != scene_manager.current_scene:
        scene_manager.switch_to(scene_manager.current_scene.next_scene)
    
    pygame.display.flip()
    clock.tick(FPS)

# import pygame as pg
# pg.init()


# win = pg.display.set_mode((500,500))

# pg.display.set_caption('Scene Switcher')

# center_x = 250 - 130
# center_y = 250  

# black= (0,0,0)
# red = (255,0,0)
# blue = (0,0,255)

# def ct(font, size, text, color):
#     mf = pg.font.Font(font, size)

#     t = mf.render(text, True, color)

#     return t 



# def draw_scene1():
#     print("This is Scene 1")
#     txt = ct("SB.ttf", 40, "Hello World!", black)
#     win.blit(txt, (center_x,center_y))


# def draw_scene2():
#     print("This is scene 2")
#     txt2 = ct("SB.ttf", 40, "scene2 ", black)
#     win.blit(txt2, (center_x,center_y))






# while True:
#     win.fill(red)

#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()

#             quit()
        
#     mouses =  pg.mouse.get_pressed()
 

#     scene_counter = 0

#     # When this function is called the next scene is drawn.

#     def draw_next_screen():
#         global scene_counter
#         scene_counter += 1
#         if scene_counter == 1:
#             draw_scene1()
#         else:
#             draw_scene2()


#     if mouses:
#         draw_next_screen()
    
#     pg.display.update()
