import pygame
from util import *
import random

class FireParticle:
    def __init__(self, pos, size, color, collision_rects=None):
        self.pos = pygame.Vector2(pos)
        self.size = pygame.Vector2(size)
        self.speed = pygame.Vector2(100, 100)
        self.color = color
        
        self.collision_rects = collision_rects
        self.g = 0.6
        self.mass = 1

        self.rect = pygame.Rect(self.pos, size)
        self.rect.center = self.pos

        self.min_width = 1
        self.min_height = 1
        self.max_width = 100
        self.max_height = 100

        self.target_width = 1
        self.target_height = 1

        self.direction = pygame.Vector2(random.uniform(-1, 1), -1)

        self.current_time = 0

        self.alive = True
        
    def compute_force(self):
        return pygame.Vector2(0, self.mass * self.g)

    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.circle(screen, self.color, self.rect.center, self.rect.width)

    def apply_gravity(self, dt):
        self.direction.y = lerp(self.direction.y, 1, dt)
        self.g = 9.8
        self.mass = 0.5

    def check_collision(self):

        if self.rect.left < 0 or self.rect.right > 800:
            self.direction.x *= -1
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.direction.y *= -1

        if self.collision_rects:
            for rect in self.collision_rects:
                if self.rect.colliderect(rect):
                    if abs(rect.top - self.rect.bottom) < 10 and self.direction.y > 0:
                        self.direction.y *= -1
                    elif abs(rect.bottom - self.rect.top) < 10 and self.direction.y < 0:
                        self.direction.y *= -1

                    if abs(rect.left - self.rect.right) < 10 and self.direction.x > 0:
                        self.direction.x *= -1
                    elif abs(rect.right - self.rect.left) < 10 and self.direction.x < 0:
                        self.direction.x *= -1

    def update(self, dt):  # dt in seconds
    
        #self.apply_gravity(dt)
    
        #force = self.compute_force()
        #acceleration = pygame.Vector2(force.x / self.mass, force.y / self.mass)
        #self.speed.x += acceleration.x * dt
        #self.speed.y += acceleration.y * dt
    
        #print(dt)
        if self.rect.width <= self.target_width:
            self.alive = False

        self.size.x = lerp(self.size.x, self.target_width, f(dt))
        self.size.y = lerp(self.size.y, self.target_height, f(dt))

        #self.speed.x = lerp(self.speed.x, 0, f(dt))
        #self.speed.y = lerp(self.speed.y, 0, f(dt))

        self.pos.x = lerp(self.pos.x, self.pos.x + random.randint(-100, 100), f(dt))
        self.pos.y = lerp(self.pos.y, self.pos.y + 20 * self.direction.y, f(dt))

        self.rect.size = (self.size.x, self.size.y)
        self.rect.x, self.rect.y = (self.pos.x, self.pos.y)
        #print(self.rect.size)

        self.rect.center = self.pos

        #self.check_collision()
        #self.apply_gravity(dt)
        