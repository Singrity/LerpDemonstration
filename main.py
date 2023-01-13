import pygame
from particle import Particle
from util import lerp


class Game:

    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.particles = []

        self.box_rect1 = pygame.Rect(100, 100, 100, 200)
        self.box_rect2 = pygame.Rect(300, 100, 100, 200)
        self.box_rect3 = pygame.Rect(500, 100, 100, 200)
        self.box_direction = pygame.Vector2(0, 0)



        self.pressed = False

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
                    for _ in range(30):
                        particle = Particle(pygame.mouse.get_pos(), (20, 20), (255, 255, 255), 1.5, [self.box_rect1, self.box_rect2, self.box_rect3])
                        self.particles.append(particle)
                        print(len(self.particles))
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.pressed = False

    def update(self, dt):

        #particle = Particle(pygame.mouse.get_pos(), (20, 20), (255, 255, 255), 1000, [self.box_rect1, self.box_rect2, self.box_rect3])

        #self.particles.append(particle)

        for particle in self.particles.copy():

            particle.update(dt)

            if not particle.alive:
                self.particles.remove(particle)

        #self.box_rect.x += self.box_direction.x

        # if self.box_rect.right > 800 or self.box_rect.left < 0:
        #     self.box_direction *= -1

        #print(len(self.particles))

    def draw(self):
        self.screen.fill((0, 0, 0))
        for particle in self.particles.copy():
            particle.draw()

        pygame.draw.rect(self.screen, (255, 0, 0), self.box_rect1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.box_rect2)
        pygame.draw.rect(self.screen, (255, 0, 0), self.box_rect3)

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()


