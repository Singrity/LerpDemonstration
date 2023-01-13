import pygame
from util import lerp, f
import random


class Particle:

    def __init__(self, pos, size, color, life_time, collision_rects=None):
        self.pos = pygame.Vector2(pos)
        self.size = pygame.Vector2(size)
        self.speed = pygame.Vector2(100, 100)
        self.direction = pygame.Vector2(1, 1)
        self.color = color
        self.collision_rects = collision_rects
        self.g = 0
        self.mass = 0

        self.rect = pygame.Rect(self.pos, size)
        self.rect.center = self.pos

        self.min_width = 1
        self.min_height = 1
        self.max_width = 100
        self.max_height = 100

        self.target_width = 1
        self.target_height = 1

        self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        self.life_time = life_time
        self.current_time = 0

        self.alive = True

    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, self.color, self.rect)

    def apply_gravity(self, dt):
        self.direction.y = lerp(self.direction.y, 1, dt)
        self.g = 1
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
        #print(dt)
        if self.rect.width <= 1:
            self.alive = False

        self.size.x = lerp(self.size.x, self.target_width, f(dt))
        self.size.y = lerp(self.size.y, self.target_height, f(dt))

        #self.speed.x = lerp(self.speed.x, 0, f(dt))
        #self.speed.y = lerp(self.speed.y, 0, f(dt))

        self.pos.x = lerp(self.pos.x, self.pos.x + self.speed.x * self.direction.x * self.g * self.mass, f(dt))
        self.pos.y = lerp(self.pos.y, self.pos.y + self.speed.y * self.direction.y * self.g * self.mass, f(dt))

        self.rect.size = (self.size.x, self.size.y)
        self.rect.x, self.rect.y = (self.pos.x, self.pos.y)
        #print(self.rect.size)

        self.rect.center = self.pos

        self.check_collision()
        self.apply_gravity(dt)








