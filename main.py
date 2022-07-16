import pygame
from Utils import Vector
from Things import Player
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
    p = Player(size = 20, mass=1000, pos=Vector(WIDTH/2, HEIGHT/2), friction_toggle=True, shape='circle', color = (255, 0, 0), controls = 0)
    q = Player(size = 20, mass=1000, pos=Vector(WIDTH/2, HEIGHT/2), friction_toggle=True, shape='circle', color = (0, 255, 0), controls = 1)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill((255, 255, 255))

        q.control()
        p.control()

        p.update()
        q.update()

        p.draw(WIN)
        q.draw(WIN)

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
