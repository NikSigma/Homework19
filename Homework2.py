import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("спрайт")


run_images = [pygame.image.load(f"run{i}.jpg") for i in range(1, 5)] 
current_image = 0


x, y = 100, 400
clock = pygame.time.Clock()

running = True
is_running = False
animation_speed = 0.2

while running:
    screen.fill((135, 206, 235))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        is_running = True
        y -= 5 
    else:
        is_running = False

    if is_running:
        current_image += animation_speed
        if current_image >= len(run_images):
            current_image = 0
    else:
        current_image = 0

    screen.blit(run_images[int(current_image)], (x, y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
