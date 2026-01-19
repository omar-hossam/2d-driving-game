import pygame
import sys

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
car_speed = 5

# Road
road_width = 200
road_left = SCREEN_WIDTH // 2 - road_width // 2
road_right = SCREEN_WIDTH // 2 + road_width // 2

# road center line
road_line_width = 7
road_line_x = (road_right // 2 + road_left // 2)
# road_line_height = SCREEN_HEIGHT

# Main game loop
running = True
while running:
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, (50, 50, 50), (road_left, 0, road_width, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (road_line_x, 0, road_line_width, SCREEN_HEIGHT))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key handling 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > road_left:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < road_right - car_width:
        car_x += car_speed
    
    # draw car
    pygame.draw.rect(screen, CAR_COLOR, (car_x, car_y, car_width, car_height))

    # update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60) # 60 FPS

pygame.quit()
sys.exit()
