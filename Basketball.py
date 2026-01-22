import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Basketball")
clock = pygame.time.Clock()

coby = pygame.Rect(30, 450, 20, 100)

ball_radius = 20
ball_color = "orange"

GAME_RUNNING = "running"
GAME_OVER = "over"
game_state = GAME_RUNNING

# Trajectory
ball_pos = [0, 0]
ball_vel = [0, 0]
ball_shot = False

gravity = 0.5
shoot_power_x = 10 
shoot_power_y = -15 

def move_hoop():
    y = random.randint(200, 700)
    return pygame.Rect(700, y, 100, 20)

hoop = move_hoop()
hoop_top = pygame.Rect(739, hoop.y, 80, 5)


shot_scored = False

score = 0
font_score = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill("light blue")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        coby.y -= 5
    if keys[pygame.K_DOWN]:
        coby.y += 5

    # Ball Trajectory
    if keys[pygame.K_SPACE] and not ball_shot:
        ball_shot = True
        shot_scored = False
        ball_vel = [shoot_power_x, shoot_power_y]


    if not ball_shot:
        ball_pos = [coby.x + 40, coby.y + 20]
    else:
    # Ball physics
        ball_vel[1] += gravity
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
    if ball_shot and (ball_pos[1] > 900 or ball_pos[0] > 900):
        if not shot_scored:
            score = 0  
        ball_shot = False
        shot_scored = False


    ball_rect = pygame.Rect(
    ball_pos[0] - ball_radius,
    ball_pos[1] - ball_radius,
    ball_radius * 2,
    ball_radius * 2
    )
    hoop_top = pygame.Rect(739, hoop.y, 80, 5)
   
    # Collision
    if game_state == GAME_RUNNING:
        if ball_rect.colliderect(hoop_top):
            ball_shot = False
            shot_scored = True
            hoop = move_hoop()
            score += 1
   # Score
    score_text = font_score.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
   
    pygame.draw.rect(screen, "brown", coby)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.draw.rect(screen,"red",hoop )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
