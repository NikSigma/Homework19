import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рух спрайта")


WHITE = (255, 255, 255)

sprite = pygame.image.load("sticman.jpg")
sprite_rect = sprite.get_rect()
sprite_rect.topleft = (WIDTH // 2, HEIGHT // 2)


speed = 5


running = True
while running:
    screen.fill(WHITE)

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]: 
        sprite_rect.x -= speed
    if keys[pygame.K_d]: 
        sprite_rect.x += speed
    if keys[pygame.K_w]:  
        sprite_rect.y -= speed
    if keys[pygame.K_s]:
        sprite_rect.y += speed

    
    screen.blit(sprite, sprite_rect)

   
    pygame.display.flip()
    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()
