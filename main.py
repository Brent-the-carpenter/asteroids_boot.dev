import pygame

from constants import *    

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    start = pygame.init()
    running = True  
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT  ))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black" , rect=None)
        pygame.display.flip()
if __name__ == "__main__":
    main()
