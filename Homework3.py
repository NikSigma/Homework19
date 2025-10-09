import pygame
import math
import os

# Ініціалізація Pygame
pygame.init()

# Параметри вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рух по колу")

# Завантаження спрайтів
sprite_folder = "sprites"  # Папка з кадрами спрайта
sprite_frames = [pygame.image.load(os.path.join(sprite_folder, f)) for f in sorted(os.listdir(sprite_folder)) if f.endswith(".png")]
total_frames = len(sprite_frames)

# Центр кола
center_x, center_y = WIDTH // 2, HEIGHT // 2
radius = 150

# Кут і швидкість
angle = 0
angle_speed = 0.02  # Чим більше, тим швидше

# Частота оновлення
clock = pygame.time.Clock()
FPS = 60

# Для анімації спрайтів
frame_index = 0
frame_timer = 0
frame_delay = 5  # Затримка між кадрами (чим менше, тим швидше змінюються кадри)

running = True
while running:
    clock.tick(FPS)
    screen.fill((30, 30, 30))  # Тло

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Розрахунок позиції по колу
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    angle += angle_speed

    # Оновлення кадру спрайта
    frame_timer += 1
    if frame_timer >= frame_delay:
        frame_timer = 0
        frame_index = (frame_index + 1) % total_frames

    sprite = sprite_frames[frame_index]

    # Обертаємо спрайт в напрямку руху (за бажанням)
    direction_angle = math.degrees(angle) + 90
    rotated_sprite = pygame.transform.rotate(sprite, -direction_angle)
    rect = rotated_sprite.get_rect(center=(x, y))

    screen.blit(rotated_sprite, rect)

    pygame.display.flip()

pygame.quit()
