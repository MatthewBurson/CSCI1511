class Settings:

  def __init__(self):
    self.game_name = 'Alien Invasion'
    self.screen_width = 1200
    self.screen_height = 800
    self.resolution = (self.screen_width, self.screen_height)
    self.bg_color = (230, 230, 230)
    self.frame_rate = 60
    self.ship_speed = 1.5
    self.ship_limit = 3
    self.bullet_speed = 2.5
    self.bullet_width = 15
    self.bullet_height = 500
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 3
    self.alien_speed = 1.0
    self.fleet_drop_speed = 10
    self.fleet_direction = 1