from Utils import Vector
from constansts import *
import pygame

class Thing:
    def __init__(self, radius: int, mass: int, pos: Vector):
        self.radius = radius
        self.mass = mass
        self.pos = pos
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.force = Vector(0, 0)

    def draw(self, window):
        pygame.draw.circle(window, (255,0,0), (self.pos.x, self.pos.y), self.radius)

    def apply_force(self, force: Vector):
        self.force += force

    def update_force(self):
        self.force = Vector(0, 0)

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
        
