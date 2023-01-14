import pygame
from particle import Particle
from fire_particle import FireParticle
from util import lerp
import random


class Game:

    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.particles = []
        
        self.fire_particles = []

        self.box_rect1 = pygame.Rect(100, 100, 100, 200)
        self.box_rect2 = pygame.Rect(300, 100, 100, 200)
        self.box_rect3 = pygame.Rect(500, 100, 100, 200)
        self.box_direction = pygame.Vector2(0, 0)
        
        self.torch = pygame.image.load("torch.png")
        self.torch.set_colorkey((0, 255, 0))
        
        print(self.torch)



        self.spawning_particles = False
        self.firing = False

    def run(self):
        while self.running:
            self.clock.tick()
            time_passed_ms = self.clock.get_time()
            time_passed_s = time_passed_ms / 1000.
            #print(time_passed_ms)
            self.events()
            self.update(time_passed_s)
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.spawning_particles = True
                if event.button == 3:
                    self.firing = True
                    
                        
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.spawning_particles = False
                if event.button == 3:
                    self.firing = False
                    
    def create_fire_particles(self, pos):
        colors = [(255,0,0), (255,90,0), (255,154,0), (255,206,0), 	(255,232,8)]
        for color in colors:
            particle = FireParticle(pos, (5, 5), color)
            self.fire_particles.append(particle)
            

    def update(self, dt):
        if self.firing:
           self.create_fire_particles(pygame.mouse.get_pos())
        if self.spawning_particles:
            for _ in range(5):
                particle = Particle(pygame.mouse.get_pos(), (20, 20), (255, 255, 255), 1.5, [self.box_rect1, self.box_rect2, self.box_rect3])
                self.particles.append(particle)
                
        if random.randint(0, 20) == 20:
            self.create_fire_particles((432, 420))

        for particle in self.particles.copy():
            particle.update(dt)
            if not particle.alive:
                self.particles.remove(particle)
        
        for fire_particle in self.fire_particles.copy():
        
            fire_particle.update(dt)
            if not fire_particle.alive:
                self.fire_particles.remove(fire_particle)

        #self.box_rect.x += self.box_direction.x

        # if self.box_rect.right > 800 or self.box_rect.left < 0:
        #     self.box_direction *= -1

        #print(len(self.particles))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.torch = pygame.transform.scale(self.torch, (64, 64))
        self.screen.blit(self.torch, (400, 400))
        for particle in self.particles.copy():
            particle.draw()
            
        for fire_particle in self.fire_particles.copy():
            fire_particle.draw()

        pygame.draw.rect(self.screen, (255, 0, 0), self.box_rect1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.box_rect2)
        pygame.draw.rect(self.screen, (255, 0, 0), self.box_rect3)
        
        

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()


