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
            self.force -= self.velocity.unit_vector()*(self.mass*ACCELERATION_DUE_TO_GRAVITY*COEFFICIENT_OF_FRICTION)

    def update_acceleration(self):
        self.acceleration = self.force/self.mass
        # print(f"Acceleration: {self.acceleration}", end=" ")

    def update_velocity(self):
        self.velocity += self.acceleration
        # print(f"Velocity: {self.velocity}", end=" ")

    def update_position(self):
        self.pos += (self.velocity)/10
        # print(f"Position: {self.pos}")

    def update(self):
        self.update_acceleration()
        self.update_velocity()
        self.update_position()
        self.update_force()
        
