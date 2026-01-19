import pygame
import sys
from random import randint

pygame.init()

# Screen settings

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Driving Game")

# Colors
BG_COLOR = (32, 125, 195)
CAR_COLOR = (255, 0, 0)

# Car Settings
car_width, car_height = 40, 60
car_x = SCREEN_WIDTH // 2 - car_width // 2
car_y = SCREEN_HEIGHT - car_height - 10
car_speed = 11

# Road
road_width = 200
road_left = SCREEN_WIDTH // 2 - road_width // 2
road_right = SCREEN_WIDTH // 2 + road_width // 2
road_speed = 10
road_y = 0

# road center line
road_line_width = 7
road_line_x = (road_right // 2 + road_left // 2)
# road_line_height = SCREEN_HEIGHT

# Obstacles (other cars)
obstacle_width, obstacle_height = 40, 60
obstacle_x = randint(road_left, road_right - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 11

score = 0

# Main game loop
running = True
while running:
    screen.fill(BG_COLOR)
    
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (225, 185, 45))
    
    score += 1
    
    obstacle_y += obstacle_speed
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = randint(road_left, road_right - obstacle_width)
    
    road_y += road_speed
    if road_y >= SCREEN_HEIGHT:
        road_y = 0
    
    pygame.draw.rect(screen, (50, 50, 50), (road_left, road_y - SCREEN_HEIGHT, road_width, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (50, 50, 50), (road_left, road_y, road_width, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (road_line_x, 0, road_line_width, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (0, 0, 255), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    screen.blit(score_text, (10, 10))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key handling 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > road_left + road_line_width:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < road_right - road_line_width - car_width:
        car_x += car_speed
    
    if (car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y and car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x):
        print("Crash!")

    
    
    # draw car
    pygame.draw.rect(screen, CAR_COLOR, (car_x, car_y, car_width, car_height))

    # update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60) # 60 FPS

pygame.quit()
sys.exit()
