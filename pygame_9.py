import pygame
import sys

pygame.init()

# Pencere boyutlarını ayarla
genişlik = 800
yükseklik = 600
pencere = pygame.display.set_mode((genişlik, yükseklik))

# Renk tanımlamaları
siyah = (0, 0, 0)

# FPS ayarı için saat
clock = pygame.time.Clock()

# Karakter ayarları
hız = 5
spiderman = pygame.image.load("spiderman.png")
spiderman_koordinat = spiderman.get_rect()
spiderman_koordinat.center = (genişlik // 2, yükseklik // 2)

# Ana döngü
while True:
    # Olayları işle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Klavye durumunu kontrol et
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spiderman_koordinat.x = max(spiderman_koordinat.x - hız, 0)
    if keys[pygame.K_RIGHT]:
        spiderman_koordinat.x = min(spiderman_koordinat.x + hız, genişlik - spiderman_koordinat.width)
    if keys[pygame.K_UP]:
        spiderman_koordinat.y = max(spiderman_koordinat.y - hız, 0)
    if keys[pygame.K_DOWN]:
        spiderman_koordinat.y = min(spiderman_koordinat.y + hız, yükseklik - spiderman_koordinat.height)

    # Arka planı temizle
    pencere.fill(siyah)
    
    # Karakteri güncellenen koordinatlarla çiz
    pencere.blit(spiderman, spiderman_koordinat)
    
    # Ekranı güncelle
    pygame.display.update()
    
    # FPS'i sınırla
    clock.tick(60)  # 60 FPS
