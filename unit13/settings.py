class Settings:
  """A class to store all settings for Alien Invasion."""
  def __init__(self):
    """Initialize the game's settings."""
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
    self.bullet_height = 3
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 3
    self.alien_speed = 1.0
    self.fleet_drop_speed = 15
    self.fleet_direction = 1

    # How quickly the game speeds up
    self.speedup_scale = 1.1
    self.initialize_dynamic_settings()
    # How quickly the alien point values increase
    self.score_scale = 1.5

  def initialize_dynamic_settings(self):
      """Initialize settings that change throughout the game."""
      self.ship_speed = 1.5
      self.bullet_speed = 2.5
      self.alien_speed = 1.0
      self.alien_points = 50


      # fleet_direction of 1 represents right; -1 represents left.
      self.fleet_direction = 1
  def increase_speed(self):
      """Increase speed settings and alien point values."""
      self.ship_speed *= self.speedup_scale
      self.bullet_speed *= self.speedup_scale
      self.alien_speed *= self.speedup_scale
      self.alien_points = int(self.alien_points * self.score_scale)
      print(self.alien_points)