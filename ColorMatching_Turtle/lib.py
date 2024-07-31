import pygame 

def wait(wait_ms):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < wait_ms:
        # handle events to keep the application responsive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()