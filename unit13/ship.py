import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
  """A class to manage the ship."""
  def __init__(self, ai_game):
    """Initialize the ship and set its starting position."""
    super().__init__()
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    self.image = pygame.image.load('unit12/resources/ship.bmp')
    self.rotated_image = pygame.transform.rotate(self.image, 90)
    self.rect = self.image.get_rect()

    self.rect.midright = self.screen_rect.midright

    self.moving_right = False
    self.moving_left = False

    self.settings = ai_game.settings

    self.y = float(self.rect.y)

  def update(self):
    """Update the ship's position based on movement flags."""
    if self.moving_right and self.rect.bottom < self.screen_rect.bottom:
      self.y += self.settings.ship_speed
    elif self.moving_left and self.rect.top > self.screen_rect.top:
      self.y -= self.settings.ship_speed

    self.rect.y = self.y

  def blit_me(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.rotated_image, self.rect)

  def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)