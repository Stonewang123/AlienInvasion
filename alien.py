import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges_lf(self):
        screen_right = self.screen.get_rect().right

        if self.rect.right >= screen_right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False

    def check_edges_td(self):

        screen_bottom = self.screen.get_rect().bottom
        if self.rect.bottom >= screen_bottom - 144:
            self.ai_settings.fleet_drop_factor = -10
            return True
        elif self.rect.top <= 0:
            self.ai_settings.fleet_drop_factor = 10
            return True
        else:
            return False

