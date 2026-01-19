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
CAR_SIZE = (75, 60)
OBSTACLE_SIZE = (75, 60)
car_speed = 11
obstacle_speed = 11

# Road
road_width = 200
road_left = SCREEN_WIDTH // 2 - road_width // 2
road_right = SCREEN_WIDTH // 2 + road_width // 2
road_speed = 10
road_y = 0

# road center line
road_line_width = 7
road_line_x = (road_left + road_right) // 2

## load images
car_img = pygame.image.load("car.png")
obstacle_img = pygame.image.load("obstacle.png")

# Scale images 
car_img = pygame.transform.scale(car_img, CAR_SIZE)
obstacle_img = pygame.transform.scale(obstacle_img, OBSTACLE_SIZE)

# NOW get rects that match the images
car_rect = car_img.get_rect()
obstacle_rect = obstacle_img.get_rect()
car_rect.inflate_ip(-20, -10)
obstacle_rect.inflate_ip(-20, -10)

# Position cars properly
car_rect.centerx = SCREEN_WIDTH // 2
car_rect.bottom = SCREEN_HEIGHT - 20

obstacle_rect.x = randint(road_left, road_right - obstacle_rect.width)
obstacle_rect.y = -obstacle_rect.height


# others
score = 0
font = pygame.font.SysFont(None, 36)

# Main game loop
running = True
while running:
    screen.fill(BG_COLOR)
    score_text = font.render(f"Score: {int(score)}", True, (225, 185, 45))
    
    score += 0.1
    
    obstacle_rect.y += obstacle_speed
    if obstacle_rect.y > SCREEN_HEIGHT:
        obstacle_rect.y = -obstacle_rect.height
        obstacle_rect.x = randint(road_left, road_right - obstacle_rect.width)
    
    road_y += road_speed
    if road_y >= SCREEN_HEIGHT:
        road_y = 0
    
    pygame.draw.rect(screen, (50, 50, 50), (road_left, 0, road_width, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (road_line_x, 0, road_line_width, SCREEN_HEIGHT))

    screen.blit(obstacle_img, obstacle_rect)
    
    screen.blit(score_text, (10, 10))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key handling 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.left > road_left - road_line_width -5:
        car_rect.x -= car_speed
    if keys[pygame.K_RIGHT] and car_rect.right < road_right - road_line_width:
        car_rect.x += car_speed
    
    if car_rect.colliderect(obstacle_rect):
        print("Crash!")
        running = False

    
    
    # draw car
    screen.blit(car_img, car_rect)

    # update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60) # 60 FPS

pygame.quit()
sys.exit()
