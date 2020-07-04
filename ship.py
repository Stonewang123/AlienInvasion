import pygame


class Ship:
    def __init__(self, screen, ai_settings):
        self._screen = screen
        self._image = pygame.image.load("./images/ship.bmp")
        self._rect = self._image.get_rect()
        self._screen_rect = self._screen.get_rect()
        self._rect.centerx = self._screen_rect.centerx
        self._rect.bottom = self._screen_rect.bottom
        self._ai_settings = ai_settings

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def get_screen(self):
        return self._screen

    def get_rect(self):
        return self._rect

    def get_image(self):
        return self._image

    def blitme(self):
        self._screen.blit(self._image, self._rect)

    def update(self):
        if self.move_right and self._rect.right < self._screen_rect.right:
            self._rect.centerx += self._ai_settings.get_ship_speed_factor()
        elif self.move_left and self._rect.left > self._screen_rect.left:
            self._rect.centerx -= self._ai_settings.get_ship_speed_factor()
        elif self.move_up and self._rect.top > self._screen_rect.top:
            self._rect.bottom -= self._ai_settings.get_ship_speed_factor()
        elif self.move_down and self._rect.bottom < self._screen_rect.bottom:
            self._rect.bottom += self._ai_settings.get_ship_speed_factor()
