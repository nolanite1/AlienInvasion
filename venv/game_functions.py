import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx+=5
            elif event.key == pygame.K_LEFT:
                ship.rect.centerx-=5


def update_screen(ai_settings,ship,screen):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()


