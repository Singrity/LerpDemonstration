import pygame
from util import lerp, f


class Game:

    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.color_surf = pygame.Surface((600, 70))

        self.ball_rect = pygame.Rect(0, 245 + 25, 20, 20)
        #self.ball_rect.center = (10, 300 - 10)

        self.ball_vel = pygame.Vector2(0, 0)
        self.ball_direction = pygame.Vector2(1, 0)
        self.ball_pos = pygame.Vector2(120, 300 - 10)
        self.ball_target_pos = pygame.Vector2(680, 300 - 10)


        # self.min_color = (230, 239, 233)
        # self.max_color = (143, 131, 137)
        #
        # self.current_r = 230
        # self.target_r = 143
        # self.current_g = 239
        # self.target_g = 131
        # self.current_b = 233
        # self.target_b = 137

        # self.min_color = (0, 0, 0)
        # self.max_color = (255, 255, 255)
        #
        self.current_r = 0
        self.target_r = 255
        self.current_g = 0
        self.target_g = 123
        self.current_b = 0
        self.target_b = 4

        self.time = 0

        self.pos_x = 0
        self.target_pos_x = 600

    def run(self):
        while self.running:
            self.clock.tick()
            time_passed_ms = self.clock.get_time()
            time_passed_s = time_passed_ms / 1000.

            #print(time_passed_s, time_passed_ms)

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

    def gradient_lerp(self, dt):
        self.target_pos_x = self.ball_target_pos.x - 100
        for y in range(self.color_surf.get_size()[1]):
            self.color_surf.set_at((int(self.pos_x), y), (int(self.current_r), int(self.current_g), int(self.current_b)))

        self.time += dt
        self.pos_x = lerp(self.pos_x, self.target_pos_x, f(dt))
        #print(self.target_pos_x, self.pos_x)

        self.current_r = lerp(self.current_r, self.target_r, (self.pos_x / 600) * dt)
        self.current_g = lerp(self.current_g, self.target_g, (self.pos_x / 600) * dt)
        self.current_b = lerp(self.current_b, self.target_b, (self.pos_x / 600) * dt)

        if abs(self.current_r - self.target_r) <= 2:

            print(self.current_r, self.target_r)


        #print(int(self.current_r), int(self.current_g), int(self.current_b), int(self.target_r), int(self.target_g), int(self.target_b))

    def update(self, dt):
        #print(dt)
        self.gradient_lerp(dt)
        K = 1.0 - (0.9 ** (dt * 1000.))

        self.ball_pos.x = lerp(self.ball_pos.x, self.ball_target_pos.x, f(dt))
        self.ball_rect.x = self.ball_pos.x * self.ball_direction.x

        if self.ball_pos.x >= self.ball_target_pos.x - 1:
            #self.ball_direction.x *= -1
            self.ball_target_pos.x = 120
        if self.ball_pos.x <= self.ball_target_pos.x + 1:
            self.ball_target_pos.x = 680




    def draw(self):
        self.screen.fill((0, 0, 0))
        #pygame.draw.rect(self.screen, (255, 255, 255), [100, 245, 600, 70], 1)
        #self.color_surf.fill((0, 0, 0))
        self.screen.blit(self.color_surf, (100, 245))
        pygame.draw.circle(self.screen, (255, 255, 255), self.ball_rect.center, self.ball_rect.width / 2, 1)

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

