import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Анімація спрайтів")

# Завантаження зображень для анімації
sprite_images = [
    pygame.image.load("1.jpg"),
    pygame.image.load("2.jpg"),
    pygame.image.load("3.jpg"),
    pygame.image.load("4.jpg")
]

# Клас для нашого спрайта
class AnimatedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = sprite_images
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.animation_speed = 1
        self.time = 5
    
    def update(self):
        self.time += self.animation_speed
        if self.time >= len(self.images):
            self.time = 0
        self.current_image = int(self.time)
        self.image = self.images[self.current_image]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1

# Створення групи спрайтів та додавання нашого спрайта
all_sprites = pygame.sprite.Group()
player = AnimatedPlayer()
all_sprites.add(player)

# Головний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Оновлення спрайтів
    all_sprites.update()
    
    # Очищення екрану
    screen.fill((255, 255, 255))
    
    # Малювання спрайтів
    all_sprites.draw(screen)
    
    # Оновлення екрану
    pygame.display.flip()

pygame.quit()