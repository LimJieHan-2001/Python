import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake and food
snake = [(200, 200), (210, 200), (220, 200)]
food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
dx, dy = CELL_SIZE, 0

# Game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
score = 0

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def move_snake():
    global dx, dy, food, score

    # Move the snake
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    # Check if snake has eaten the food
    if head == food:
        food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        score += 1
    else:
        snake.pop()

    # Check if snake has collided with the walls or itself
    if (head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:]):
        return False
    return True

def display_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_snake()
    draw_food()
    display_score()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL_SIZE
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL_SIZE, 0
