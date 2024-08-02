import pygame 
import lib 
from button import Button 

class End: 
    def __init__(self): 
        self.but_back = Button(600, 100, 100, 50, lib.WHITE, lib.GRAY, 15, 'BACK', lib.BLACK, self.back_menu) 
    
    def back_menu(self): 
        lib.scene_manager = "MENU"
        lib.screen.fill(lib.BLACK)

    def end_scene(self): 
        self.but_back.draw(lib.screen)
        self.display()
        pygame.display.flip() 

    def display(self): 
        font_l = pygame.font.SysFont('sfnsmono', 20) 
        text_dis = font_l.render("Your turtle ran out!", True, lib.WHITE)
        text_rect_dis = text_dis.get_rect() 
        text_rect_dis.center = (400, 280)
        lib.screen.blit(text_dis, text_rect_dis)
        text_sco = font_l.render("You win " + str(lib.score) + " turtles!", True, lib.WHITE)
        text_rect_sco = text_sco.get_rect() 
        text_rect_sco.center = (400, 320)
        lib.screen.blit(text_sco, text_rect_sco)
        pygame.display.flip() 
    
