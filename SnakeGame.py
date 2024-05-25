import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 25)
        self.colors = {
            "white": (255, 255, 255),
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "black": (0, 0, 0)
        }
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.food_position = [random.randrange(1, 60) * 10, random.randrange(1, 40) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

    def display_score(self):
        score_text = self.font.render("Score: " + str(self.score), True, self.colors["white"])
        self.screen.blit(score_text, [0, 0])

    def display_snake(self):
        for position in self.snake_body:
            pygame.draw.rect(self.screen, self.colors["green"], pygame.Rect(position[0], position[1], 10, 10))

    def display_food(self):
        pygame.draw.rect(self.screen, self.colors["red"], pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))

    def game_over(self):
        # Implement game over screen here
        pygame.quit()
        quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    self.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    self.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    self.change_to = 'RIGHT'

    def run_game(self):
        while True:
            self.handle_events()
            self.change_direction()
            self.move_snake()
            self.check_collisions()
            self.update_screen()

    def change_direction(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def move_snake(self):
        if self.direction == 'UP':
            self.snake_position[1] -= 10
        if self.direction == 'DOWN':
            self.snake_position[1] += 10
        if self.direction == 'LEFT':
            self.snake_position[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_position[0] += 10
        self.snake_body.insert(0, list(self.snake_position))

    def check_collisions(self):
        if self.snake_position[0] == self.food_position[0] and self.snake_position[1] == self.food_position[1]:
            self.score += 1
            self.food_spawn = False
        else:
            self.snake_body.pop()

        if not self.food_spawn:
            self.food_position = [random.randrange(1, (self.screen_width // 10)) * 10,
                                  random.randrange(1, (self.screen_height // 10)) * 10]
            self.food_spawn = True

        if (self.snake_position[0] < 0 or self.snake_position[0] > self.screen_width - 10 or
                self.snake_position[1] < 0 or self.snake_position[1] > self.screen_height - 10):
            self.game_over()

        for block in self.snake_body[1:]:
            if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                self.game_over()

    def update_screen(self):
        self.screen.fill(self.colors["black"])
        self.display_snake()
        self.display_food()
        self.display_score()
        pygame.display.update()
        self.clock.tick(15)

if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
