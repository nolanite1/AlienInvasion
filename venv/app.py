import pygame
import sys


def run_game():
    # Initialize a game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230,230,230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()


run_game()