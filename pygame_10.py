import pygame
import sys

pygame.init()

genişlik = 800
yükseklik = 600
pencere = pygame.display.set_mode((genişlik, yükseklik))

clock = pygame.time.Clock()

# Renkler
siyah = (0, 0, 0)

# Karakter
karakter = pygame.image.load("karakter.png")
karakter_koordinat = karakter.get_rect()
karakter_koordinat.center = (genişlik // 1, yükseklik // 1)

# Engel
engel = pygame.image.load("engel.png")
engel_koordinat = engel.get_rect()
engel_koordinat.center = (genişlik // 2, yükseklik // 2)

hız = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        karakter_koordinat.x -= hız
    if keys[pygame.K_RIGHT]:
        karakter_koordinat.x += hız
    if keys[pygame.K_UP]:
        karakter_koordinat.y -= hız
    if keys[pygame.K_DOWN]:
        karakter_koordinat.y += hız

    # Çarpışma kontrolü
    if karakter_koordinat.colliderect(engel_koordinat):
        print("Çarpışma!")

    pencere.fill(siyah)
    pencere.blit(karakter, karakter_koordinat)
    pencere.blit(engel, engel_koordinat)
    pygame.display.update()

    clock.tick(60)
