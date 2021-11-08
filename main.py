import pygame
from Utils import Vector
from Things import Thing

pygame.init()

SIZE = WIDTH, HEIGHT = 640, 360
FPS = 60

WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Physics Simulator.")



def main():
    clock = pygame.time.Clock()
    run = True
    p = Thing(radius=20, mass=200, pos=Vector(320, 180))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]:
            p.apply_force(Vector(-100, 0))
        
        if keys_pressed[pygame.K_d]:
            p.apply_force(Vector(+100, 0))

        if keys_pressed[pygame.K_w]:
            p.apply_force(Vector(0, -100))
        
        if keys_pressed[pygame.K_s]:
            p.apply_force(Vector(0, +100))

        WIN.fill((255, 255, 255))
        p.update()
        p.draw(WIN)
        print(f"Position: {p.pos}  Velocity: {p.velocity}  Acceleration: {p.acceleration}")
        

        pygame.display.update()
        

    pygame.quit()



if __name__ == "__main__":
    main()
