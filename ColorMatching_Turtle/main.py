import pygame
import random
import lib 
from button import Button 
from scene_menu import Menu 
from scene_game import Game 

if __name__ == "__main__": 
    running = True 
    lib.screen.fill(lib.BLACK)

    menu = Menu()
    game = Game(15)

    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.MOUSEBUTTONUP: 
                x, y = event.pos 
                if lib.scene_manager == "MENU": 
                    menu.handle_color_wish(x, y, 75)
            menu.start_game.check_click(event)
            game.add_tur.check_click(event)
        
        if lib.scene_manager == "GAME": 
            game.game_scene(lib.check_interval) 
        elif lib.scene_manager == "LOSE": 
            pass 
        elif lib.scene_manager == "WIN": 
            pass 
        else: 
            if lib.scene_manager != "MENU": 
                print("INVALID SCENE") 
            menu.menu_scene() 

    pygame.quit() 
