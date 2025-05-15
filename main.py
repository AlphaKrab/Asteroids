import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() #Initialized the game
    
    clock = pygame.time.Clock()
    
    dt = 0 #Delta Time used to keep track of FPS

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updateable, drawable)
    
    Player.containers = (updateable, drawable) # Sets the containers for Player to updatable and drawable
    
    Asteroid.containers = (asteroids, updateable, drawable) # Sets the cointainers for the asteroids
    
    AsteroidField.containers = (updateable)

    asteroid_feild = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_for_collisions(shot):
                    shot.kill()
                    asteroid.split()

        for asteroid in asteroids:
            if player.check_for_collisions(asteroid):
                print("Game Over!")
                sys.exit()
        
        screen.fill("black")
    
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
       
        dt = clock.tick(60) / 1000 #Converts dt into miliseconds and limits FPS to 60


if __name__ == "__main__":
    main()