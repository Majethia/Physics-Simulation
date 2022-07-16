from Utils import Vector
from constansts import *
import pygame

class Thing:
    def __init__(self,size: int, mass: int, pos: Vector, friction_toggle: bool, shape: str, color: tuple[3]):
        self.size = size
        self.mass = mass
        self.pos = pos
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.force = Vector(0, 0)
        self.friction_toggle = friction_toggle
        self.force_reset = True
        self.shape = shape
        self.color = color

    def apply_force(self, force: Vector):
        self.force += force

    def apply_brakes(self):
        self.force -= self.velocity.unit_vector()*(self.mass*ACCELERATION_DUE_TO_GRAVITY*COEFFICIENT_OF_FRICTION)*5

    def update_force(self):
        self.force = Vector(0, 0)
        if self.friction_toggle:
            self.velocity.round()
            self.force -= self.velocity.unit_vector()*(self.mass*ACCELERATION_DUE_TO_GRAVITY*COEFFICIENT_OF_FRICTION)

    def update_acceleration(self):
        self.acceleration = self.force/self.mass

    def update_velocity(self):
        self.velocity += self.acceleration

    def update_position(self):
        if self.out_of_bounds(self.pos + (self.velocity)/10):
            self.pos += (self.velocity)/10

    def check_vibration(self):
        if self.velocity.magnitude() < 0.5:
            self.velocity = Vector(0, 0)

    def update(self):
        self.update_acceleration()
        self.update_velocity()
        self.update_position()
        self.check_vibration()

        self.update_force()

    def out_of_bounds(self, pos):
        if (0 + self.size) < pos.x < (WIDTH - self.size) and (0 + self.size) < pos.y < (HEIGHT - self.size):
            return True
        elif (0 + self.size) < pos.x < (WIDTH - self.size):
            y = self.velocity.y
            self.velocity.y = 0
            self.velocity += Vector(0, -y*self.mass)*COEFFICIENT_OF_RESTITUTION/self.mass
            return True
        elif (0 + self.size) < pos.y < (HEIGHT - self.size):
            x = self.velocity.x
            self.velocity.x = 0
            self.velocity += Vector(-x*self.mass, 0)*COEFFICIENT_OF_RESTITUTION/self.mass
            return True

        y = self.velocity.y
        self.velocity.y = 0
        x = self.velocity.x
        self.velocity.x = 0
        self.velocity += Vector(-x*self.mass, -y*self.mass)*COEFFICIENT_OF_RESTITUTION/self.mass      
        return False

    def draw(self, window):
        if self.shape == 'circle':
            pygame.draw.circle(window, self.color, (self.pos.x, self.pos.y), self.size)
        elif self.shape == 'square':
            pygame.draw.rect(window, self.color, pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))


class Player(Thing):
    def __init__(self, size: int, mass: int, pos: Vector, friction_toggle: bool, shape: str, controls: int, color: tuple[3]):
        super().__init__(size, mass, pos, friction_toggle, shape, color)
        self._controls = controls
    

    def control(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[CONTROLS[self._controls][0]]:
            self.apply_force(Vector(-FORCE, 0))
        
        if keys_pressed[CONTROLS[self._controls][1]]:
            self.apply_force(Vector(+FORCE, 0))

        if keys_pressed[CONTROLS[self._controls][2]]:
            self.apply_force(Vector(0, -FORCE))
        
        if keys_pressed[CONTROLS[self._controls][3]]:
            self.apply_force(Vector(0, +FORCE))

        if keys_pressed[CONTROLS[self._controls][4]]:
            self.apply_brakes()

