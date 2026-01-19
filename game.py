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
car_width, car_height = 80, 60
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
road_line_x = (road_left + road_right) // 2
# road_line_height = SCREEN_HEIGHT

# Obstacles (other cars)
obstacle_width, obstacle_height = 65, 60
obstacle_x = randint(road_left, road_right - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 11

score = 0

## load images
car_img = pygame.image.load("car.png")
obstacle_img = pygame.image.load("obstacle.png")
car_img = pygame.transform.scale(car_img, (car_width, car_height))
obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_height))

font = pygame.font.SysFont(None, 36)

# Main game loop
running = True
while running:
    screen.fill(BG_COLOR)
    score_text = font.render(f"Score: {int(score)}", True, (225, 185, 45))
    
    score += 0.1
    
    obstacle_y += obstacle_speed
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = randint(road_left, road_right - obstacle_width)
    
    road_y += road_speed
    if road_y >= SCREEN_HEIGHT:
        road_y = 0
    
    pygame.draw.rect(screen, (50, 50, 50), (road_left, 0, road_width, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (50, 50, 50), (road_right, 0, road_width - SCREEN_HEIGHT, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (road_line_x, 0, road_line_width, SCREEN_HEIGHT))
    
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))
    
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
        running = False

    
    
    # draw car
    screen.blit(car_img, (car_x, car_y))

    # update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60) # 60 FPS

pygame.quit()
sys.exit()
