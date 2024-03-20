import pygame
import random

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
        self.font = pygame.font.Font(None, 36)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                    self.snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                    self.snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                    self.snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                    self.snake.direction = (1, 0)

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.position = self.food.randomize_position()
            self.score += 1
        if self.snake.check_collision() or self.snake.check_boundary():
            self.game_over()

    def game_over(self):
        pygame.quit()
        quit()

    def draw(self, surface):
        surface.fill(BLACK)
        self.snake.draw(surface)
        self.food.draw(surface)
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        surface.blit(score_text, (10, 10))

# Main function
def main():
    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Set up the clock
    clock = pygame.time.Clock()

    # Initialize the game
    game = Game()

    # Main loop
    while True:
        # Handle input
        game.handle_input()

        # Update game state
        game.update()

        # Draw to the screen
        game.draw(screen)

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
