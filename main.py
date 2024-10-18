import pygame
from sys import exit
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Shot.containers = (shots, drawable, updatable)
    
    while True:
        screen.fill(color="black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if obj.detect_collision(player):
                print("Game over!")
                exit()
            for shot_obj in shots:
                if obj.detect_collision(shot_obj):
                    obj.split()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    
if __name__ == "__main__":
    main()