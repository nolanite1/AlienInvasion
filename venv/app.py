import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    # Initialize a game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,ship,screen)


run_game()