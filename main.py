import pygame
from Utils import Vector
from Things import Circle, Square
from constansts import *

pygame.init()

FORCE = 2000

WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Physics Simulator.")



def main():
    clock = pygame.time.Clock()
    run = True
    p = Circle(20, mass=1000, pos=Vector(WIDTH/2, HEIGHT/2), friction_toggle=True)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]:
            p.apply_force(Vector(-FORCE, 0))
        
        if keys_pressed[pygame.K_d]:
            p.apply_force(Vector(+FORCE, 0))

        if keys_pressed[pygame.K_w]:
            p.apply_force(Vector(0, -FORCE))
        
        if keys_pressed[pygame.K_s]:
            p.apply_force(Vector(0, +FORCE))

        if keys_pressed[pygame.K_SPACE]:
            p.apply_brakes()

        WIN.fill((255, 255, 255))
        p.update()
        p.draw(WIN)

        print(f"Position: {p.pos}  Velocity: {p.velocity}  Acceleration: {p.acceleration}")
        

        pygame.display.update()
        

    pygame.quit()



if __name__ == "__main__":
    main()
