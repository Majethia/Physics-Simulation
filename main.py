import pygame
from Utils import Vector
from Things import Circle
from constansts import *

pygame.init()

FORCE = 2000

WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Physics Simulator.")

pygame.init()
pygame.font.init()
font = pygame.font.Font('DmMonoMedium-6Y4ex.ttf', 20)

def main():
    count = 0
    data = ""
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

        count += 1
        if count == 6:
            data = f"Position: {p.pos}  Velocity: {p.velocity}  Acceleration: {p.acceleration}"
            count = 0
        textsurface = font.render(data, False, (0,0,0))
        WIN.blit(textsurface,(10, 10))

        pygame.display.update()
        

    pygame.quit()



if __name__ == "__main__":
    main()
