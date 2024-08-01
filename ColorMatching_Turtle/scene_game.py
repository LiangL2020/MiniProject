import pygame 
import random
import lib 
from button import Button 

BLOCK_SIZE = 25 
ROWS, COLS = 3, 3
SQUARE_SIZE = lib.WIDTH // (COLS+2) 

class Game: 
    def __init__(self, turtle_left): 
        lib.score = 0
        self.num_turtle = turtle_left
        self.turtle_left = turtle_left 
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)] 
        self.add_tur = Button(600, 100, 100, 50, lib.WHITE, lib.GRAY, 15, 'add turtle', lib.BLACK, self.button_turtle)
        self.back_menu = Button(35, 550, 50, 25, lib.WHITE, lib.GRAY, 8, "Back", lib.BLACK, self.back_menu) 
        self.star_over = Button(100, 550, 50, 25, lib.WHITE, lib.GRAY, 8, "Restart", lib.BLACK, self.but_start) 

    def reset(self): 
        lib.score = 0
        self.turtle_left = self.num_turtle
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)] 
        
    # button to add turtle 
    def button_turtle(self): 
        # TODO: if color_wish make "ding~" 
        if self.turtle_left == 0: 
            lib.scene_manager = "END"
            lib.screen.fill(lib.BLACK)
            pass 
        color = random.choice(lib.COLORS) 
        action_done = False
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] is None:
                    self.board[row][col] = color
                    self.turtle_left -= 1
                    if color == lib.color_wish: 
                        lib.score += 1 
                        self.turtle_left += 1
                    action_done = True
                    break
            if action_done:
                break

    def back_menu(self): 
        lib.scene_manager = "MENU"
        lib.screen.fill(lib.BLACK)

    def but_start(self): 
        self.reset() 
        lib.screen.fill(lib.BLACK)

    def game_scene(self, check_interval): 
        self.add_tur.draw(lib.screen)
        self.back_menu.draw(lib.screen)
        self.star_over.draw(lib.screen)
        self.update_board() 
        self.update_screen()
        if self.check_full(): 
            lib.wait(check_interval)
            self.check_board(check_interval)  

    def check_full(self): 
        for row in range(ROWS):
            for col in range(COLS): 
                if self.board[row][col] == None: 
                    return False 
        return True 

    def check_empty(self): 
        for row in range(ROWS):
            for col in range(COLS): 
                if self.board[row][col] != None: 
                    return False 
        return True  

    def contains_pair(self, pairs, target_pair):
        reversed_pair = (target_pair[1], target_pair[0])
        return target_pair in pairs or reversed_pair in pairs

    def check_duplicates(self): 
        triples = [] 
        pairs = []
        included_coords = set()

        # triples 
        if self.board[0][0] == self.board[1][1] == self.board[2][2]: 
            included_coords.add((0, 0))
            included_coords.add((1, 1))
            included_coords.add((2, 2))
            triples.append(((0, 0), (1, 1), (2, 2)))
        if self.board[0][2] == self.board[1][1] == self.board[2][0]: 
            included_coords.add((0, 2))
            included_coords.add((1, 1))
            included_coords.add((2, 0))
            triples.append(((0, 2), (1, 1), (2, 0)))
        for i in range(ROWS): 
            if self.board[i][0] == self.board[i][1] == self.board[i][2]: 
                included_coords.add((i, 0))
                included_coords.add((i, 1))
                included_coords.add((i, 2))
                triples.append(((i, 0), (i, 1), (i, 2)))
            if self.board[0][i] == self.board[1][i] == self.board[2][i]: 
                included_coords.add((0, i))
                included_coords.add((1, i))
                included_coords.add((2, i))
                triples.append(((0, i), (1, i), (2, i)))
        
        # pairs 
        for row in range(ROWS): 
            for col in range(COLS): 
                color = self.board[row][col] 
                if color is not None: 
                    for row_match in range(ROWS): 
                        for col_match in range(COLS): 
                            if self.board[row_match][col_match] == color and not (row == row_match and col == col_match): 
                                new_pair = ((row, col), (row_match, col_match))
                                if not self.contains_pair(pairs, new_pair):
                                    if (row, col) not in included_coords and (row_match, col_match) not in included_coords:
                                        pairs.append(new_pair)
                                        included_coords.add((row, col))
                                        included_coords.add((row_match, col_match))
        return triples, pairs

    def check_board(self, check_interval): 
        # 考虑优先级，积分可调 
        # 1. 清空 +5 
        # 2. 三连 +3 
        # 3. 隐藏 +2 
        # 4. 许愿色 + 1 
        # 5. 对对碰 + 1  

        triples, pairs = self.check_duplicates()

        while triples: 
            for r, c in triples[0]: 
                self.board[r][c] = None
            lib.score += 3 
            self.turtle_left += 3 
            self.update_board()
            self.update_screen()
            lib.wait(lib.check_interval)
            triples = triples[1:]

        while pairs: 
            for r, c in pairs[0]: 
                self.board[r][c] = None
            lib.score += 1 
            self.turtle_left += 1 
            self.update_board()
            self.update_screen()
            lib.wait(check_interval)
            pairs = pairs[1:]

        if self.check_empty(): 
            lib.score += 5 
            self.turtle_left += 5 
            self.update_screen()

    # update board 
    def update_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                color = self.board[row][col] if self.board[row][col] else lib.WHITE
                pygame.draw.rect(lib.screen, color, (col * SQUARE_SIZE + BLOCK_SIZE, row * SQUARE_SIZE + BLOCK_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        for col in range(COLS + 1):
            pygame.draw.line(lib.screen, lib.BLACK, (col * SQUARE_SIZE + BLOCK_SIZE, BLOCK_SIZE), (col * SQUARE_SIZE + BLOCK_SIZE, 3 * SQUARE_SIZE + BLOCK_SIZE))
        for row in range(ROWS + 1):
            pygame.draw.line(lib.screen, lib.BLACK, (BLOCK_SIZE, row * SQUARE_SIZE + BLOCK_SIZE), (3 * SQUARE_SIZE + BLOCK_SIZE, row * SQUARE_SIZE + BLOCK_SIZE))
        pygame.display.flip() 

    # display score board  
    def update_screen(self): 
        col_pos = 490 

        font_l = pygame.font.SysFont('sfnsmono', 18) 
        text_title = font_l.render("Score Board", True, lib.WHITE)
        text_rect = text_title.get_rect() 
        text_rect.center = (650, 300)
        lib.screen.blit(text_title, text_rect)
        pygame.draw.line(lib.screen, lib.WHITE, (600, 315), (705, 315), 2)

        pygame.draw.rect(lib.screen, lib.BLACK, (580, 320, 160, 60))
        font_s = pygame.font.SysFont('sfnsmono', 15) 
        text_tur = font_s.render("Turtle Left: " + str(self.turtle_left), True, lib.WHITE)
        text_sco = font_s.render("Score: " + str(lib.score), True, lib.WHITE)
        text_rect_tur = text_tur.get_rect() 
        text_rect_sco = text_sco.get_rect() 
        text_rect_tur.center = (650, 335)
        text_rect_sco.center = (650, 360)
        lib.screen.blit(text_tur, text_rect_tur)
        lib.screen.blit(text_sco, text_rect_sco)

        text_wis = font_s.render("Color Wished: ", True, lib.WHITE)
        text_rect_wis = text_wis.get_rect() 
        text_rect_wis.center = (600, 550)
        lib.screen.blit(text_wis, text_rect_wis)
        pygame.draw.rect(lib.screen, lib.color_wish, (660, 525, 50, 50))

        for i, color in enumerate(lib.COLORS): 
            pygame.draw.rect(lib.screen, color, (col_pos + BLOCK_SIZE + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip() 

    