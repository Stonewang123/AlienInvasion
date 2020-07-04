class Settings:
    def __init__(self):
        self._screen_width = 1280
        self._screen_height = 720
        self._bg_color = (250, 250, 250)

        self._ship_speed_factor = 1.5

        self._bullet_speed_factor = 1
        self._bullet_width = 3
        self._bullet_height = 15
        self._bullet_color = (60, 60, 60)
        self._bullets_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_factor = 10
        # 1->right -1->left
        self.fleet_direction = 1

    def get_width(self):
        return self._screen_width

    def get_height(self):
        return self._screen_height

    def get_bg_color(self):
        return self._bg_color

    def get_ship_speed_factor(self):
        return self._ship_speed_factor

    def get_bullet_speed_factor(self):
        return self._bullet_speed_factor

    def get_bullet_width(self):
        return self._bullet_width

    def get_bullet_height(self):
        return self._bullet_height

    def get_bullet_color(self):
        return self._bullet_color

    def get_bullets_allowed(self):
        return self._bullets_allowed

    def get_alien_speed_factor(self):
        return self._alien_speed_factor

