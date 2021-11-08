import pygame
from Utils import Vector
from planet import Thing
import sys

pygame.init()

SIZE = WIDTH, HEIGHT = 640, 360
FPS = 30

WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Gravity Sim.")



def main():
    clock = pygame.time.Clock()
    run = True
    p = Thing(radius=20, mass=100, pos=Vector(320, 180))
    # p.apply_force(Vector(5000, 0))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]:
            p.apply_force(Vector(5000,0))
        
        if keys_pressed[pygame.K_d]:
            p.apply_force(Vector(-5000,0))

        WIN.fill((255, 255, 255))
        p.update()
        p.draw(WIN)
        print(f"Position: {p.pos}  Velocity: {p.velocity}  Acceleration: {p.acceleration}")
        

        pygame.display.update()
        

    pygame.quit()



if __name__ == "__main__":
    main()
