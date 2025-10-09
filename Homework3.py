import pygame
import math
import os


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рух")


sprite_folder = "sprites"  
sprite_frames = [pygame.image.load(os.path.join(sprite_folder, f)) for f in sorted(os.listdir(sprite_folder)) if f.endswith(".jpg")]
total_frames = len(sprite_frames)


center_x, center_y = WIDTH // 2, HEIGHT // 2
radius = 300


angle = 0
angle_speed = 0.02  

clock = pygame.time.Clock()
FPS = 60

frame_index = 0
frame_timer = 0
frame_delay = 5

running = True
while running:
    clock.tick(FPS)
    screen.fill((30, 30, 30))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    angle += angle_speed

    
    frame_timer += 1
    if frame_timer >= frame_delay:
        frame_timer = 0
        frame_index = (frame_index + 1) % total_frames

    sprite = sprite_frames[frame_index]

    
    direction_angle = math.degrees(angle) + 90
    rotated_sprite = pygame.transform.rotate(sprite, -direction_angle)
    rect = rotated_sprite.get_rect(center=(x, y))

    screen.blit(rotated_sprite, rect)

    pygame.display.flip()

pygame.quit()
