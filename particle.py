import pygame
from util import lerp
import random


class Particle:

    def __init__(self, pos, size, color, life, collision_rects=None):
        self.pos = pygame.Vector2(pos)
        self.size = pygame.Vector2(size)
        self.rect = pygame.Rect(self.pos, size)
        self.rect.center = self.pos
        self.speed = pygame.Vector2(1, 0)
        self.direction = pygame.Vector2(1, 1)
        self.color = color
        self.collision_rects = collision_rects

        self.min_width = 1
        self.min_height = 1
        self.max_width = 100
        self.max_height = 100

        self.target_width = 1
        self.target_height = 1

        self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        self.life = life
        self.time = 0

        self.alive = True

    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, self.color, self.rect)

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

    def update(self, dt):
        K_size = 0.1
        K_size = 1.0 - K_size ** dt

        K_pos = 0.02
        K_pos = 1.0 - K_pos ** dt

        self.time += dt * 1000.
        if self.time >= self.life:
            pass
            self.alive = False

        current_width = lerp(self.rect.width, self.target_width, K_size)
        current_height = lerp(self.rect.height, self.target_height, K_size)

        current_pos_x = lerp(self.pos.x, self.pos.x + 30 * self.direction.x, K_pos)
        current_pos_y = lerp(self.pos.y, self.pos.y + 30 * self.direction.y, K_pos)

        #print(self.rect)
        self.rect.size = (current_width, current_height)
        self.pos = pygame.Vector2(current_pos_x, current_pos_y)
        self.rect.center = self.pos

        # if abs(current_width - self.target_width) < self.target_width / current_width or\
        #         abs(current_height - self.target_height) < self.target_height / current_height:
        #     self.target_width = self.min_width if self.target_width == self.max_width else self.max_width
        #     self.target_height = self.min_height if self.target_height == self.max_height else self.max_height



        self.check_collision()













