import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Sound effects
EAT_SOUND = pygame.mixer.Sound(os.path.join("sounds", "eat.wav"))
CRASH_SOUND = pygame.mixer.Sound(os.path.join("sounds", "crash.wav"))

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, 1)

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def draw(self, surface):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(surface, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:]:
            return True
        return False

    def check_boundary(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        return False

# Food class
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        x, y = self.position
        pygame.draw.rect(surface, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Game class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.high_score = self.load_high_score()
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.clock = pygame.time.Clock()

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if not self.game_over:
                    if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                        self.snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                        self.snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        self.snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                        self.snake.direction = (1, 0)
                else:
                    if event.key == pygame.K_RETURN:
                        self.restart_game()

    def update(self):
        if not self.game_over:
            self.snake.move()
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.position = self.food.randomize_position()
                self.score += 1
                EAT_SOUND.play()
                if self.score > self.high_score:
                    self.high_score = self.score
            if self.snake.check_collision() or self.snake.check_boundary():
                self.game_over = True
                CRASH_SOUND.play()
                self.save_high_score()

    def restart_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False

    def draw(self, surface):
        surface.fill(BLACK)
        if not self.game_over:
            self.snake.draw(surface)
            self.food.draw(surface)
            score_text = self.font.render("Score: " + str(self.score), True, WHITE)
            surface.blit(score_text, (10, 10))
        else:
            game_over_text = self.font.render("Game Over!",
