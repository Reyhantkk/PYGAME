import pygame
import sys

pygame.init()

genişlik = 800
yükseklik = 600
pencere = pygame.display.set_mode((genişlik, yükseklik))

spiderman = pygame.image.load("spiderman.png")
spiderman_koordinat = spiderman.get_rect()
spiderman_koordinat.center = (genişlik // 2, yükseklik // 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            # Fare hareketini algıla ve karakterin koordinatlarını güncelle
            spiderman_koordinat.center = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Fareye tıklandığında, karakterin koordinatlarını tıklanan noktaya zıplat
            spiderman_koordinat.center = event.pos

    pencere.fill((0, 0, 0))  # Arka planı temizle
    pencere.blit(spiderman, spiderman_koordinat)  # Karakteri güncellenen koordinatlarla çiz
    pygame.display.update()
    clock.tick(60)  # FPS'i 60 olarak sınırla
