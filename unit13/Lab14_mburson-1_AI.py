import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
  """Overall class to manage game assets and behavior."""

  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode(self.settings.resolution)
    self.clock = pygame.time.Clock()
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    pygame.display.set_caption(self.settings.game_name)
    self.aliens = pygame.sprite.Group()
    self.stats = GameStats(self)
    self.sb = Scoreboard(self)
    self._create_fleet()
     # Start Alien Invasion in an inactive state.
    self.game_active = False
    # Make the Play button.
    self.play_button = Button(self, "Play")

  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
            self._fire_bullet()  

  def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
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
     """Create an alien and place it in the fleet."""
     new_alien = Alien(self)
     new_alien.y = y_position
     new_alien.rect.y = y_position
     new_alien.rect.x = x_position
     self.aliens.add(new_alien)

  def _update_aliens(self):
     """Check if the fleet is at an edge, then update positions."""
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
             alien.rect.x += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


  def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

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
            pygame.mouse.set_visible(True)
          
        

  def _check_keyup_events(self, event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type ==  pygame.KEYUP:
        self._check_keyup_events(event)
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self._check_play_button(mouse_pos)

  def _update_bullets(self):
     """Update position of bullets and get rid of old bullets."""
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
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

  def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    self.ship.blit_me()
    self.aliens.draw(self.screen)
    # Draw the score information.
    self.sb.show_score()

    for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    if not self.game_active:
      self.play_button.draw_button()
    pygame.display.flip()
    
        
  
  def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
          # Reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
        
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      if self.game_active:
          self.ship.update()
          self._update_bullets()
          self._update_aliens()
          
      
      self._update_screen()
      self.clock.tick(self.settings.frame_rate)          

if __name__ == '__main__':
  """Make a game instance, and run the game."""
  ai = AlienInvasion()
  ai.run_game()