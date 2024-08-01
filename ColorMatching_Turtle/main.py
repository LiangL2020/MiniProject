### 
# Liang Lu - Color Matching Turtle Mini Game (碰碰龟-简易版)
# Start: 7/28/2024 
### 

import pygame
import random
import lib 
from button import Button 
from scene_menu import Menu 
from scene_game import Game 
from scene_end import End 

# TODO: 
#  1. make scenes different classes for organization [CHECK]
#  2. make color blocks turtles (or something else)
#  3. hidden color (隐藏色) 
#  4. if color_wish make "ding~" when adding turtle (button click) 
#  5. end game if out of turtles [CHECK]
#  6. start over button 
#  7. make button not valid when scene changed [CHECK]

if __name__ == "__main__": 
    running = True 
    lib.screen.fill(lib.BLACK)

    menu = Menu()
    game = Game(15)
    end = End() 

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
            end.but_back.check_click(event)
        
        if lib.scene_manager == "GAME": 
            menu.start_game.valid = False 
            game.add_tur.valid = True 
            end.but_back.valid = False 
            game.game_scene(lib.check_interval) 
        elif lib.scene_manager == "END": 
            menu.start_game.valid = False 
            game.add_tur.valid = False 
            end.but_back.valid = True 
            end.end_scene()
        else: 
            if lib.scene_manager != "MENU": 
                print("INVALID SCENE") 
            menu.start_game.valid = True 
            game.add_tur.valid = False 
            end.but_back.valid = False 
            menu.menu_scene() 

    pygame.quit() 
