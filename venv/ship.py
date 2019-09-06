import pygame

class Ship():
    def __init__(self, ai_settings,screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx-=self.ai_settings.ship_speed_factor
    def blitme(self):
        self.screen.blit(self.image, self.rect)