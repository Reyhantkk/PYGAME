import pygame
import sys

# Pygame'i başlat
pygame.init()

# Ekran ayarlarını yap
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Renk tanımlamaları
black = (0, 0, 0)
white = (255, 255, 255)

# Yazı tipi ve boyutunu ayarla
font_size = 36
font = pygame.font.Font(None, font_size)

# Yazı metnini ve rengini ayarla
text = "Merhaba, Pygame!"
text_surface = font.render(text, True, white)

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ekranı temizle
    screen.fill(black)

    # Yazıyı ekrana çiz
    screen.blit(text_surface, (screen_width / 2 - text_surface.get_width() / 2, screen_height / 2 - text_surface.get_height() / 2))

    # Ekranı güncelle
    pygame.display.flip()

# Pygame'i kapat
pygame.quit()
sys.exit()
