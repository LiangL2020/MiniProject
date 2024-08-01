import pygame 
import lib 
from button import Button 

class End: 
    def __init__(self): 
        self.but_back = Button(600, 100, 100, 50, lib.WHITE, lib.GRAY, 'BACK', lib.BLACK, self.back_menu) 
    
    def back_menu(self): 
        lib.scene_manager = "MENU"
        lib.screen.fill(lib.BLACK)

    def end_scene(self): 
        self.but_back.draw(lib.screen)
        pygame.display.flip() 
    
