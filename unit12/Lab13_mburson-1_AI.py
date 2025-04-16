import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats

class AlienInvasion:

  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode(self.settings.resolution)
    self.clock = pygame.time.Clock()
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    pygame.display.set_caption(self.settings.game_name)
    self.aliens = pygame.sprite.Group()
    self.stats = GameStats(self)
    self._create_fleet()
    self.game_active = True

  def _check_keydown_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
            self._fire_bullet()  

  def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)   
  
  def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        self.aliens.add(alien)
        alien_width = alien.rect.width
        
        current_y, current_x = alien_width, alien_height
        
        
           
        while current_x < (self.settings.screen_width - 2 * alien_width):
            while current_y < (self.settings.screen_height - 3 * alien_height):
                
                self._create_alien(current_y, current_x)
                current_y += 2 * alien_height
            

            current_x += 2 * alien_width
            current_y  = alien_height



  def _create_alien(self, y_position, x_position):
     new_alien = Alien(self)
     new_alien.y = y_position
     new_alien.rect.y = y_position
     new_alien.rect.x = x_position
     self.aliens.add(new_alien)

  def _update_aliens(self):
     self.aliens.update()
     self._check_fleet_edges()
     if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
     
     self._check_aliens_right()

  def _check_aliens_right(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.settings.screen_width:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

  def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

  def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
             alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


  def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False

  def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type ==  pygame.KEYUP:
        self._check_keyup_events(event)

  def _update_bullets(self):
     self.bullets.update()
     for bullet in self.bullets.copy():
        if bullet.rect.left <= 0:
            self.bullets.remove(bullet)
     self._check_bullet_alien_collisions()

  def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blit_me()
    self.aliens.draw(self.screen)
    for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    pygame.display.flip()
        
  

  def run_game(self):
    while True:
      self._check_events()
      if self.game_active:
        self.ship.update()
        self._update_bullets()
        self._update_aliens()
      
      self._update_screen()
      self.clock.tick(self.settings.frame_rate)          

if __name__ == '__main__':
  
  # Make a game instance, and run the game.
  ai = AlienInvasion()
  ai.run_game()