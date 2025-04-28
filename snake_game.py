import random
import pygame
import sys

pygame.init()

# Set screen size
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game by Lahari")

# Snake and food starting position
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0

food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)

# Clock to control speed
clock = pygame.time.Clock()

# Snake body list
snake_body = [(snake_x, snake_y)]

# Main game function
def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y

    # Move snake
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Check collision with itself
    if (snake_x, snake_y) in snake_body[1:]:
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    snake_body.append((snake_x, snake_y))

    # Check if food eaten
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)
    else:
        del snake_body[0]

    # Draw everything
    game_screen.fill((150, 150, 150))
    pygame.draw.circle(game_screen, (0, 0, 128), (food_x, food_y), 6)
    for (x, y) in snake_body:
        pygame.draw.circle(game_screen, (255, 255, 102), (x, y), 6)

    pygame.display.update()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -10
                change_y = 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x = 10
                change_y = 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_x = 0
                change_y = -10
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_x = 0
                change_y = 10

    display_snake_and_food()
    clock.tick(15)
