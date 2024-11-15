import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Game variables
bucket_width = 100
bucket_height = 20
bucket_x = (SCREEN_WIDTH - bucket_width) // 2
bucket_y = SCREEN_HEIGHT - bucket_height - 10
bucket_speed = 10

ball_radius = 10
ball_x = random.randint(0, SCREEN_WIDTH - ball_radius)
ball_y = 0
ball_speed = 7

score = 0
lives = 3
font = pygame.font.Font(None, 36)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control the bucket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bucket_x > 0:
        bucket_x -= bucket_speed
    if keys[pygame.K_RIGHT] and bucket_x < SCREEN_WIDTH - bucket_width:
        bucket_x += bucket_speed

    # Move the ball
    ball_y += ball_speed

    # Check if the ball is caught
    if bucket_y <= ball_y + ball_radius <= bucket_y + bucket_height and bucket_x <= ball_x <= bucket_x + bucket_width:
        score += 1
        ball_x = random.randint(0, SCREEN_WIDTH - ball_radius)
        ball_y = 0

    # Check if the ball is missed
    if ball_y > SCREEN_HEIGHT:
        lives -= 1
        ball_x = random.randint(0, SCREEN_WIDTH - ball_radius)
        ball_y = 0

    # Draw the bucket
    pygame.draw.rect(screen, BLUE, (bucket_x, bucket_y, bucket_width, bucket_height))

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Display the score and lives
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (SCREEN_WIDTH - 100, 10))

    # Game over condition
    if lives <= 0:
        game_over_text = font.render("Game Over!", True, BLACK)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

pygame.quit()
