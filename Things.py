from Utils import Vector
from constansts import *
import pygame


class Thing:
    def __init__(self, radius: int, mass: int, pos: Vector, friction_toggle: bool = True):
        self.radius = radius
        self.mass = mass
        self.pos = pos
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.force = Vector(0, 0)
        self.friction_toggle = friction_toggle

    def draw(self, window):
        pygame.draw.circle(window, (255,0,0), (self.pos.x, self.pos.y), self.radius)

    def apply_force(self, force: Vector):
        self.force += force

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

    def update(self):
        self.update_acceleration()
        self.update_velocity()
        self.update_position()
        self.update_force()

    def out_of_bounds(self, pos):
        if 0 < pos.x < 640 and 0 < pos.y < 360:
            return True
        elif 0 < pos.x < 640:
            self.velocity.y = 0
            return True
        elif 0 < pos.y < 360:
            self.velocity.x = 0
            return True
        return False