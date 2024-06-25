import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
GRID_SIZE = 20
ROWS, COLS = SCREEN_HEIGHT // GRID_SIZE, SCREEN_WIDTH // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pacman")

# Clock
clock = pygame.time.Clock()
FPS = 10

# Load images
pacman_img = pygame.image.load('pacman.png')
ghost_img = pygame.image.load('ghost.png')

# Scale images
pacman_img = pygame.transform.scale(pacman_img, (GRID_SIZE, GRID_SIZE))
ghost_img = pygame.transform.scale(ghost_img, (GRID_SIZE, GRID_SIZE))

# Initialize game variables
pacman_pos = [ROWS // 2, COLS // 2]
ghost_pos = [random.randint(0, ROWS - 1), random.randint(0, COLS - 1)]
dots = [[random.randint(0, ROWS - 1), random.randint(0, COLS - 1)] for _ in range(50)]
direction = [0, 0]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = [0, -1]
            elif event.key == pygame.K_RIGHT:
                direction = [0, 1]
            elif event.key == pygame.K_UP:
                direction = [-1, 0]
            elif event.key == pygame.K_DOWN:
                direction = [1, 0]

    # Move pacman
    pacman_pos[0] += direction[0]
    pacman_pos[1] += direction[1]

    # Wrap around screen
    pacman_pos[0] %= ROWS
    pacman_pos[1] %= COLS

    # Check collision with dots
    if pacman_pos in dots:
        dots.remove(pacman_pos)

    # Check collision with ghost
    if pacman_pos == ghost_pos:
        running = False
        print("Game Over!")

    # Move ghost randomly
    ghost_direction = random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
    ghost_pos[0] += ghost_direction[0]
    ghost_pos[1] += ghost_direction[1]
    ghost_pos[0] %= ROWS
    ghost_pos[1] %= COLS

    # Drawing
    screen.fill(BLACK)
    for dot in dots:
        pygame.draw.circle(screen, WHITE, (dot[1] * GRID_SIZE + GRID_SIZE // 2, dot[0] * GRID_SIZE + GRID_SIZE // 2),
                           GRID_SIZE // 4)
    screen.blit(pacman_img, (pacman_pos[1] * GRID_SIZE, pacman_pos[0] * GRID_SIZE))
    screen.blit(ghost_img, (ghost_pos[1] * GRID_SIZE, ghost_pos[0] * GRID_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
