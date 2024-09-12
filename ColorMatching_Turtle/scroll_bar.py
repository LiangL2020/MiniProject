# import pygame

# class ScrollBar:
#     def __init__(self, x, y, width, height, color, scroll_color, action=None):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.color = color
#         self.scroll_color = scroll_color
#         self.action = action 
#         self.valid = False 

#     def draw(self, screen):
#         mouse_pos = pygame.mouse.get_pos()

#     def check_click(self, event):
#         if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
#             if self.action and self.valid:
#                 self.action()

import pygame

class ScrollBar:
    def __init__(self, x, y, width, height, color, scroll_init_pos, scroll_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.init_pos = scroll_init_pos
        self.scroll_color = scroll_color
        self.action = action
        self.scroll_rect = pygame.Rect(x + scroll_init_pos, y - 5, 10, height + 10) 
        self.dragging = False
        self.valid = False
        self.min_y = y 
        self.max_y = y + height - self.scroll_rect.height 

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect) 
        pygame.draw.rect(screen, self.scroll_color, self.scroll_rect) 

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.scroll_rect.collidepoint(event.pos):
                self.dragging = True
                self.valid = True
                print("trueee")
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
            if self.valid and self.action:
                self.action()
            self.valid = False

    def update(self):
        if self.dragging:
            mouse_x = pygame.mouse.get_pos()[0]
            # Update the scroll_rect position within the min_x and max_x bounds
            self.scroll_rect.x = max(self.min_x, min(self.max_x, mouse_x - self.scroll_rect.width // 2))

    def get_value(self):
        """Returns a value between 0 and 1 indicating the scroll position."""
        return (self.scroll_rect.y - self.min_y) / (self.max_y - self.min_y)
